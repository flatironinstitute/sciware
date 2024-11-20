// @ts-check
/**
 * This is a Node.js script to generate the
 * index.html page for the Sciware website.
 * — Paul Murray, 2024-03-13
 */

import fs from "node:fs";
import { execSync } from "node:child_process";

// Add events here to have them appear at the top of the page.
// If this array is empty, the page will display a message saying there are no upcoming events.
const upcoming_events = [
  // {
  //   title: `Tool Setup, Intro to the Shell and the Cluster`,
  //   weekday: `Tuesday`,
  //   date: `June 4`,
  //   time: `10 AM – 12:30 PM`,
  //   location: `162 5th Ave<br />IDA Auditorium`,
  //   summary: `
  //   Learn about the cluster and navigating the command line, and setup your laptop for coding.`,
  // },
  // {
  //   title: `Intro to Visual Studio Code`,
  //   weekday: `Wednesday`,
  //   date: `June 12`,
  //   time: `10 AM – 12:30 PM`,
  //   location: `162 5th Ave<br />IDA Auditorium`,
  //   summary: `Learn how Visual Studio Code can help you be a better Python programmer.`,
  // },
  // {
  //   title: `NVIDIA Intro to Machine Learning`,
  //   weekday: `Monday – Tuesday`,
  //   date: `June 17 – 18`,
  //   time: `All Day`,
  //   location: `162 5th Ave<br />IDA Auditorium`,
  //   summary: `Learn to use the popular <code>torch</code> Python package to train machine learning models using cluster hardware.`,
  // },
  // {
  //   title: `Intro to GitHub, Part 1`,
  //   weekday: `Thursday`,
  //   date: `June 20`,
  //   time: `10 AM – 12:30 PM`,
  //   location: `162 5th Ave<br />IDA Auditorium`,
  //   summary: `Get setup with <code>git</code> and local version control.`,
  // },
  // {
  //   title: `Intro to GitHub, Part 2`,
  //   weekday: `Thursday`,
  //   date: `June 27`,
  //   time: `10 AM – 12:30 PM`,
  //   location: `162 5th Ave<br />IDA Auditorium`,
  //   summary: `Connect to Github and learn how to collaborate on code.`,
  // },
  // {
  //   title: `Intro to Python Packaging`,
  //   weekday: `Thursday`,
  //   date: `September 26`,
  //   time: `3 — 5 PM`,
  //   location: `162 5th Ave<br />3rd Floor Classroom`,
  //   summary: html`In this Sciware workshop, we'll discuss Python packaging and relevant tools. Our main focus will be on how to get a project <code>pip</code>-installable using a <code>pyproject.toml</code> file and <code>setuptools</code>. We'll work together to make a test project where everyone can go through the steps of organizing and making a Python package.`,
  // },
  // {
  //   title: `Extended Intro to High-Performance Computing`,
  //   weekday: `Wednesday`,
  //   date: `October 2`,
  //   time: `10 AM — Noon`,
  //   location: `162 5th Ave<br />IDA Auditorium`,
  //   summary: html` In this SCC-hosted Sciware, we will introduce cluster terminology and describe the two Flatiron clusters, <code>popeye</code> and <code>rusty</code>. In the interactive session, we will learn to make use of the software and hardware resources available by setting up a Python environment and running a Python script on the cluster by submitting jobs using <code>slurm</code>. In addition, we will demonstrate how to use <code>mpi4py</code> and <code>disBatch</code> to run distributed Python tasks. `,
  // },
  {
    // Date- Thur Nov 21 at 10am-12pm.
    title: `How to publish a (hopefully) reproducible paper`,
    weekday: `Thursday`,
    date: `November 21`,
    time: `10 AM — Noon`,
    location: `160 5th Ave<br />4th Floor Classroom`,
    summary: html`There is a lot of code and data that goes into a paper (simulation, analysis, plotting) that doesn't belong in a software package. How do you share that code and data so that it is possible for your work to be reproducible? In this workshop, we will discuss considerations around sharing such code and data. Tools and topics will include workflow managers like Snakemake; software environments & installability; GitHub; README best practices; using repositories and data archives such as Zenodo; licensing; and more. We will focus on code and data products which are not intended to be maintained or generalizable but rather which are particular to a specific publication.`,
  },
];

// This is an array of past events, with the format:
// [session number, title, date, slides link, github link, vimeo link]
// The array is reversed so that the most recent events appear first.
const past_events = [
  [`Session #00`, `Founding`, `Feb 28, 2019`, `/00_Founding/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/00_Founding`],
  [`Session #01`, `Overview`, `Mar 28, 2019`, `/01_Overview/reveal.html`, `https://github.com/flatironinstitute/sciware/tree/main/01_Overview`],
  [`Session #02`, `Testing Scientific Software`, `May 09, 2019`, `/02_Testing/reveal.html`, `https://github.com/flatironinstitute/sciware/tree/main/02_Testing`],
  [`Session #03`, `Tools and Workflows Show and Tell Intro`, `Jul 18, 2019`, `/03_ToolsWorkflows/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/03_ToolsWorkflows`],
  [`Session #04a`, `Debugging Strategies`, `Aug 29, 2019`, `/04_Debugging/slides1.html`, `https://github.com/flatironinstitute/sciware/tree/main/04_Debugging`],
  [`Session #04b`, `Debugging: System Tools`, `Aug 29, 2019`, `/04_Debugging/slides2.html`, `https://github.com/flatironinstitute/sciware/tree/main/04_Debugging`],
  [`Session #05a`, `Parallel and Distributed APIs`, `Oct 17, 2019`, `/05_Parallelization/slides-apis.html`, `https://github.com/flatironinstitute/sciware/tree/main/05_Parallelization`],
  [`Session #05b`, `Parallel and Distributed Computing`, `Oct 17, 2019`, `/05_Parallelization/slides-intro.html`, `https://github.com/flatironinstitute/sciware/tree/main/05_Parallelization`],
  [`Session #05c`, `Parallel and Distributed terminology`, `Feb 28, 2019`, `/05_Parallelization/slides-terms.html`, `https://github.com/flatironinstitute/sciware/tree/main/05_Parallelization`],
  [`Session #06`, `Modern C++`, `Jan 30, 2020`, `/06_ModernC++/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/06_ModernC%2B%2B`],
  [`Session #07`, `Working Remotely`, `Apr 16, 2020`, `/07_RemoteWork/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/07_RemoteWork`],
  [`Session #08`, `Intro to Julia`, `May 14, 2020`, `/08_Julia/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/08_Julia`, `https://vimeo.com/showcase/7164070/video/421645775`],
  [`Session #09`, `Intel VTune`, `Jun 18, 2020`, `/09_IntelVTune/slides.html`, null, `https://vimeo.com/showcase/7164070/video/431887277`],
  [`Session #10`, `Shells and Environments`, `Aug 13, 2020`, `/10_EnvShell/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/10_EnvShell`, `https://vimeo.com/showcase/7164070/video/451198564`],
  [`Session #11`, `Intro to Git with Software Carpentry`, `Sep 24 - Oct 01, 2020`, `/11_GitSWC/slides.html`, `https://github.com/flatironinstitute/sciware-swc-2020-09-git`],
  [`Session #12`, `Functions`, `Nov 06, 2020`, `/12_Functions/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/12_Functions`, `https://vimeo.com/showcase/7164070/video/480005445`],
  [`Session #13`, `Debugging`, `Mar 04, 2021`, `/13_Debugging/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/13_Debugging`, `https://vimeo.com/showcase/7164070/video/521019306`],
  [`Session #14a`, `Testing and Packaging workshop`, `Apr 29, 2021`, `/14_TestingPackaging/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/14_TestingPackaging`, `https://vimeo.com/showcase/7164070/video/551569254`],
  [`Session #15 day 1`, `Intro to Github`, `Jun 16, 2021`, `/15_IntroGithub/slides1.html`, `https://github.com/flatironinstitute/sciware/tree/main/15_IntroGithub`, `https://vimeo.com/showcase/7164070/video/568915163`],
  [`Session #15 day 2`, `Collaboration with Github`, `Jun 17, 2021`, `/15_IntroGithub/slides2.html`, `https://github.com/flatironinstitute/sciware/tree/main/15_IntroGithub`],
  [`Session #16`, `Intro to code editors`, `Jul 08, 2021`, `/16_EditorsVSCode/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/16_EditorsVSCode`, `https://vimeo.com/showcase/7164070/video/574579678`],
  [`Session #17`, `Performance-focused guide to using Flatiron Clusters`, `Nov 04, 2021`, `/17_FICluster/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/17_FICluster`, `https://vimeo.com/showcase/7164070/video/667883784`],
  [`Session #18`, `3D Scientific Visualization with Blender`, `Oct 21, 2021`, `/18_Blender/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/18_Blender`, `https://vimeo.com/showcase/7164070/video/639252185`],
  [`Session #19`, `Performance Troubleshooting and Profiling`, `Jan 27, 2022`, `/19_Profiling/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/19_Profiling`, `https://vimeo.com/showcase/7164070/video/672382395`],
  [`Session #20`, `Documentation: How to win users and influence science`, `Mar 24, 2022`, `/20_Documentation/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/20_Documentation`, `https://vimeo.com/showcase/7164070/video/695811502`],
  [`Session #21`, `Intro to Git and Github`, `June 21 - 22, 2022`, `/21_IntroGithub`, `https://github.com/flatironinstitute/sciware/tree/main/21_IntroGithub`, `https://vimeo.com/showcase/7164070`],
  [`Session #22`, `Intro to code editors and debugging`, `June 29, 2022`, `/22_Editors/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/22_Editors`, `https://vimeo.com/showcase/7164070/video/731055316`],
  [`Session #23`, `Command-line interaction and shells`, `July 21, 2022`, `/23_CommandLine/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/23_CommandLine`, `https://vimeo.com/showcase/7164070/video/733280307`],
  [`Session #24`, `Types`, `September 29, 2022`, `/24_Types/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/24_Types`, `https://vimeo.com/showcase/7164070/video/778892798`],
  [`Session #25`, `Modern C++`, `October 20, 2022`, `/25_ModernC++/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/25_ModernC++`, `https://vimeo.com/showcase/7164070/video/778640628`],
  [`Session #26`, `File Formats and Storing Data`, `December 15, 2022`, `/26_DataFormats/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/26_DataFormats`, `https://vimeo.com/showcase/7164070/video/797753028`],
  [`Session #27 day 1`, `Summer Intro Series`, `May 31, 2023`, `/27_SummerIntro`, `https://github.com/flatironinstitute/sciware/tree/main/27_SummerIntro`, `https://vimeo.com/showcase/7164070/video/832383176`],
  [`Session #27 day 2`, `Summer Intro Series`, `June 6, 2023`, `/27_SummerIntro/day2.html`, `https://github.com/flatironinstitute/sciware/tree/main/27_SummerIntro`, `https://vimeo.com/showcase/7164070/video/835496004`],
  [`Session #27 day 3`, `Summer Intro Series`, `June 14, 2023`, `/27_SummerIntro/day3.html`, `https://github.com/flatironinstitute/sciware/tree/main/27_SummerIntro`, `https://vimeo.com/showcase/7164070/video/885375948`],
  [`Session #27 day 4`, `Summer Intro Series`, `June 21, 2023`, `/27_SummerIntro/day4.html`, `https://github.com/flatironinstitute/sciware/tree/main/27_SummerIntro`, `https://vimeo.com/showcase/7164070/video/885382496`],
  [`Session #28`, `CCB-Hosted Sciware`, `September 21, 2023`, `/28_CCB/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/28_CCB`, `https://vimeo.com/showcase/7164070/video/885390328`],
  [`Session #29`, `CCA-Hosted Sciware`, `November 11, 2023`, `/29_CCA/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/29_CCA`, `https://vimeo.com/showcase/7164070/video/885395764`],
  [`Session #30`, `Programming Language Interoperability`, `February 15, 2024`, `/30_CCQ/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/30_CCQ`, `https://vimeo.com/showcase/7164070/video/939128628`],
  [`Session #31`, `Code Writing Robots and LLM Magic: The Good, The Bad, and The Ugly`, `March 28, 2024`, `/31_CodeRobots/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/31_CodeRobots`, `https://vimeo.com/showcase/7164070/video/938814931`],
  [`Session #32`, `Intro to High-Performance Computing`, `April 25, 2024`, `/32_IntroToHPC/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/32_IntroToHPC`],
  [`Session #33 day 1`, `Command line and Shell interaction`, `June 4, 2024`, `/33_SummerIntro/day1.html`, `https://github.com/flatironinstitute/sciware/tree/main/33_SummerIntro`],
  [`Session #33 day 2`, `Intro to VS Code`, `June 12, 2024`, `/33_SummerIntro/day2.html`, `https://github.com/flatironinstitute/sciware/tree/main/33_SummerIntro`],
  [`Session #33 day 3`, `Intro to GitHub, Part 1`, `June 20, 2024`, `/33_SummerIntro/day3.html`, `https://github.com/flatironinstitute/sciware/tree/main/33_SummerIntro`],
  [`Session #33 day 4`, `Intro to GitHub, Part 2`, `June 27, 2024`, `/33_SummerIntro/day4.html`, `https://github.com/flatironinstitute/sciware/tree/main/33_SummerIntro`],
  [`Session #34`, `Python Packaging`, `September 26, 2024`, `/34_PyPackaging/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/34_PyPackaging`],
  [`Session #35`, `Extended Intro to HPC`, `October 2, 2024`, `/35_IntroToHPC/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/35_IntroToHPC`],
  [`Session #36`, `How to publish a (hopefully) reproducible paper`, `November 21, 2024`, `/36_ReproduciblePaper/slides.html`, `https://github.com/flatironinstitute/sciware/tree/main/36_ReproduciblePaper`],
];

const upcoming_events_list_items = upcoming_events.map(({ title, weekday, date, time, location, summary }) => {
  return html`
    <li>
      <div class="details">
        <div data-type="weekday">${weekday}</div>
        <div data-type="date">${date}</div>
        <div data-type="time">${time}</div>
        <div data-type="location">${location}</div>
      </div>
      <div class="summary">
        <h3>${title}</h3>
        <p>${summary}</p>
      </div>
    </li>
  `;
});

const upcoming_events_list = html`
  <ul>
    ${upcoming_events_list_items}
  </ul>
`;

const past_events_list = past_events.reverse().map(([session, title, date, link, github, vimeo]) => {
  const g = github ? html`<a href="${github}" class="icon inline-icon brands fa-github" target="_blank" rel="noopener noreferrer"></a>` : ``;
  const v = vimeo ? html`<a href="${vimeo}" class="icon inline-icon brands fa-vimeo" target="_blank" rel="noopener noreferrer"></a>` : ``;
  // prettier-ignore
  return html`
      <li>
        <span>${session}:</span>
        ${link ? html`<a href="${link}">${title}</a>` : html`<span style="color: #717171;">${title}</span>`}
        ${g}
        ${v}
        <span class="inline-date">${date}</span>
      </li>
    `;
});

// prettier-ignore
const organizers = [
  `Kelle Cruz, Flatiron`,
  `Dylan Simon, SCC`,
  `Robert Blackwell, SCC`,
  `Billy Broderick, CCN`,
  `Chris Edelmaier, CCB`,
  `Lehman Garrison, SCC`,
  `Geraud Krawezik, SCC`,
  `Jeff Soules, CCM`,
  `Nils Wentzell, CCQ`,
];

const about_section = html`
  <div>
    <p> <b>Sciware</b> is a Flatiron-wide activity to share and build scientific software development and computing skills in a variety of areas. Our goal is to create an environment where everyone can discuss technologies, tools, and tricks that make their research process more efficient, across all experience levels, language and technology choices, and scientific disciplines. </p>
    <p> We meet roughly once a month on Thursdays at 3pm and focus on a specific topic, bringing Flatiron (and occasionally external) expertise together to demonstrate and discuss everything from debuggers to editors to file formats, optimization to packaging. Events are open to all Flatiron and Simons Foundation researchers, as well as their external students and collaborators. </p>
    <p>
      There is also a
      <a href="https://simonsfoundation.slack.com/archives/CDU1EE9V5" alt="#sciware Slack Channel">#sciware </a>
      channel on the Simons Foundation Slack that everyone is encouraged to join and ask questions, share knowledge, or request code reviews.
    </p>
  </div>
  <div>
    <h2>Organizers</h2>
    ${organizers.map((name) => html`<li>${name}</li>`)}
    <div style="height: 2rem;"></div>
    <h2>Contact</h2>
    <div style="display: flex; column-gap: 1rem;">
      <h3 class="icon solid fa-envelope">
        <span class="label">Email</span>
      </h3>
      <a href="mailto:sciware@flatironinstitute.org">sciware@flatironinstitute.org</a>
    </div>
  </div>
`;

const main_contents = html`
  <section id="upcoming">
    <h2>Upcoming Sciware Events</h2>
    ${upcoming_events_list_items.length > 0 ? upcoming_events_list : html`<p>There are no upcoming events at this time.</p>`}
  </section>
  <section id="past">
    <h2>Previous Events</h2>
    <p>
      In addition to the session slides listed below, many of the recordings from past events are available on
      <a href="https://vimeo.com/showcase/sciware">Vimeo</a>. Please see the <a href="https://simonsfoundation.slack.com/archives/CDU1EE9V5" alt="sciware slack">#sciware </a>Slack channel for the password.
    </p>
    <ul>
      ${past_events_list}
    </ul>
  </section>
  <section id="about">
    <h2>About</h2>
    <div class="columns">${about_section}</div>
  </section>
`;

const head_contents = html`
  <title>Sciware: a scientific software development learning community"</title>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
  <link rel="shortcut icon" href="/icons/favicon.ico" />
  <link rel="stylesheet" href="assets/css/main-v2.css" />
`;

const header_contents = html`
  <a href="#" style="width: 6rem; border-bottom: none;"><img src="assets/sciware.png" alt="" /></a>
  <h1>
    <strong>Sciware</strong>, a scientific<br />
    software learning community <br />
    at the <a href="http://flatironinstitute.org">Flatiron Institute</a>.
  </h1>
`;

const socials = [
  [`GitHub`, `Sciware GitHub repository`, `https://github.com/flatironinstitute/sciware`, `brands fa-github`],
  [`Slack`, `#sciware Slack channel`, `https://simonsfoundation.slack.com/archives/CDU1EE9V5`, `brands fa-slack`],
  [`Vimeo`, `Sciware Vimeo showcase`, `https://vimeo.com/showcase/sciware`, `brands fa-vimeo`],
  [`Email`, `Email sciware`, `mailto:sciware@flatironinstitute.org`, `solid fa-envelope`],
];

const footer_contents = html`
  <ul class="icons">
    ${socials.map(([title, alt, url, classname]) => {
      return html`
        <li>
          <a href="${url}" class="icon ${classname}" alt="${alt}">
            <span class="label">${title}</span>
          </a>
        </li>
      `;
    })}
  </ul>
`;

const template = html`<!DOCTYPE html>
  <html>
    <head>
      ${head_contents}
    </head>
    <body>
      <header>${header_contents}</header>
      <main>${main_contents}</main>
      <footer>${footer_contents}</footer>
    </body>
  </html> `;

fs.writeFileSync("index.html", template);

execSync("npx prettier --write index.html", { stdio: "inherit" });

/**
 * This is a tagged template function to generate HTML strings.
 * It is very similar in spirit to the `html` function in the `lit-html` library.
 */
function html(strings, ...values) {
  let result = "";
  for (const [i, string] of strings.entries()) {
    result += string;
    if (i >= values.length) continue;
    let value = values[i];
    // Process arrays by recursively processing each element
    if (Array.isArray(value)) {
      value = value
        .map((element) => {
          if (Array.isArray(element) || typeof element === "function") {
            return html`${element}`;
          }
          return element;
        })
        .join("\n");
    } else if (value == null) {
      // Handle undefined and null values safely
      value = "";
    }
    result += value; // Append the processed value to the result
  }
  return result;
}
