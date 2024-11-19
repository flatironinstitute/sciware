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

- What are your goals?  <!-- .element: class="fragment"  -->
- Who is the target community?  <!-- .element: class="fragment"  -->
- How much maintenance do you want to do on this?  <!-- .element: class="fragment"  -->
- The earlier you start, the easier this will be.  <!-- .element: class="fragment" -->
- But it's never too late to start. <!-- .element: class="fragment" -->
- Don't let the perfect be the enemy of the good.  <!-- .element: class="fragment"  -->

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

so our topics are grouped into a couple of higher-level categories: read slide. Edaordo's going to present about the first two of these, which are the meatiest, and then I'm going to come back and finish us up. Periodically, we're going to switch tabs to show you how we've implemented these steps in our own projects.



## Get your code running on another machine

#note: the absolute minimal requirement for reproducible results is that your analysis code can run on a machine that is not your own. In the next slides I will
provide a few advices that should make this requirement easier.


### Choose Your Toolkit Well
- **Focus on Your Scientific Problem**
  - Use "standard" tools to avoid re-implementing common solutions.   <!-- .element: class="fragment"  -->
  - Example: don't reimplement your own PCA; use libraries like scikit-learn instead.  <!-- .element: class="fragment"  -->
  - Look for: well-documented, widely used, and actively maintained tools.   <!-- .element: class="fragment"  -->

#note: First of all, it is important to choose your tools wisely. Your code should focus mainly on your research question, and standard processing steps should be handled by established tools when available. When deciding between tools, what I look for is: well-documented, widely used, and actively maintained. In general, try not to depend on other research code, this type of code is not meant for stable distribution. If you depend on research code, expect breaking changes at every release.


### Open Source First
- Increases transparency and reproducibility.  <!-- .element: class="fragment"  -->
- Open-source tools often have better community support.  <!-- .element: class="fragment"  -->

### Avoid GUIs, Prefer Scripting  <!-- .element: class="fragment"  -->
- GUIs limit automation—use scriptable alternatives or obtain a scripted version when possible. <!-- .element: class="fragment"  -->
- When not possible, store both GUI outputs and configurations. <!-- .element: class="fragment"  -->
   - Example: Finding and merging double-counted units in spike sorting (manual GUI step). <!-- .element: class="fragment"  -->

#note: My second recommendation is to prioritize open source tools. This increases transparency and often results in better support from active communities of users and developers.


### Version Control with Git
- **Keep a Clean Repository**
   - <!-- .element: class="fragment" --> Use <code>.gitignore</code> to avoid committing unnecessary files. 
   - <!-- .element: class="fragment" --> Have a <code>README</code> file explaining repo content, as well as references to associated paper. 
   - Minimize the amount of files (especially large binaries).  <!-- .element: class="fragment"  -->
   - Delete stale branches.  <!-- .element: class="fragment"  -->
   - Avoid credential and private data.  <!-- .element: class="fragment"  -->

#note: Next, you should version control you code. You can host your code in a repo, GitHub is the most common, GitLab or bitbucket are other alternatives. Try to keep your repository clean, which include having a gitignore file to minimize the risk  of adding unecssary files; delete inactive branches,do not hardcode credential or personal data.


### License Your Code
- **Clarify Usage Rights**
   - Add a license (e.g., MIT, Apache 2.0) to define how others can use your code.

### Avoid Hard-Coded Paths  <!-- .element: class="fragment" data-fragment-index=1 -->
- <!-- .element: class="fragment" data-fragment-index=1 -->Use <strong>config files</strong> (or <strong>environment variables</strong>, harder for users). 

#note: generally, license your code, this is a way to specify how your work shold be used and distributed.



### Facilitate Installation
- Specify Core Dependencies in a [pyproject.toml](https://github.com/flatironinstitute/sciware/blob/main/34_PyPackaging/example_project_root/pyproject.toml) file.
   - List only direct dependencies. <!-- .element: class="fragment"  -->
   - Avoid pinning package versions if possible. <!-- .element: class="fragment"  -->
   - <!-- .element: class="fragment"  --> Store your package version as a reference, using <code>pip freeze > myenv.txt</code> for Python.
   -  <!-- .element: class="fragment"  --> See <a href="https://sciware.flatironinstitute.org/34_PyPackaging/slides.html">September Sciware on Packaging</a>.

#note: Finally, facilitate installing your code. List your direct dependecies in a requirement file, menaing the things you directly import and use. Do not pin specific python version; for more details on this check Sept sciware on pacakging. You can list your import in various way, here I added a one-linear command for that.


### Containers?
- **When To Use Containers**
   - If your code has **complex dependencies** or non-Python packages.
   - If you have code that must run on High-Performance Computing clusters (facilitates portability).
- **When To Probably Not** <!-- .element: class="fragment" data-fragment-index=1 -->
   -  <!-- .element: class="fragment" data-fragment-index=1 --> If you use <strong>stable Python packages</strong> with good backward compatibility.
   -  <!-- .element: class="fragment" data-fragment-index=2 --> <strong>Conda environments</strong> might be enough if dependencies are Python-only.

#note: You can also consider containers, like Docker or Singularity. Usually convenient when your package as complex dependency, like more than one programming language. Singularity may be a good idea since it makes your environment very easy to port on any 
HPC syste. On the other hand, if your installation is easy enough (pure python, standard packages), conda enviroments may be sufficient.



## Provide Necessary Information

Write a `README` file which answers the following questions:

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
- Notebooks should show example usages, rather than full analysis.


## How to cite?

Different ways of adding citations:

- Bibtex entry in `README`
- Link to a paper. 
- Consider generating a DOI via Zenodo.
- [Example](https://github.com/billbrod/spatial-frequency-preferences/blob/main/README.md)

## What data to share and where?

#note: when thinking about sharing data, start with these questions.


## What to share?

- Raw data <!-- .element: class="fragment" -->
- Processed data <!-- .element: class="fragment"  -->
- Model parameters <!-- .element: class="fragment" -->
- Stand-alone outputs <!-- .element: class="fragment"  -->
- Metadata (e.g., data dictionary)  <!-- .element: class="fragment"  -->

#note: So what do you share? the obvious one is your raw data. If someone is going to run your analysis from scratch, they obviously need your data.

However, there are other things worth sharing that you might not thought of:
- it's probably worth sharing data that has been processed in some way. this is especially useful if part of your pipeline uses non-open source software or takes a long time / lots of computational resources to run. if you have any pre-processing steps, which use standard analyses which you are not responsible for (e.g., you're using some existing package and just applying as is), it can be useful to share the output of all those steps as well. these are typically also a good deal smaller than the raw data, at least in neuroscience. For me, I like to share the output of these pre-processing steps, and then also the inputs to the figure generation. that gives people multiple entry points into the data
- Model parameters. if you fit a model, these are probably useful to people. it's probably a small text file (csv, json) and very important for anyone to use your model, but a pain in the ass to sufficiently include in the paper
- Stand-alone outputs. By this I mean things that might be useful for people beyond just the goal of re-creating your figures. in that case, it's a bit out of the context of this talk, but still worth taking a moment to think about. model parameters (or model code, if new) are one instance of this but, there are others. (model metamer images)
- Metadata. how do you interpret any of this stuff? If you have collaborators, I'm sure you have the experience of getting data from them and having no idea how to move through it. you need to describe it: what does stimulus=0 mean? how do subject codes align with those used in the paper? etc. the generic way of doing this is using something called a data dictionary, which is a csv file describing each field in your dataset, with description (including units), and possible values

- [data dictionary](https://help.osf.io/article/217-how-to-make-a-data-dictionary)


## Use data standards

![](assets/data_standards.svg) <!-- .element: class="plain" -->

#note: it might strike you that writing up all the metadata is a lot of work. yep! that's why, if your field has a data standard, you should use it. in neuroscience, there's BIDS (brain imaging data structure) for neuroimaging, and NWB (neurodata without borders) for physiology.

The point of a data standard is to handle all of that metadata for you: you'll have to go through some effort to get your data into that standard (though this should be at least a lab-wide, if not department-wide effort and only needs to be done once), but this makes it very clear how the information is structured. standard typically also have validation tools, which will automatically ensure everything looks good.

Ideally, getting data into the standard happens as soon as the data is collected, and this should be moved as upstream as possible. as an example, I gathered fMRI data in my phd, and what really led to the fMRI labs at NYU adopting BIDS is that the team that ran the actual fMRI machine made it easy to export the data directly into BIDS: they already had a consistent internal format, and so they were able to put together a little pipeline that converted from that format into BIDS, and offered it to everyone.

advantage beyond reproducibility: tools! for BIDS, there are a lot of tools that will work automatically with BIDS-formatted data, so you get an immediate benefit as an individual researcher.


## Where to share?

- Generally, data does not belong in a git repo.  <!-- .element: class="fragment" -->
  - Exception: small (<1 MB) text files. <!-- .element: class="fragment" -->
- Checklist:  <!-- .element: class="fragment" -->
  - Is it run by a non-profit and open source? 
  - How discoverable is it? How is it indexed?
  - Related to above, what does community use?
  - Gives DOI 
  - Integrations with other services
- Examples:   <!-- .element: class="fragment" -->
  - General: Open Science Framework (OSF), Zenodo
  - Neuroscience-specific: OpenNeuro, DANDI
  - Institutional repositories (e.g., NYU Faculty Data Archive)

#note: generally speaking, data does not belong in a git repo. the only exception is small text files containing model parameters or similar.

therefore, we need to come up with somewhere else to put it. this is a checklist from Vicky Rampin, the reproducibility librarian at NYU. she's excellent, and was a lot of help during my PhD. I recommend anyone at NYU who's looking to share their data/code talk with her.

talk through checklist, show examples. these are all free, and will have different file size / number of file limits. the neuro-specific ones also enforce and check for data standards

in particular, you'll note that dropbox and google drive are not on here. Beyond the points in this checklist (which they fail), they're just not fit-for-purpose: they are not intended to do long-term public archiving (of anything).


## Code archiving

The internet is not forever.

#note: which brings me to my next point: beyond your data, you should also archive your code. nothing is guaranteed to last forever on the internet, and this is especially true of resources owned by private companies like Microsoft.

Fortunately, Zenodo has an easy interface with Github. Once you set up your account, you can set it up to automatically archive your code, giving you a DOI and promising to archive it for a long time. In fact, Zenodo will mint a new DOI whenever you do a release / add a git tag, which leads us to...


## Versioning

Not just for software packages!

#note: while versioning is very useful for software packages, it can also be useful for research code. I've used versions to mark whenever I've reached a milestone. that includes when making a pretty large refactor, but also just to say "this was the code I used for this presentation" or "the preprint", "journal submission", "final accepted version".

This way, it's easy to come back and say "I generated this figure in that presentation I made three years ago, but at some point later I broke the code -- how did I do it?"



## Workflow

How do I convert the data into figures?
- Some notes in your readme  <!-- .element: class="fragment" -->
- A handful of bash scripts <!-- .element: class="fragment" -->
- Snakemake <!-- .element: class="fragment" -->
- Spyglass / DataJoint / BrainLife <!-- .element: class="fragment" -->

#note: when I say workflow, I'm referring to whatever you have that can answer the question of "how do I convert data into figures?"

there are many ways to do this, with varying levels of complexity. it could be as simple as some notes showing the commands you ran, in order or bash scripts doing just that. however, there are also dedicated tools for this, which can be quite helpful, such as snakemake and spyglass / datajoint / brainlife. these second class are "heavier" in that they are primarily cloud services and build docker containers and run everything as well. for me, these have generally seemed like overkill for the kind of small bespoke research projects that I have done (balance shifts if you have a super standard pipeline that is used for every dataset)

for me, snakemake is ideal. it can be run locally, makes naive parallelization easy , can be configured to work with cluster or commercial cloud systems, and is fairly flexible.

Snakemake comes from the bioinformatics community and is inspired by GNU make, which, if you're like me, you've only interacted with by calling `make install`.



## Snakemake

```python
rule bwa_map:
    input:
        "data/genome.fa",
        "data/samples/A.fastq"
    output:
        "mapped_reads/A.bam"
    shell:
        "bwa mem {input} | samtools view -Sb - > {output}"
```

#note: snakemake defines rules in a Snakefile, which all look something like this: they define some number of inputs, outputs, and what needs to be done to get from in to out. this is from their official tutorial and not my area, but here we have some arbitrary shell code that converts the input to the output. this can be shell, as here, but can also be arbitrary python or a script.

if this is the contents of your file, you can run `snakemake mapped_reads/A.bam`, and snakemake goes through the rules, finds how to produce the file you requested, and calls the shell code.


## Wildcards

```python
rule bwa_map:
    input:
        "data/genome.fa",
        "data/samples/{sample}.fastq"
    output:
        "mapped_reads/{sample}.bam"
    shell:
        "bwa mem {input} | samtools view -Sb - > {output}"
```

#note: snakemake supports wildcards, so if we have many different files that are all created with the same basic command, we don't need to write separate rules for `mapped_reads/B.bam`, etc. we just use the curly brace syntax to denote a wildcard. now running `snakemake mapped_reads/A.bam` or `snakemake mapped_reads/B.bam` will both produce the appropriate output.



## Tests and Continuous Integration

#note: And now to talk about something that initially sounds like it's too complex: tests and CI. Since you're writing research code, you don't need to fully test your code in the way you would if you were writing a research package. however, Github actions is available for free on any public repo and is quite easy to set up.

this can allow you to check: did I actually define my installation correctly? can write a small test to install your dependencies and run a quick test: can I import my code and run a simple test (e.g., initialize my model, load a subset of my data). if you're using snakemake, you could write a small rule (or some number of rules) that serves as your "installation check", which will import your code and do similar. this way, you can have that check running in your CI and your readme can tell people "run this command, if it passes, then your installation is working".

this can also help you keep track of dependencies changing under you. if you followed our advice from before, your version limits are minimal, but running this CI regularly will let you know if a version of e.g., pytorch, gets released that you're not compatible with.

this will give you some maintenance load, which is why it's not obvious that it's necessary; you're committing to looking at this if it fails at some point. but the goal being that you do ~10 minutes / month, rather than coming back in a year and having to spend much longer.


## CI to build a paper

#note: there's a different use case for CI, which has always struck me as cool, but impractical: build your entire paper with CI. this requires that your analysis's compute requirements be relatively small, so that you can run it on the free resources in a relatively short amount of time -- that's never happened to me, but would be very cool.



## Code style and readability


#note: finally, some closing thoughts. we've spent this entire time talking about how to share your code without actually describing anything about what your code looks like. that's intentional -- ideally, people will be able to do the above without looking at your source code.

but, at some point, if someone is interested enough, they'll want to look at your code. in order to make their life easier, try to write readable code. Sciware and CCM member Jeff Soules gave a great talk at FWAM about how to write code for humans, the slides of which canb e found (__). 

additionally, most programming languages have some sort of linters / formatters, such as ruff for python, which will help keep your code to some defined standards. this will help your code match your readers' expectation, reducing the cognitive load. not necessary, but can be nice.


## Resources

- https://blog.nicholdav.info/four-tips-structuring-research-python/
- https://help.osf.io/article/217-how-to-make-a-data-dictionary
- https://goodresearch.dev/
- https://book.the-turing-way.org/index.html
- https://guides.nyu.edu/software-reproducibility/home 


## Survey
Please give us some feedback!
