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
- We're recruiting: looking for CCB representative, contributors


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



# Binary File Formats

Lehman Garrison (SCC)


## What do we mean by "binary file"?

* Not human readable (usually)
* Low-level, often mostly a "raw memory dump"
  * The data is stored identically on disk as it is in memory
  * No expensive translation step, like with CSV to binary
  * Or if there is a translation step (c.f. compression), it's very efficient
  * Binary formats are almost always the right way to store large amounts of data!


## What do binary files look like?

```python
>>> a = np.arange(10**7, dtype='f4')
>>> a.tofile('mybinfile')
```

```
$ head -c 128 mybinfile
�?@@@�@�@�@�@AA A0A@APA`ApA�A�A�A�A�A�A�A�A�A�A�A�A�A�A�A�A
```

* It's gobbledygook, as expected
* What would we do if we wanted it to be human readable?


## What do binary files look like? (cont.)

* Could make a human readable file with:

```python
>>> np.savetxt('mytxtfile', a)
```

```
$ head -n8 mytxtfile
0.000000000000000000e+00
1.000000000000000000e+00
2.000000000000000000e+00
3.000000000000000000e+00
4.000000000000000000e+00
5.000000000000000000e+00
6.000000000000000000e+00
7.000000000000000000e+00
```


## Why not always do human readable?

* It's so much slower to save, so much slower to load, and so much bigger to store!

```python
>>> %timeit np.savetxt("mytxtfile", a)
14.5 s ± 141 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

>>> %timeit a.tofile("mybinfile")
19.1 ms ± 196 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

```
$ ls -lh
-rw-rw-r-- 1 lgarrison lgarrison  39M Dec  8 12:09 mybinfile
-rw-rw-r-- 1 lgarrison lgarrison 239M Dec  8 12:09 mytxtfile
```


## So we should always do `np.tofile()`?

* Don't always do `np.tofile()`!
  * or similar raw binary dumps
  * Doesn't store metadata
  * Not self-describing—how will a user know how to read? Does this file contain floats or ints? 4-byte or 8-byte? Etc.

```python
>>> np.fromfile("mybinfile")
array([7.81250000e-03, 3.20000076e+01, 2.04800049e+03, ...,
       5.88761292e+53, 5.88762023e+53, 5.88762753e+53])
```

That's garbage! Have to remember to do:

```python
>>> np.fromfile("mybinfile", dtype='f4')
array([0.000000e+00, 1.000000e+00, 2.000000e+00, ..., 9.999997e+06,
       9.999998e+06, 9.999999e+06], dtype=float32)
```


## Better Binary Formats

* Better formats exist that solve these problems
  * Self-describing (e.g. knows its own `dtype`), stores metadata
  * Retain the performance and size benefits of raw binary
* Examples
  * .npy/.npz files (Numpy specific)
  * Msgpack ("binary JSON": arbitrarily structured binary data, not just arrays)
  * ASDF (human-readable header, binary data blocks, best of both worlds)
  * HDF5 (wide adoption, feature-rich, often the Right Choice)
  * See table at the end of this section


## ASDF File Format

* Most binary formats are _all_ binary—no way to know what's inside with installing special tools (e.g. `h5ls`)
* Doesn't have to be that way, we can have a human-readable header while still storing the data in binary blocks for efficiency
* That's what ASDF is!
  * ASDF = Advanced Scientific Data Format
  * "A next-generation interchange format for scientific data"
* https://github.com/asdf-format/asdf


## ASDF Example

```python
import asdf
import numpy as np

seed = 123
rng = np.random.default_rng(seed)
sequence = np.arange(10**6, dtype='f4')
rand = rng.random((512,512))
tree = {'seq': sequence,
        'rand': rand,
        'params':
            {'comment': 'This is an example for Sciware',
             'seed': seed,
            },
       }

af = asdf.AsdfFile(tree)
af.write_to('/tmp/myfile.asdf')
```


## ASDF Example

```yaml
#ASDF 1.0.0
#ASDF_STANDARD 1.5.0
%YAML 1.1
%TAG ! tag:stsci.edu:asdf/
--- !core/asdf-1.1.0
asdf_library: !core/software-1.0.0 {author: The ASDF Developers, homepage: 'http://github.com/asdf-format/asdf',
  name: asdf, version: 2.13.0}
history:
  extensions:
  - !core/extension_metadata-1.0.0
    extension_class: asdf.extension.BuiltinExtension
    software: !core/software-1.0.0 {name: asdf, version: 2.13.0}
params: {comment: This is an example for Sciware, seed: 123}
rand: !core/ndarray-1.0.0
  source: 1
  datatype: float64
  byteorder: little
  shape: [512, 512]
seq: !core/ndarray-1.0.0
  source: 0
  datatype: float32
  byteorder: little
  shape: [1000000]
...
<D3>BLK^@0^@^@^@^@^@^@^@^@^@^@^@^@^@=   ^@^@^@^@^@^@=   ^@^@^@^@^@^@=   ^@<B7>_<98><E3>^B<87><A5><FE>^M
^M<BF><A7>^H*<B0><91>*^@^@^@^@^@^@<80>?^@^@^@@^@^@@@^@^@<80>@^@^@<A0>@^@^@<C0>@^@^@<E0>@^@^@^@A^@^@^PA^@
```


## ASDF Inline Array Example

```python
import asdf

sequence = list(range(12))
squares = {k:k**2 for k in range(10,20)}
tree = { 'seq': sequence, 'squares': squares}

af = asdf.AsdfFile(tree)
af.write_to('/tmp/myfile.asdf')
```


## ASDF Inline Array Example

```yaml
#ASDF 1.0.0
#ASDF_STANDARD 1.5.0
%YAML 1.1
%TAG ! tag:stsci.edu:asdf/
--- !core/asdf-1.1.0
asdf_library: !core/software-1.0.0 {author: The ASDF Developers, homepage: 'http://github.com/asdf-format/asdf',
  name: asdf, version: 2.13.0}
history:
  extensions:
  - !core/extension_metadata-1.0.0
    extension_class: asdf.extension.BuiltinExtension
    software: !core/software-1.0.0 {name: asdf, version: 2.13.0}
seq: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
squares: {10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289,
  18: 324, 19: 361}
```


## ASDF Details
- Development led by astronomy community (STScI) as a FITS replacement
- [Greenfield, et al. (2015)](https://www.sciencedirect.com/science/article/pii/S2213133715000645) lays out motivation: want human-readable headers; avoid complexity of HDF5 (is it really archival?); HDF5 doesn't represent certain data structures (e.g. Python dict) well
- The reference implementation is in Python. Excellent integration with Numpy. C++ interface less mature.
- Lehman prefers to use ASDF over HDF5 when it makes sense
  - End-users are using Python and are okay with non-HDF5


## Summary of Binary Formats

- Binary formats store data in a low-level way, often as a direct copy of the data in memory
- Nearly always the right choice when size or performance is a consideration
- Downsides: the format you choose locks you (and your users) into that format's tooling ecosystem
  - HDF5 files have to be read with an HDF5 library, npy files have to be read with numpy, etc.
  - Usually can't open a file and know what's inside without that format's tools (but see ASDF)


## Binary Formats Table

- Which: HDF5, ASDF, Pickle, msgpack, npy
- Columns
  - Self-describing
  - Random access
  - Supports compression
  - Human-readable header
  - Best for (npy: Numpy arrays; msgpack: JSON-like structures; pickle: Python objects, etc)



# HDF5

Dylan Simon (SCC)


## HDF5 concepts

Largely taken from HDFGroup's [Introduction to HDF5](https://docs.hdfgroup.org/hdf5/develop/_intro_h_d_f5.html)

"An HDF5 file can be thought of as a container (or group) that holds a variety of heterogeneous data objects (or datasets). The datasets can be images, tables, graphs, and even documents, such as PDF or Excel"


### HDF5 Groups

- Groups are like directories in a filesystem

<img src="https://docs.hdfgroup.org/hdf5/develop/group.png" width="80%" style="border:0;box-shadow:none">

- UNIX path names are used to reference objects: `/SimOut/Mass`


### HDF5 Datasets

- Datasets store multi-dimensional blocks of data of a single type
- Usually represent a single "column" of data

<img src="https://docs.hdfgroup.org/hdf5/develop/dataset.png" width="80%" style="border:0;box-shadow:none">


### HDF5 Datatypes

- Datatypes are designed to map to in-memory representations
- Predefined datatypes: atomic values
  - `H5T_IEEE_F32LE`, `H5T_NATIVE_FLOAT` (float)
  - `H5T_INTEL_I32`, `H5T_STD_I32LE`, `H5T_NATIVE_INT` (int)
  - `H5T_C_S1` (char, basis for fixed-length strings)
- Derived datatypes: compound values composed of other types
  - fixed-length strings


### HDF5 Compound Datatypes

<img src="https://docs.hdfgroup.org/hdf5/develop/cmpnddtype.png" width="80%" style="border:0;box-shadow:none">

- Compound types can be nested and include fixed-sized arrays


### HDF5 Dataspaces

- Dataspaces represent the size and dimensions of an array (scalar, vector, etc.)
- Can be used to describe overall Dataset size, and subsets ("views", "slices") of data

<img src="https://docs.hdfgroup.org/hdf5/develop/dataspace.png" width="80%" style="border:0;box-shadow:none">


### HDF5 Attributes

- Attributes are metadata attached to an object (usually a Group or Dataset)
- Have names and values
- Values are the same as Dataset values, but are usually small
  - Scalar value of simulation parameter
  - String describing field, units, etc.


### HDF5 Properties

- Properties control how data is stored on disk

<img src="https://docs.hdfgroup.org/hdf5/develop/properties.png" width="80%" style="border:0;box-shadow:none">


### And more...

- Links (symlinks), Filters (compression, checksums)
- Images, tables, units



## HDF5 Inspection Tools

- h5ls
- h5dump
- hdfview


### `h5ls`

- Like ls for hdf5 structure
- Useful for summarizing contents
- `h5ls -r`

```
/                        Group
/results                 Group
/results/count           Dataset {SCALAR}
/results/final           Group
/results/final/x         Dataset {1000}
/results/final/y         Dataset {1000}
/results/final/Position  Dataset {1000, 2}
/results/final/Mass      Dataset {1000}
```


### `h5dump`

- Full text dump of all data
- Can limit to certain groups (`-g /path`) or dataset (`-d /path/x`)

```
HDF5 "vasp.h5" {
GROUP "/" {
   GROUP "/results" {
      DATASET "count" {
         DATATYPE  H5T_STD_I64LE
         DATASPACE  SCALAR
         DATA {
         (0): 20
         }
      }
      GROUP "final" {
         DATASET "x" {
            DATATYPE  H5T_IEEE_F64LE
            DATASPACE  SIMPLE { ( 1000 / 1000 ) }
            DATA {
            (0): 0.052104
            (1): 0.139832
            (2): 1.398349
            ...
            }
            ATTRIBUTE "units" {
               DATATYPE  H5T_STRING {
                  STRSIZE 8;
                  STRPAD H5T_STR_NULLPAD;
                  CSET H5T_CSET_ASCII;
                  CTYPE H5T_C_S1;
               }
               DATASPACE  SCALAR
               DATA {
               (0): "furlongs"
               }
            }
         }
      }
   }
}
```


### HDFView

- Graphical viewer (and editor) for hdf5 files

<img src="https://docs.hdfgroup.org/hdf5/develop/datasetwdata.png" width="80%" style="border:0;box-shadow:none">



# HDF5 Libraries

- There is only one full HDF5 implementation (in C): hdf5
- Many interfaces built on top of this


## C library

```c
/* Open an existing file. */
hid_t file_id = H5Fopen(FILE, H5F_ACC_RDWR, H5P_DEFAULT);

/* Open an existing dataset. */
hid_t dataset_id = H5Dopen2(file_id, "/dset", H5P_DEFAULT);

/* Read the dataset. */
int dset_data[4][6];
herr_t status = H5Dread(dataset_id, H5T_NATIVE_INT, H5S_ALL, H5S_ALL, H5P_DEFAULT, dset_data);

/* Close the dataset. */
status = H5Dclose(dataset_id);

/* Close the file. */
status = H5Fclose(file_id);
```


## h5py

- h5py is the standard interface to hdf5 in python
- Provides a low-level interface (that looks a lot like the C API)
- More common high-level interface provides pythonic access


### h5py Files and Groups

- Open files with `h5py.File("file.h5", mode)`
   - `mode` can be `"r"` (read) `"w"` (create/truncate), or `"r+"` (read/write)
- Files can be closed using `with` (explicit scope) or automatically when unreferenced
- Groups provide dict-like interface, index with `[]` and paths

```python
file = h5py.File("file.h5", "r")
# <HDF5 file "file.h5" (mode r)>

group = file["results"]["final"]
group = file["results/final"]
# <HDF5 group "/results/final" (4 members)>
```


### h5py Datasets

- Datasets mostly look like numpy arrays, can be indexed with `[]`
- Scalar values are accessed by `()`

```python
count = file["results/count"]
# <HDF5 dataset "count": shape (), type "<i8">
count[()]
# 20

x = group["x"]
# <HDF5 dataset "x": shape (1000), type "<f8">
x.dtype
x.shape
x[0]
# 0.052104: numpy.float64
x[10:20]
# numpy.ndarray
```


### h5py Attributes

- Groups and Datasets have `attrs`
- Works like a simple dictionary

```python
group.attrs.keys()
x.attrs["units"]
```


### h5py writing

```python
file = h5py.File("file.h5", "w")
group = file.create_group("results/data")

x = group.create_dataset("x", (1000,), dtype="f")

x[0] = 0.052104

x.attrs["units"] = "furlongs"
```


### h5py multi-dimensional arrays

```python
pos = group.create_dataset("Position", (1000,2), dtype="f")

pos[10,1] = 3.5
pos[10][1] # works for access, not assignment!

pos[0,:]
pos[20:29,0] = numpy.arange(10)
```
