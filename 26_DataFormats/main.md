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

### Jeff Soules (CCM)


## Outline

- Review definitions
- Consider a few ways to characterize data
- Discuss what we want files to support
- Look at some high-level choices about how to structure files

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
  - with a *finite* series of *bits*
  - on some *persistent* electronic storage
  - *separate* from other data


### Where is data when it's not in files?

In memory!

- The same representation trade-offs apply here too
- Files have an additional task: getting the right data in & out of memory


### What's metadata?

- "Data that describes data"
- Says how to interpret a representation/file
  - Often separate from the file itself
- Expresses assumptions made about the data


## Ways to characterize data

- Different data lends itself to different formats
- Let's think about properties of data and how they can influence choices


### Example Data Sets

- A novel
- A particle simulation
- An electronic medical record


- _War and Peace_ (the novel)
  - Text (in Russian? in English?)
    - Broken into paragraphs? Pages? Chapters?
  - Author, maybe a translator
  - Publisher, publication year


- Particle Position simulation
  - Observations measured over some (consistently spaced?) time unit
  - x, y, z coordinates of a set of particles
    - (What origin? What axes?)
  - velocity, momenta, etc for particles


- Electronic Medical Record
  - Patient biographic/demographic data
  - Natural-language notes from medical providers
  - Quantitative vital signs (every 5 minutes)
  - Medication notes (as administered)


### Data can be more or less strongly typed

- Characters & text
  - (But different encodings?)
- Numbers
  - Integers, reals?
  - What precision, what encoding method?
- Categorical
  - Are all the categories known in advance?


### Data can be free-form or structured

- Q: Does the data have different **fields** ("columns")?
- Q: Does each field have a clear type?
- Less structured: everything is one column
  - Book contents, transcribed speech
- More structured: distinct parts or columns
  - Table of particle positions


### Data can be regular or irregular

- Is the data made of repeated **records** ("rows")?
- Does each record have the same size, or set of values?
- Less regular: variable number of values in some fields
- More regular: rows are always distinct


### Data can be complete or incomplete

- Are there records that are missing fields?
  - Because there was no value?
  - or because we don't know what it was?
- Do we know all the fields when we start collecting the data?
  - Will we want to add more fields partway through?


## What can an ideal file format do?

- We're Flatiron: today We focus on efficiency and clarity
- There are plenty of other desirable properties
  - Access control
  - Resilience
  - Verifiability
- These are out of scope for today


### An ideal format could let us....

- Read files fast
  - Sequentially (from start to finish)
  - Or skipping around (random access)
- Write files fast
- Use minimal disk space
- Open files on any machine
- Read files without special tools
- Understand the file contents without outside knowledge


You can't have all of those things at once!


In general:

- Smaller files are faster to read than larger ones
  - compression makes things complicated
- Transparency/self-documentation leads to added size
- Reading speeds compete with writing speeds

It's easy to come up with exceptions!


## Trade-offs in file format design

(Remember, much of this applies to all data representations!)


### General-purpose vs Specific

- Some file formats can support arbitrary data
- Others are specific to one type of data/record
- The more general the format, the more explanation you need for any particular data set
- The more specific the format, the more outside documentation you need


### Portable vs Machine-Dependent

- Writing memory to disk is "easy"
  - ...but it won't make sense to anyone later
- Portability requires encoding data
  - That often means more space
  - Or more documentation of encodings
- Fortunately we have standards for this
  - If you find yourself writing your own standard...
  - Maybe have a snack and reconsider


### Transparent vs Opaque

- It's easy to inspect formats that can be opened with text editors
  - But character encodings have an overhead
  - "AGAGCT" could be 6 characters (48 to 192 bits)
  - Or it could be 12 bits if we know there's only 4 possible letters
- Some formats label fields internally (JSON, CSV)
  - Pro: the file is self-documenting
  - Con: the file can be much larger


### Regular vs Irregular

- Random access to records depends on regular sizing
  - Easy to find the 1001st character
  - Hard to find the 1001st word
- But sparse data may not be worth storing in regular-sized chunks
  - A 30 GB tensor that's 98% zeroes is probably not ideal for anything


### Support for missing values

- Think back to complete vs. incomplete data
- Some representations imply that missing data is a negative observation
  - Edge list vs. adjacency matrix
  - If you add a field to a CSV, you need to populate it for all records
- It's possible to support data sets whose fields aren't all known in advance
  - but it costs you in efficiency and clarity


### Transposed/Deconstructed Data Layouts

- "Natural" option: each record has one value for each of the fields
- "Transposed" option: each field is a separate set of indexed records

[DROP IN: Two spreadsheet snippets illustrating this]

- Multi-way trade-off among:
  - write speed
  - random-access read speed
  - sequential read speed
  - internal consistency


## Rubric

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
