// @ts-check
/**
 * This is a Node.js script to generate the index.html page for the Sciware website.
 * It's a little messy, sorry. — Paul Murray, 2024-02-06
 */

import fs from "node:fs";
import { execSync } from "node:child_process";

const upcoming_events = [
  {
    title: `Code Writing Robots and LLM Magic:<br />The Good, The Bad, and The Ugly`,
    weekday: `Thursday`,
    date: `March 28`,
    time: `3:00 PM - 5:00 PM`,
    location: `160 5th Ave<br />3rd Floor<br />CCM Classroom`,
    summary: `We will discuss ways to develop software more quickly using tools which analyze and generate code.  Specifically, we’ll talk about static analysis tools (e.g., pylint, ruff, clangd) and GitHub Copilot. We’ll discuss how to use these tools and their pros and cons.`,
  },
];

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
  [`Session #22`, `Intro to code editors and debugging`, `June 29, 2022`, `/22_Editors`, `https://github.com/flatironinstitute/sciware/tree/main/22_Editors`, `https://vimeo.com/showcase/7164070/video/731055316`],
  [`Session #23`, `Command-line interaction and shells`, `July 21, 2022`, `/23_CommandLine`, `https://github.com/flatironinstitute/sciware/tree/main/23_CommandLine`, `https://vimeo.com/showcase/7164070/video/733280307`],
  [`Session #24`, `Types`, `September 29, 2022`, `/24_Types`, `https://github.com/flatironinstitute/sciware/tree/main/24_Types`, `https://vimeo.com/showcase/7164070/video/778892798`],
  [`Session #25`, `Modern C++`, `October 20, 2022`, `/25_ModernC++`, `https://github.com/flatironinstitute/sciware/tree/main/25_ModernC++`, `https://vimeo.com/showcase/7164070/video/778640628`],
  [`Session #26`, `File Formats and Storing Data`, `December 15, 2022`, `/26_DataFormats`, `https://github.com/flatironinstitute/sciware/tree/main/26_DataFormats`, `https://vimeo.com/showcase/7164070/video/797753028`],
  [`Session #27 day 1`, `Summer Intro Series`, `May 31, 2023`, `/27_SummerIntro`, `https://github.com/flatironinstitute/sciware/tree/main/27_SummerIntro`, `https://vimeo.com/showcase/7164070/video/832383176`],
  [`Session #27 day 2`, `Summer Intro Series`, `June 6, 2023`, `/27_SummerIntro/day2.html`, `https://github.com/flatironinstitute/sciware/tree/main/27_SummerIntro`, `https://vimeo.com/showcase/7164070/video/835496004`],
  [`Session #27 day 3`, `Summer Intro Series`, `June 14, 2023`, `/27_SummerIntro/day3.html`, `https://github.com/flatironinstitute/sciware/tree/main/27_SummerIntro`, `https://vimeo.com/showcase/7164070/video/885375948`],
  [`Session #27 day 4`, `Summer Intro Series`, `June 21, 2023`, `/27_SummerIntro/day4.html`, `https://github.com/flatironinstitute/sciware/tree/main/27_SummerIntro`, `https://vimeo.com/showcase/7164070/video/885382496`],
  [`Session #28`, `CCB-Hosted Sciware`, `September 21, 2023`, `/28_CCB/`, null, `https://vimeo.com/showcase/7164070/video/885390328`],
  [`Session #29`, `CCA-Hosted Sciware`, `November 11, 2023`, `/29_CCA/`, null, `https://vimeo.com/showcase/7164070/video/885395764`],
  [`Session #30`, `Programming Language Interoperability`, `February 15, 2024`, `/30_CCQ/`, `https://github.com/flatironinstitute/sciware/tree/main/30_CCQ`],
];

const upcoming_events_list = upcoming_events.map(({ title, weekday, date, time, location, summary }) => {
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

const past_events_list = past_events.reverse().map(([session, title, date, link, github, vimeo]) => {
  const g = github ? html`<a href="${github}" class="icon inline-icon brands fa-github"></a>` : ``;
  const v = vimeo ? html`<a href="${vimeo}" class="icon inline-icon brands fa-vimeo"></a>` : ``;
  // prettier-ignore
  return html`
      <li>
        <span>${session}:</span>
        <a href="${link}">${title}</a>
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
    <ul>
      ${upcoming_events_list}
    </ul>
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

fs.writeFileSync("index-v2.html", template);

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
