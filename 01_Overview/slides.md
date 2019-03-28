# Sciware Overview

Activities facilitating scientific software development skills at the Flatiron Institute


# Goals for Today 

- Describe vision for Sciware activity
- Motivate and provide an overview of the topics we plan to discuss 
- Hear multiple perspectives



# Vision

1. Increase awareness and adoption of software development best practices to improve scientific productivity and quality.
2. A positive and inclusive learning environment for all experience levels.
3. A blend of lecture, activities, and discussion to facilitate equal involvement across experience levels.


# Vision

<ol start='4'>
    <li>Topics general enough to be relevant to anyone doing scientific research.</li>
    - For example, technology and coding language agnostic
<li>To use the Flatiron Institute as a sandbox for development of something useful for all of science.</li>
</li>


## Meetings and Format

- Blend of presentations and intro followed by hands-on activities
- 1x/month for 2 hours
- Location TBD

### Next dates: Apr 25, May 23

#### [github.com/flatironinstitute/learn-sciware-dev](https://github.com/flatironinstitute/learn-sciware-dev)
#### [#sciware on simonsfoundation.slack.com](https://simonsfoundation.slack.com/messages/CDU1EE9V5/)



## Rules of Engagement

### Goal: 

Participants all working to actively foster an environment which encourages participation across experience levels, coding language fluency, technology choices, and scientific disciplines.


## Rules of Engagement

- Avoid discussions between a few people on a narrow topic
- Provide time for people who haven't spoken to speak/ask questions
- Find ways to be sure everybody is following and that folks aren't lost
- Make it engaging enough for experts to attend
- Make it accessible enough for novices to attend

(These will always be a work in progress and will be updated, clarified, or expanded as needed.)



## Software Engineering (SCC)

### What is it (and why should you care)?

- Not how to write code (software development), but
- How to turn code into a product (process)
- "...*systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software*" (IEEE)
- "...*sound engineering principles to <b>economically</b> obtain software that is reliable and works efficiently on real machines*" (Fritz Bauer, 1972)


### Software development at scale

- groups of developers and non-developers working together
- requirements, agile, scrum
- waterfall, release schedules
- QA, support, product management
- coordination between individuals with different skill sets and levels


### <strike>Software development at scale</strike>
### Economic, sustainable development


### Efficient, maintainable development

#### Produce working code more quickly

- Tools to write code faster
- Tools to find bugs sooner
- Shorten the iteration/feedback cycle


#### Communicating with and protecting (against) your future self

- Invest in file structure, function naming
- Comment for your (future) self
- Write tests to prevent later changes from breaking older parts ("regression" tests)


#### Do more science, faster

- Productive languages and tools mean less time coding
- Reusable components mean less code to maintain
- A few minutes of optimization can save days of run time
- Good resources (people, documentation) mean less time figuring it out yourself



## Katharine Hyatt (CCQ)
### Testing and why open source


## Open Source Mindset
  - People from other fields can ask deceptively simple questions
  - Passive way to solicit feedback and code improvements, verify correctness
  - Advertise your work and techniques to more people
  - Open source is democratizing
  - Openness is a fundamental value of science
  - Don’t have to reinvent the wheel


## FLOSS in Action
  - “I have no idea why, but suddenly radio astronomers are interested in fixing bugs in my package?”
  - “I just wanted to learn how debuggers work, and then I ended up writing big parts of the Julia compiler and garbage collector…”
  - Physics, math, and CS people spontaneously collaborating to create a huge ecosystem of ODE/PDE solving tools


## Testing
  - Force ourselves to ask: what does this code actually do?
  - Often writing tests spurs rewrites which make code clearer and more robust
  - Easier to catch problems early and know immediately if a change broke something
  - Good way to onboard new contributors



## Joakim Anden (CCM)
### Readable code and version control


## Why readable code?

"*Programs must be written for people to read, and only incidentally for machines to execute.*" (Abelson and Sussman, 1985)


## Find closest prime?

```js
n=>(g=(o,d=N=n+o)=>N%--d?g(o,d):d-1?g(o<0?-o:~o):N)
```
— Arnauld, Code Golf Stack Exchange


## ???

```matlab
%Coeff = [sPCA_data.Coeff, conj(sPCA_data.Coeff)]; % John April 2016
Coeff = sPCA_data.Coeff;
Freqs = sPCA_data.Freqs;
eigval = sPCA_data.eigval;
clear sPCA_data;
%rad_Freqs = sPCA_data.rad_Freqs;
n_im = size(Coeff, 2);
%n_im = (size(Coeff, 2))/2; % John April 21, 2017
%normalize the coefficients
Coeff(Freqs==0, :) = Coeff(Freqs==0, :)/sqrt(2);
for i=1:n_im  %% John April 21, 2017 %% No need to double the coefficients
    Coeff(:, i) = Coeff(:, i) / norm(Coeff(:, i));
end
Coeff(Freqs==0, :)=Coeff(Freqs==0, :)*sqrt(2);
%Compute bispectrum
%[ Coeff_b, toc_bispec ] = Bispec_2Drot_large( Coeff, Freqs ); %If the number of images and number of Coefficients are large use Bispec_2Drot_large
%[ Coeff_b,  toc_bispec ] = Bispec_2Drot_1( Coeff, Freqs );
%[ Coeff_b, Coeff_b_r, toc_bispec ] = Bispec_2Drot_large_v2( Coeff, Freqs );
[ Coeff_b, Coeff_b_r, toc_bispec ] = Bispec_2Drot_large( Coeff, Freqs, eigval );

```


## Who's reading the code when?

- Yourself, collaborators, other researchers?
- Lifetime: 1 day, 1 week, 1 month, 1 year, ...?


## "Code smell"

- Duplicated code
- Variable names: too short, too long, not meaningful
- Functions: too long, too many arguments, no well-defined purpose
- Comments: redundant, not present, outdated


## Cognitive load

How much time do you need to spend to understand what the code does?


## Why version control?

<img src='https://imgs.xkcd.com/comics/git_2x.png' height='580'>  
([xkcd #1597](https://xkcd.com/1597))


## Not just

- A version archiver (use `cp`)
- A synchronizer (use `rsync`)
- A new, exciting way to make you and your colleagues miserable

## But

- A tool for code collaboration through story-telling


## Metadata

- Change (what?)
- Author (who?)
- Message (why?)


## Questions answered

- Why was this line of code changed?
- What was there before?
- When was this bug introduced?
- What changed in this file between v0.1 and v0.2?
- Who has been contributing to this function?


## Usage

- Benefit doesn't come from tool, but how you use it

<img src='https://imgs.xkcd.com/comics/git_commit_2x.png' height='500'>  
([xkcd #1296](https://xkcd.com/1296))



## Olivier Parcollet (as Miles Stoudenmire) (CCQ)
### Performant/efficient code



## What's next? 
What topics we want to cover in next two meetings?

### Apr 25

### May 23
