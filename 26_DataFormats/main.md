# Sciware

## File Formats and Storing Data

https://sciware.flatironinstitute.org/26_DataFormats

https://github.com/flatironinstitute/sciware/tree/main/26_DataFormats


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

- Dedicated Zoom moderator to field questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)


## Future Sessions

- Suggest topics or contribute to content in #sciware Slack


## Today's Agenda

- Intro to _data_ and _files_
- Basic overview of common file formats and their strengths/weaknesses
- Moderately in-depth overview of the hdf5 file format and how to interact with hdf5 data in python (touching on other languages)



# Background/motivation

Jeff Soules (CCM)



# Common "human readable" formats

Robert Blackwell (SCC)


## What do I mean by "human readable"

- Text only -- a human can read it
- ...That's about it


## Some generalities: the "pros"

- Self-documenting
- Typically easy to read
- Portable
- Generally flexible/extendable


## Simplest human readable format: one number

```bash
% cat Energy_K=1.0_Beta=2.5_Gamma=193.2
3.953190
```

* Pls don't


## JSON

* Flexible
* Arbitrary structures
* Verbose (introduce transposed formats)
* No comments! (I assure you this is terrible)


## CSV

* Fixed table
* Flexible types
* Comments
* Very portable


## "TXT" et al.

* Suited for documentation and logging
* Since no standard format, hard to parse otherwise


## Some generalities: the "cons"

* Size: Typically 2-??X larger than binary
    * CSV: ~2x for floats
    * JSON: minified ~2x, formatted ~10x (+?!)
* Performance: Typically orders of magnitude slower than binary
* Only sequential access -- No random access (in most cases)



# Common binary formats

Lehman Garrison (SCC)
