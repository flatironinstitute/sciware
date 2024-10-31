# Sciware

## How to (try to) publish a reproducible paper

https://sciware.flatironinstitute.org/36_ReproduciblePaper

https://github.com/flatironinstitute/sciware/tree/main/36_ReproduciblePaper


## Rules of Engagement

### Goal:

Activities where participants all actively work to foster an environment which encourages participation across experience levels, coding language fluency, *technology choices*\*, and scientific disciplines.

<small>\*though sometimes we try to expand your options</small>


## Rules of Engagement

- Avoid discussions between a few people on a narrow topic
- Provide time for people who haven't spoken to speak/ask questions
- Provide time for experts to share wisdom and discuss
- Work together to make discussions accessible to novices

<small>
(These will always be a work in progress and will be updated, clarified, or expanded as needed.)
</small>


## Future Sessions

- Suggest topics or contribute to content in #sciware Slack
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)


## Today's Agenda

- What is reproducibility and why should you care?
- Big picture questions to consider
- Steps towards reproducibility



## What is reproduciblity?

![](assets/reproducibility.png)

#note: before we get started, let's define our terms. I'm using the definitions from the Turing Way, which locates reproducible research here: can I run the same analysis on the same data and get the same output? these other quadrants are also really important for good science, but beyond the scope of this talk.

of these quadrants, reproducible should be the easiest. but that doesn't mean it's *easy*


## Why be reproducible at all?

#note: why should you do this at all? this any of these steps requires extra time, which is time that you're not spending working on your next brilliant idea. If you look around online, people make a lot of different arguments for this, but for me I think there are two main reasons, one practical and one normative.


## The number one person you're helping is future you

![](assets/future-you.png)

#note: at some point, you will return to your code. maybe you submitted the paper and now have to revise it. maybe someone reaches out to you with a question about your paper, or because they want to follow up. maybe someone in your lab wants to use your data or analysis for a new project. maybe this work will be the beginning of a new research line. assuming you think your work has some value, it is unlikely that you're done with it when you submit a paper about it; or, more accurately, that you can accurately predict when you're done with it.

the way I've heard this described is "your most important collaborator is yourself, six months from now, or five years from now". try not to make your life harder.


## Science requires transparency

![](assets/communist.svg)

#note: secondly, more normatively, doing science means being transparent. this is a paper from some philosophers of science, addressing what's known as the "demarcation problem": how do you determine whether something counts as science? their answer is that what really distinguishes science from other forms of inquiry is that scientists must share their work widely for public scrutiny and evaluation. you cannot just say "trust me", you have to explain why.


## But I've already written the paper!

![](assets/abstrusegoose.png)

#note: but you might say, I've already published the paper, surely if anyone has any questions about my analysis, they can just read my beautifully-written  and completely clear paper


## Papers are insufficient

![](assets/overlyhonestmethods.svg)

#note: papers are insufficient for reproducibility. that can be for a lot of reasons. some of those reasons are silly, but some of them are simply that it can be hard to convey all the info required to run an analysis in prose in a way that's not totally mind-numbing. not to mention, there's a lot of implicit knowledge you have, which you might not realize is relevant. and *that* problem is exacerbated by the fact that you're writing for a broad audience: the info a senior professor in your field would need to reproduce your analysis is different than that needed by a junior grad student, and different again than that required by someone outside your field (if you're writing in a journal with a broader audience).


## Points to consider

<div class="fragment appear">
What are your goals? 
</div>
<div class="fragment appear">
Who is the target community?
</div>
<div class="fragment appear">
How much maintenance do you want to do on this?
</div>
<div class="fragment appear">
The earlier you start, the easier this will be.<div class="fragment appear" style="display:inline">.. but it's never too late to start.</div>
</div>
<div class="fragment appear">
Don't let the perfect be the enemy of the good.
</div>

#note: so now you're all thoroughly convinced that you should be reproducible and that to do that, you need to share your code+data. Before we start talking practically, let's set out some questions:
- What your goal is when sharing the code: do you want people to just be able to re-generate your figures? Running same method on newly-collected data / different datasets? Are there any parts of your code (model, algorithm) that folks will want to apply to a completely new context? 
   - Do you see this as a living code base that you’ll continue to update and use for other projects? Or does it serve only to generate results for a single paper?
   - For this talk, we'll assume your goal is just to allow the regeneration of your figures
- Who is the community you are sharing with. Will depend on your publication venue, but how comfortable can you assume they are with programming. If you say “set up a python virtual environment with python 3.10”, will they know how to do that?
- Think about your maintenance burden going forward. You probably don't want to do much maintenance on this.
- In general, all of these will be easier the earlier you start. 
- Don’t let the perfect be the enemy of the good. You don’t have to do all of these on a given project, doing one is better than doing none. Ideally, this is a learning experience, and once you know how to do this on one project, you can easily do it on other projects going forward, so you’re always getting better.


## Caveats

- Largely talking about python.
- I'm mostly familiar with neuroscience and psychology.
- This is heavily opinionated.

#note: finally, some caveats


## Topics

- Get your code running on another machine.
- Tell people how to run your code and what it's doing.
- Data and archiving.
- Automation.
- Advanced topics.

#note: we're going to give a brief overview of a lot today, which fall into these categories. the goal here is to make you aware of all of these topics, and to get you started. the goal is not to be exhaustive, and you'll probably need to do more reading or ask questions about the topics we'll cover today. I'll have some resources at the end of this presentation, which you can find on the sciware site and, if you end up trying to follow these guidelines and have questions or just want to show off, post on the sciware channel!

so our topics are grouped into a couple of higher-level categories: read slide. Edaordo's going to present about the first two of these, which are the meatiest, and then I'm going to come back and finish us up.


## Get your code running on another machine

#note: the absolute minimal requirement for reproducible results is that your analysis code can run on a machine that is not your own. In the next slides I will
provide a few advices that should make this requirement easier.


<ol start="1">
  <li><strong>Choose Your Toolkit Well</strong>
    <ul>
      <li><strong>Focus on Your Scientific Problem</strong>
        <ul>
          <li class="fragment appear">Use "standard" tools to avoid re-implementing common solutions.</li>
          <li class="fragment appear">Example: don't reimplement your own PCA; use libraries like scikit-learn instead.</li>
          <li class="fragment appear">Look for: well-documented, widely used, and actively maintained tools.</li>
        </ul>
      </li>
    </ul>
  </li>
</ol>

#note: First of all, it is important to choose your tools wisely. Your code should focus mainly on your research question, and standard processing steps should be handled by established tools when available. When deciding between tools, what I look for is: well-documented, widely used, and actively maintained.


<ol start="2">
   <li><strong>Open Source First</strong>
      <ul>
         <li>Increases transparency and reproducibility.</li>
         <li class="fragment appear">Open-source tools often have better community support.</li>
      </ul>
   </li>
</ol>
<br>
<ol start="3">
   <div class="fragment appear">
   <li><strong>Avoid GUIs, Prefer Scripting</strong>
      <ul>
         <li class="fragment appear">GUIs limit automation—use scriptable alternatives or obtain a scripted version when possible.</li>
         <li class="fragment appear">When not possible, store both GUI outputs and configurations.</li>
         <li class="fragment appear"><strong>Example:</strong> Finding and merging double-counted units in spike sorting (manual GUI step).</li>
      </ul>
   </li>
   </div>
</ol>

#note: My second recommendation is to prioritize open source tools. This increases transparency and often results in better support from active communities of users and developers.


<ol start="4"> 
   <li><strong>Version Control with Git and GitHub</strong></li>
   <ul>
   <li><strong>Keep a Clean Repository</strong></li>
   <ul>
      <li class="fragment appear">Use `.gitignore` to avoid committing unnecessary files.</li>
      <li class="fragment appear">Have a `README` file explaining repo content, as well as references to associated paper.</li>
      <li class="fragment appear">Minimize the amount of files (especially large binaries).</li>
      <li class="fragment appear">Avoid credential and private data.</li>
      <li class="fragment appear">Delete stale branches.</li>
   </ul>
   </ul>
</ol>


<ol start="5"> 
<li><strong>License Your Code</strong></li>
<ul>
   <li><strong>Clarify Usage Rights</strong></li>
   <ul>
      <li>Add a license (e.g., MIT, Apache 2.0) to define how others can use your code.</li>
   </ul>
</ul>
<li><strong>Avoid Hard-Coded Paths</strong> </li>
<ul>
   <li>Use <strong>config files</strong> (or <strong>environment variables</strong>, harder for users).</li>
</ul>
</ol>


<ol start="5">
<li><strong>Make Your Package Installable</strong></li>
   <ul>
      <li>Specify Core Dependencies in a <code>requirements.txt</code> file.
      <ul>
         <li>List only direct dependencies.</li>
         <li>Avoid pinning package versions if possible.</li>
         <li>Store your package version as a reference, using <code>pip freeze > myenv.txt</code> for Python.</li>
         <li>See <a href="https://sciware.flatironinstitute.org/34_PyPackaging/slides.html">September Sciware on Packaging</a>.</li>
         <li>Check what is imported:</li>
      </ul>
   </ul>
</ol>

<pre style="position: relative; left: -20px; margin: 0; padding: 0; text-align: left;">
   <code class="language-sh">
find path/to/dir/ -type f -name '*py' -exec grep --no-filename -e '^from' -e '^import' {} \+ | sort -u
   </code>
</pre>


<ol start="6">
  <li><strong>Consider Containers</strong></li>
  <ul>
    <li><strong>When Using Containers</strong>
      <ul>
        <li>If your code has <strong>complex dependencies</strong> or non-Python packages.</li>
        <li>If you have code that must run on High-Performance Computing clusters (facilitates portability).</li>
      </ul>
    </li>
    <li><strong>When Probably Not</strong>
      <ul>
        <li>If you use <strong>stable Python packages</strong> with good backward compatibility.</li>
        <li><strong>Conda environments</strong> might be enough if dependencies are Python-only.</li>
      </ul>
    </li>
    <li><strong>Reproducibility Benefits</strong>
      <ul>
        <li>Containers ensure <strong>bitwise reproducibility</strong></li>
        <li>Hash the image.</li>
      </ul>
    </li>
  </ul>
</ol>


## Necessary Information

Have a `README` file which answers:

- What does my code do? 
- How to install my code?
- How to run my code?
- How to cite?


## What does my code do?

- Broief overview of what problem my code solves.
- Key information: programming language, core dependencies (JAX, scipy...).
- Link to related papers, presentations, or documentation.


## How to install my code?

- Step-by-step install procedure.
- Specify python vesions and non-python dependencies.
- Mention OS compatibility.


## How to run my code?

- Code snippets with examples of usage.
- Add decriptive text and comments.
- Point to extended notebook/script tutorials, summarizing the content.
- Notebooks should show example usages, not full analysis.


## How to run my code?

Different ways of adding citations:
- Bibtex entry in `README`
- Citation file in the repo as `CITATION.cff` (Citation File Format) or `CITATION.md` file/
- Consider generating a DOI via Zenodo.


## Survey
Please give us some feedback!
