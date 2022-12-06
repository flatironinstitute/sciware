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



# General Concepts

### Jeff Soules (CCM)


## Outline

- Review definitions
- Consider a few ways to characterize data
- Discuss what we want files to support
- Look at some high-level patterns among formats

Today is about the **trade-offs** imposed by different formats,
and making **choices** that fit our situation and goals.


### What is data?

- Input to or output from a computational process
- Information we care about, such as:
  - A table of values
  - Some natural-language text
  - Edge weights on a graph
  - ...


### What is a file?

- A discrete entity on a filesystem
- A *representation* of some data
  - using a *finite* series of *bits*
  - on some *persistent* electronic storage
  - *separate* from other data
- Organizing separate files is its own expensive task


### Where is data when it's not in files?

In memory!

- The same representation trade-offs apply here too
- Files have an additional task: getting the right data in & out of memory


### What's metadata?

- "Data that describes data"
- Says how to interpret a representation/file
  - Often separate from the file itself
  - Might not even be explicitly stated
- Expresses assumptions made about the data


## Ways to characterize data

- Different data lends itself to different formats
- Let's look at some example data sets
  - A novel
  - A particle simulation
  - An electronic medical record
- What data do they each have?


### Novel (_War and Peace_)

- Text
  - In Russian? In English?
  - Broken into paragraphs? Pages? Chapters?
- Author, maybe a translator?
- Publisher, publication year?
- Edition, printing, etc?


### Particle Position Simulation

- States grouped by (consistently spaced?) time unit
- For each particle:
  - x, y, z position coordinates
    - (What origin? What axes?)
  - and velocity, momentum, etc. in coordinates
- Is the number of particles fixed?
- Simulation parameters??


### Electronic Medical Record

- Patient biographic/demographic data
- Natural-language notes from medical providers
- Quantitative vital signs
  - Measured every 5 minutes?
- Medication notes
  - Dosing units?
  - Time--whenever administered?


### Horizontal structure: Fields

- Does the data have different **fields** ("columns")?
  - Is the data composed of distinct parts?
  - Does each field have a clear type?
- Novel: text is pretty much one column
- Particle simulation: each property is its own field


### Vertical structure: Records

- Is the data made of repeated **records** ("rows")?
  - Does each record have the same set of fields?
  - Does each record have 0, 1, or many values per field?
- Particle simulation: one value per record per field
- EMR: ?
  - Vital signs recorded every 5 minutes
  - Provider notes, not so much
  - Medication doesn't follow the vital sign clock-tick


### Fields can be more or less strongly typed

- Characters & text
  - Can come in different encodings
  - How many characters per field?
- Numbers
  - Integers, reals? Units?
  - Positives, negatives?
  - What precision, what encoding method?
- Categorical
  - Are all the values in the category known in advance?


### Data can be complete or incomplete

- Are there records that are missing some fields?
  - Because there was no value?
  - Because we don't know what the value was?
- Do we know all the fields when we start collecting the data?
  - Will we want to add more fields partway through?


## The Ideal File Format

- This is Flatiron: we'll focus on efficiency and clarity
- There are plenty of other desirable properties
  - Access control
  - Resilience
  - Verifiability
- These are out of scope for today


### An ideal format would let us....

- Read files fast
  - Sequentially (from start to finish)
  - Or skipping around (random access)
- Write files fast
- Use minimal disk space
- Open files on any machine
- Read files without special tools
- Understand the file contents without outside knowledge


**You can't have all of those things at once!**


### General Trade-Offs:

**It's easy to come up with exceptions!**

- Smaller files are faster to read than larger ones
  - (...please don't mention file compression)
- Transparency/self-documentation leads to added size
- Reading speeds compete with writing speeds


## Trade-offs in file format design

(Remember, much of this applies to all data representations!)


### General-purpose vs Specific

- Some file formats can support arbitrary data
- Others only store one type of data/record
- Everything needs explanation
  - General formats must put this in the file itself
  - Specific formats (hopefully!) put it in external documentation


### Portable vs Machine-Dependent

- Writing memory to disk is "easy"
  - ...but it won't make sense to anyone later
- Portability requires encoding data
  - That often requires more space
  - and documentation of the encoding system
- Fortunately we have lots of standards
  - If you find yourself writing your own standard...
  - Maybe have a snack and reconsider


### Transparent vs Opaque

- It's convenient to open files with a text editor
  - But character encodings have an overhead
  - "AGAGCT" could be 6 characters (48 to 192 bits)
  - Or 12 bits--there's only 4 possible letters
- Some formats label fields internally (JSON, CSV)
  - Pro: the file is self-documenting
  - Con: the file is (sometimes much) larger


### Regular- vs Irregular-sized Records

- Random access to records depends on regular sizing
  - Easy to find the 1001st character
  - Hard to find the 1001st word
- Sparse data may not be worth storing regularly
  - A 30 GB tensor that's 98% zeroes is probably not ideal


### Support for missing values

- Think back to complete vs. incomplete data
- Some representations imply that missing data is a negative observation
  - Edge list vs. adjacency matrix
  - Need an explicit "unknown" value?
- You can support data whose fields aren't all known upfront
  - but it costs you in efficiency and clarity


### Transposed/Deconstructed Data Layouts

- "Natural": each record has one value for each of the fields
- "Transposed": each field is its own list, indexed by record

[DROP IN: Two spreadsheet snippets illustrating this]

- Multi-way trade-off among:
  - write speed
  - random-access read speed
  - sequential read speed
  - internal consistency


## Rubric

(Yeah, I need to make this an image or something)

| Format | General | Portable | Character vs Binary | Self-documenting | Allows blanks | Flexible Layouts |
| ---    | ------- | -------- |  ------------------ | ---------------- | ------------- |  --------------- |
| ...    |         |          |                     |                  |               |                  |



# Common "human readable" formats

Robert Blackwell (SCC)


## What do I mean by "human readable"

- Text only -- a human can read it
- ...That's about it


## Some generalities: the "pros"

- Self-documenting
- No special tooling required to inspect
- Typically easy to read
- Portable
- Generally flexible/extendable


## Simplest human readable format: one number

```bash
% cat Energy_K=1.0_Beta=2.5_Gamma=193.2
3.953190
```

* EXTREMELY slow/space inefficient
* Difficult to extend
* Blows up very very quickly at scale


## JSON (1)

```json

```


## JSON (2)

* Flexible
* Arbitrary structures
* Verbose (introduce transposed formats)
* No comments! (I assure you this is terrible)


## CSV

```csv
```

* Fixed table
* Flexible types
* Comments
* Very portable


## "TXT" et al.

* Typically suited for documentation and logging - not data
* Since no standard format, hard to parse otherwise


## Some generalities: the "cons"

* Size: Typically 2-??X larger than binary
  * CSV: ~2x for floats
  * JSON: minified ~2x, formatted ~10x (+?!)
* Performance: Typically orders of magnitude slower than binary
* Only sequential access -- No random access (in most cases)



# Common binary formats

Lehman Garrison (SCC)
