# Sciware

## Blender
## Intro to 3D Scientific Visualization

https://github.com/flatironinstitute/sciware/tree/main/18_Blender


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


## Zoom Specific

- If comfortable, please keep video on so we can all see each other's faces.
- OK to break in for quick, clarifying questions.
- Use Raise Hand feature for new topics or for more in-depth questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted on #sciware Slack.
- Please keep questions for the speaker in the Zoom chat.


## Future Sessions

- Nov 4: Flatiron Clusters (rescheduled)
- Suggest topics and vote on options in #sciware Slack


## Today's agenda

- Demo 1: Catalog rendering
- Offline cluster rendering
- Questions / Break
- Demo 2: Datacube rendering
- Reception (roof)



# Demo 1 - Catalog

https://github.com/brkent/flatiron-sciware-blender-2021



# Offline Cluster Rendering

How to submit a render job to a V100 queue and render a .blend file on 4 gpus simultaneously:

1. Blender support rendering in headless mode, which means we can launch a blender instance for rendering. https://docs.blender.org/manual/en/latest/advanced/command_line/render.html
2. To use multiple gpus at once, we can either use them all in one blender instance or launch multiple blender instance to render different frames in the scene. From what I have seen on the internet, it seems launching multiple instances is more efficient in rendering.
3. Attached are two scripts I used to launch 4 stances on a V100 node with 4 GPUs. blender_preference.py is not directly executed, but used in blender for it to figure out which gpu to use in a particular instance. run_batch_blender.py uses subprocess in python to launch 4 blender instances to render different frames.

After setting the environment up, one can execute run_batch_blender.py to start the rendering. Let me know if there is anything unclear. I imagine this may be useful if more people want to try blender after the coming up blender tutorial.



# Questions

If you have a Blender question/topic you'd like to discuss in a future session, please add it to [this Google list](https://docs.google.com/spreadsheets/d/1m-WAz8p3UzOVs4fYggYqjRviC4CgVsWXiiRntRt2na8/edit?usp=sharing).


## Break
<img height=65% width=65% src="./assets/gifs/pikachu.gif">


# Demo 2 - Datacube

https://github.com/brkent/flatiron-sciware-blender-2021



# Survey

https://bit.ly/fi-clusters