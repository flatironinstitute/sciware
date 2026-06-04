# Sciware

## Summer Sciware 1
### Introduction to Scientific Computing at Flatiron

https://sciware.flatironinstitute.org/44_SummerIntro


## Summer Sciware Sessions
- Schedule
  - **June 10**: Summer Sciware 1 - Introduction to Scientific Computing at Flatiron
  - **June 17**: Summer Sciware 2 - Hands-on Computing with the Cluster
  - **July 1**: Summer Sciware 3 -  Making Your Software Project "Just Work"
    - Environment and package management with uv and pixi, the next gen pip and conda replacements
  - **July 8**: Summer Sciware 4 - Developing Software Collaboratively with git and GitHub
  - **July 22**: Summer Sciware open office hour
  - All 10 AM - noon, future sessions in **162 3rd floor classroom**


## Today's Agenda

- Introduction and Goals for Sciware
- VS Code and Claude Code
- AI discussion
- Cluster intro


## Who We Are
- Sciware is a grassroots, scientific software learning community at Flatiron Institute
- We're here to help! Our goals are:
  - to help you setup and learn the computing tools you need to do your summer work, and
  - to help you build fundamental computing skills (terminal, VS Code, git/GitHub, Python project setup, etc).
- These will be useful in any kind of computing career, academic or not!


## Where to get help
- The cluster wiki: https://wiki.flatironinstitute.org/
- The [#sciware](https://simonsfoundation.enterprise.slack.com/archives/CDU1EE9V5) channel on Simons Foundation Slack
- Sciware website: https://sciware.flatironinstitute.org/
- Your mentor!
- SCC: scicomp@flatironinstitute.org or #scicomp Slack channel
- Question: Do you want a intern-only code-help channel??



## Intro to Claude Code

https://sciware.flatironinstitute.org/44_SummerIntro/day1.html


## Agenda

- Some context on Claude
- The Claude CLI and VS Code extension
- Hands-on demos: plan mode, existing repos, models, the shell, memory, more
- Advice for exploring technical topics with Claude
- How to learn more



# Context on Claude


## What is Claude?

- LLM from Anthropic
- Model family: **Opus** (most capable), **Sonnet** (balanced), **Haiku** (fast / cheap)
- "Claude Code" = Anthropic's official CLI for software engineering
    - Can be used as a chat bot or an "agent" able to edit files and even run commands on its own
- The claude.ai website gives you access to a Claude chat bot


## The "December revolution"

- Through mid-2025, agentic coding LLMs were capable but inconsistent
- Opus 4.6 (late 2025) + Claude Code: LLM tool use and reasoning became sophisticated enough to be useful by modern software engineering standards
- This workshop wouldn't have made sense a year ago
- Many people using Opus 4.7 with Claude Code today, although many alternatives/competitors exist (OpenAI's GPT + Codex, Google's Gemini + CLI, etc).



# Two ways to use Claude


## Claude CLI vs. VS Code extension

- **Claude CLI** — runs in your terminal
- **VS Code extension** — runs inside the editor sidebar
- Same Claude underneath; pick whichever matches your workflow
- We'll see both today



# Example: hands-on tour


## Demo 1 — A new Python project from scratch

- Headline idea: **plan mode**
- Ask Claude to design *before* it writes any code
- Review the plan, edit, iterate — then approve
- Files only appear after you exit plan mode


## Demo 2 — Working in an existing repo

- `CLAUDE.md` — project conventions Claude reads on startup
- Reference materials — point Claude at docs, papers, related code
- **Skills** — small reusable instructions Claude can invoke (`/skill-name`)


## A repo friendly to Claude is friendly to humans

- Clear README, runnable examples
- Tests that exercise the real code paths
- Sensible directory structure, good error messages, clear API
- *Free win:* the LLM benefits from the same things a new collaborator does


## Demo 3 — Model, effort, usage

- Choosing **Opus** vs **Sonnet** vs **Haiku** — capability vs. cost / speed
- Effort / thinking knobs — when to let Claude think longer
- `/usage` — see your rate-limit state before you hit a wall mid-task


## Demo 4 — Claude + the shell

- **Bash commands** — Claude runs shell on your behalf; permission prompts; allowlisting
- **tmux** — detachable long-running sessions, multi-pane, survives SSH disconnects
- **`gh` CLI** — open issues / PRs, read CI logs, post review comments — from the terminal


## Demo 5 — Memory and context

- **Memory system** — facts Claude carries across sessions
    - Auto-memory directory; `CLAUDE.md` at user / project scope; `MEMORY.md` index
- **Context management** — `/compact`, `/clear`, auto-summarization
    - Habits to keep long sessions from drowning in context


## `--dangerously-skip-permissions`

- Skips every permission prompt — Claude can do anything in the shell
- The name is intentional!
- Designed for: throwaway VM, sandbox, isolated container without internet access
- Not designed for: shared clusters, your real repos
- Alert fatigue is real. Recommend curating your allowlist rather than skipping prompts.



# Ways to use Claude for research software

<style>
.spectrum-row {
    display: flex;
    align-items: center;
    margin: 60px 0 30px 0;
}
.spectrum-spacer {
    flex: 0 0 16.67%;
}
.spectrum-arrow {
    flex: 0 0 auto;
    width: 0;
    height: 0;
    border-top: 14px solid transparent;
    border-bottom: 14px solid transparent;
}
.spectrum-arrow.left {
    border-right: 20px solid #537eba;
}
.spectrum-arrow.right {
    border-left: 20px solid #537eba;
}
.spectrum-line {
    flex: 1 1 auto;
    height: 6px;
    background: #537eba;
}
.spectrum-dot {
    flex: 0 0 auto;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #537eba;
    box-sizing: border-box;
}
.spectrum-cols {
    display: flex;
    align-items: flex-start;
}
.spectrum-col {
    flex: 1 1 0;
    padding: 0 20px;
}
.spectrum-col h3 {
    text-align: center;
    margin: 0 0 18px 0;
}
.spectrum-col ul {
    display: block;
    text-align: left;
    margin: 0;
    padding-left: 1.2em;
    font-size: 0.85em;
}
.spectrum-col li {
    margin-bottom: 0.4em;
}
</style>

<div class="spectrum-row">
    <div class="spectrum-spacer"></div>
    <span class="spectrum-arrow left"></span>
    <div class="spectrum-line first"></div>
    <span class="spectrum-dot"></span>
    <div class="spectrum-line second"></div>
    <span class="spectrum-arrow right"></span>
    <div class="spectrum-spacer"></div>
</div>

<div class="spectrum-cols">
    <div class="spectrum-col">
        <h3>Fewer tradeoffs</h3>
        <ul>
            <li>LLM as Google or Stack Overflow</li>
            <li>Code review</li>
            <li>Controlled experiments (e.g. perf optimization, simplified mockups)</li>
        </ul>
    </div>
    <div class="spectrum-col">
        <h3>Some tradeoffs</h3>
        <ul>
            <li>Plan mode</li>
            <li>Bug fixing</li>
        </ul>
    </div>
    <div class="spectrum-col">
        <h3>More tradeoffs</h3>
        <ul>
            <li>Hands off, fully agentic, end-to-end execution</li>
        </ul>
    </div>
</div>



# Grounding Claude's Technical Answers

<style>
.rigor-levels {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin: 30px auto 20px auto;
    width: 90%;
}
.rigor-level {
    display: flex;
    align-items: center;
    border: 2px solid #537eba;
    border-radius: 8px;
    padding: 14px 22px;
    text-align: left;
}
.rigor-number {
    flex: 0 0 auto;
    font-size: 2.2em;
    font-weight: bold;
    color: #537eba;
    margin-right: 24px;
    line-height: 1;
}
.rigor-content {
    flex: 1 1 auto;
}
.rigor-content h3 {
    margin: 0 0 6px 0;
    text-align: left;
}
.rigor-content p {
    margin: 0;
    font-size: 0.85em;
    line-height: 1.4;
}
.rigor-tradeoff {
    font-style: italic;
    color: #888;
    text-align: center;
    margin: 24px 0 0 0;
    font-size: 0.9em;
}
</style>

<div class="rigor-levels">
    <div class="rigor-level">
        <div class="rigor-number">1</div>
        <div class="rigor-content">
            <h3>Training data</h3>
            <p>Claude answers from what it learned during pre-training. Fast and zero-setup, but may be outdated or wrong on niche topics.</p>
        </div>
    </div>
    <div class="rigor-level">
        <div class="rigor-number">2</div>
        <div class="rigor-content">
            <h3>Web search</h3>
            <p>Tell Claude to search the web or fetch documentation. Verify it actually did — look for the <code>WebFetch</code> tool in its output.</p>
        </div>
    </div>
    <div class="rigor-level">
        <div class="rigor-number">3</div>
        <div class="rigor-content">
            <h3>Reference the local docs and code</h3>
            <p>Get a copy of the software locally and force Claude to reference the source code and documentation in its answers. Potentially most accurate, but most setup.</p>
        </div>
    </div>
</div>

<p class="rigor-tradeoff">Each successive level: more work and higher token cost, but potentially more accurate answers.</p>
