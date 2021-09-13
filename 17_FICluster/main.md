# Sciware

## Flatiron Clusters: Performance and Efficiency

https://github.com/flatironinstitute/learn-sciware-dev/tree/main/17_FICluster


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
- Ok to break in for quick, clarifying questions.
- Use Raise Hand feature for new topics or for more in-depth questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted on #sciware Slack.


## Future Sessions

- Chat & office hour: (TBD)
- Blender tutorial for scientific visualization animations (DATE?)
- Suggest topics and vote on options in #sciware Slack


## Today's agenda

- Hardware + file systems overview
- Modules
- Slurm and parallelization
  - Workshop: Share your workflow.
- Monitoring jobs
  - Workshop: Find a job, analyze it, look at SlurmUtil. - Slideo
- Monitoring file systems



# Running Parallel Jobs on the FI Cluster

## Slurm, Job Arrays, and disBatch

How to run jobs efficiently on Flatiron's clusters


## Slurm

- How do you share a set of computational resources among cycle-hungry scientists?
  - With a job scheduler! Also known as a queue system.
- Flatiron uses [Slurm](https://slurm.schedmd.com) to schedule jobs
  
<img width="30%" src="./assets/Slurm_logo.png">


## Slurm
- Wide adoption at universities and HPC centers. The skills you learn today will be highly transferrable!
- Flatiron has two clusters (Rusty & Popeye), each with multiple kinds of nodes (see the slides from earlier)
- The [SCC Wiki](https://docs.simonsfoundation.org/index.php/Public:Instructions_Iron_Cluster) lists all the node options and what Slurm flags to use to request them


## Slurm Basics

- Write a "batch file" that specifies the resources your job needs, and submit it to the queue with\
`sbatch myjob.sbatch`
  - Nodes? Cores? Memory? Time?

```bash
# File: myjob.sbatch
# These look like comments, but are interpreted by Slurm as sbatch flags
#SBATCH --mem=1G
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=genx

conda activate myjob-env

for fn in *.hdf5; do
    ./myjob $fn
done
```

- Submit the job to the queue with `sbatch myjob.sbatch`
- Check the status with: `squeue`


## Slurm Tip \#1: Estimating Resource Requirements

- Jobs don't necessarily run in order; most run via "backfill".
  - Implication: specifying the smallest set of resources for your job will help it run sooner
  - But don't short yourself!
- Memory requirements can be hard to assess, especially if you're running someone else's code


## Slurm Tip \#1: Estimating Resource Requirements

- How to estimate resource requirements:
  1. Make a conservative guess based on your knowlege of the program. For scientific computing, think about the sizes of big arrays and any files being read.
  1. Run a test job
  1. Check the actual usage with:\
  `sacct -j <jobid> -o MaxRSS,Elapsed`
    - `MaxRSS`: maximum "resident set size", usually corresponds to the memory requirement (`#SBATCH --mem`)
    - `Elapsed`: wall-clock runtime (`#SBATCH -t`)


## Slurm Tip \#2: Submitting Jobs
    
- Recommendation: don't submit more than ~100 jobs at once. Job schedulers are notoriously unresponsive.
- Trick: use `-p ccX,gen` to submit to multiple partitions.
  - In general, give Slurm the maximum flexibility to run your job


## Running Jobs in Parallel

- You've written a script to post-process a simulation output
- Have 10–10000 outputs to process
   ```bash
   $ ls $HOME/projname
   my_analysis_script.py
   $ ls /mnt/ceph/users/$USER/projname
   output1.hdf5  output2.hdf5  output3.hdf5 [...]
   ```
- Each file can be processed independently
- Ready to use Rusty! ... but how?


## Running Jobs in Parallel

- This pattern of independent parallel jobs is known as "embarrassingly parallel" or "pleasantly parallel"
- Two good options for pleasantly parallel jobs:
  - Slurm job arrays
  - disBatch
- Note: this job is a bad candidate for MPI
  - If the jobs don't need to communicate with each other, no need for MPI!


## Option 1: Slurm Job Arrays
- Queues up one job per output
- Syntax: `#SBATCH --array=1-10`, submits 10 jobs as an array
- Slurm is allowed to run each job in the array individually; no need to wait for 10 nodes (assuming 1 job per node)


## Option 1: Slurm Job Arrays
- Recommend organizing into two scripts: `launch_slurm.sh` and `job.slurm`
```bash
    #!/usr/bin/env bash
    # File: launch_slurm.sh

    # Recommendation: keep scripts in $HOME, and data in ceph
    projdir="/mnt/ceph/${USER}/projname/"
    jobname="job1"
    jobdir="${projdir}/${jobname}"

    mkdir -p ${jobdir}

    # Use the "find" command to write the list of files to process, 1 per line
    fn_list="${jobdir}/fn_list.txt"
    find ${projdir} -name 'output*.hdf5' | sort > ${fn_list}
    nfiles=$(wc -l < ${fn_list})

    # Launch a Slurm job array with ${nfiles} entries
    sbatch --array=1-${nfiles} job.slurm ${fn_list}
```


```bash
    # File: job.slurm
    
    #SBATCH -p ccX,gen  # or "-p genx" if your job won't fill a node
    #SBATCH -N 1
    #SBATCH --mem=128G
    #SBATCH -t 1:00:00
    
    # the file with the list of files to process
    fn_list=${1}
    
    # the job array index
    i=${SLURM_ARRAY_TASK_ID}
    
    # get the line of the file belonging to this job
    fn=$(tail -n+${i} ${fn_list} | head -n1)
    
    echo "About to process ${fn}"
    ./my_analysis_script.py ${fn}
```


## Option 1: Slurm Job Arrays
- What did we just do?
  - Get the list of N files we want to process (one per job)
  - Write that list to a file
  - Launch a job array with N jobs
  - Have each job get the i-th line in the file
  - Execute our science script with that file
- Why write a list of files when each Slurm job could run its own `find`?
    - Just to be sure that all jobs agree on the division of work (file sorting, files appearing or disappearing, etc)


## Option 2: disBatch
- What if jobs take a variable amount of time?
  - The job array approach forces you to request the longest runtime of any single job
- What if a job in the job array fails?
  - Resubmitting requires a manual post-mortem
- disBatch is a Slurm-aware dynamic dispatch mechanism that also has nice task tracking, addressing both of the above problems
  - Developed here at Flatiron: https://github.com/flatironinstitute/disBatch


## Option 2: disBatch
- Write a "task file" with one command-line command per line:
```bash
# File: jobs.disbatch
./my_analysis_script.py output1.hdf5
./my_analysis_script.py output2.hdf5
```
- Simplify as:
```bash
# File: jobs.disbatch
#DISBATCH PREFIX ./my_analysis_script.py
output1.hdf5
output2.hdf5
```
- Submit a Slurm job, invoking the `disBatch` executable with the task file as an argument:\
`sbatch [...] --wrap "disBatch jobs.disbatch"`


## Option 2: disBatch
```bash
#!/usr/bin/env bash
# File: submit_disbatch.sh

nnodes=4
cpus_per_task=8
mem_per_node=256G

projdir="/mnt/ceph/${USER}/projname/"
jobname="job1"
jobdir="${projdir}/${jobname}"
taskfn="${jobdir}/tasks.disbatch"

# Build the task file
echo "#DISBATCH PREFIX ./my_analysis_script.py" > ${taskfn}
find ${projdir} -name 'output*.hdf5' | sort >> ${taskfn}

# Submit the Slurm job
sbatch -p ccX,genx -N${nnodes} -c${cpus_per_task} --mem=${mem_per_node} \
    --wrap "disBatch ${taskfn}"
```


## Option 2: disBatch
- When the job runs, it will write a `status.txt` file, one line per task
- Resubmit any jobs that failed with:\
`disBatch -r status.txt -R`


## Comparison: Job Arrays and disBatch

- Slurm job arrays
  - Advantages
    - No external dependencies
    - Jobs can be scheduled by Slurm independently
  - Disadvantages
    - Can require multiple scripts to launch; a little clumsy
    - No good way to retry failed jobs
    - Doesn't scale to 1000+ jobs
    - Doesn't handle variable-length jobs


## Comparison: Job Arrays and disBatch
    
- disBatch
  - Advantages
    - Dynamic scheduling handles variable-length jobs
    - Status file of successful and failed jobs
    - Easy retries of failed jobs
    - Slurm just sees a single big job, which sometimes can go through faster than many small jobs
    
  - Disadvantages
    - Writing a disBatch task file can require multiple layers of bash escaping
    - disBatch is not builtin to Slurm


## Summary of Parallel Jobs
- Independent parallel jobs are a common pattern in scientific computing (parameter grid, analysis of multiple outputs, etc.)
- For these jobs, Slurm job arrays or disBatch are preferable over MPI
- Both are good solutions, but I (Lehman) tend to use disBatch more than job arrays these days, even when I just need static scheduling
  - Status file, easy retries, and scalability to 10K+ jobs
  
<img width="30%" src="./assets/slurm_futurama.webp">



# Benchmarking

## Why, when, what, and how?

Testing how to get the best performance out of your jobs


## Why benchmarking?

- Use the resources more efficiently
- Are you sure you are running optimally?
  - What processor architecture?
  - Which libraries? (eg: OpenBLAS vs MKL)
  - What MPI ranks / OpenMP threads ratio?
  - How many nodes for a given problem size?
- A 15 minutes benchmark can help your week-long computation get you more results
  - Or reduce it to a day-long computation!


## When to benchmark?

- Before you type `sbatch --time=a-very-long-time`
- For new projects
- For known projects: batch scripts are not "one size fits all"
  - Especially if your scripts come from another HPC center
  - Even locally we have very diverse machines!
  - New software versions can mean new configuration


## What to benchmark?

- Find something that can:
  - Represent your whole run in a short period of time
  - eg: a couple of iterations instead of 1000s of them
  - Use the same configuration you intend to use in production
- Be weary of "toy benchmarks":
  - They might benefit from requiring less memory, I/O, ...
  - If possible run with your real problem, but not to completion!


## How to benchmark?
  
- Domain-specific benchmarking tools
  - [MDBenchmark](https://mdbenchmark.readthedocs.io/) for Molecular Dynamic simulations
- Generic frameworks
  - [JUBE](https://www.fz-juelich.de/ias/jsc/EN/Expertise/Support/Software/JUBE/jube.html)
- These environments will let you:
  - Explore a space of different parameters
  - Easily read/format/export results
  - Produce scaling results for articles
  - <span style="color:#990000">Fill the Slurm queues with jobs: run in multiple steps! (or use disBatch when possible)</span>


## Using JUBE 

1. Create an XML (or YAML) file describing the benchmark
1. Launch using `jube run mybenchmark.xml`
1. While running with a batch scheduler:
  - `jube continue mybenchmark --id=N`: status
  - `jube result mybenchmark --id=N`  : partial results
  - `jube analyse mybenchmark --id=N` : update results
1. Once finished, get the complete results:
  - Formatted table: `jube result mybenchmark --id=N`
  - CSV: `jube result mybenchmark --id=N -s csv`


## Benchmark 1: GROMACS
<div style="display: flex;">
<small>
<ul>
<li>How many nodes to use?</li>
<li>How to distribute threads/ranks inside nodes?</li>
<li>GROMACS can be told to stop after _N_ minutes</li>
</ul>
<img style="height=8em; float: right" src="./assets/benchmarking/jube_gromacs.png">
</small>
</div>

```xml
    <parameterset name="param_set">
        <parameter name="num_nodes">1,2,3,4,5,6,7,8,9,10</parameter>
        <parameter name="ranks_per_node">128,64,32,16</parameter>
    </parameterset>
    <parameterset name="execute_set">
        <parameter name="cores_per_node">128</parameter>
        <parameter name="threads_per_rank">$procs_per_node/$cores_per_node</parameter>
        <parameter name="num_rank">$num_nodes*$ranks_per_node</parameter>
    </parameterset>
```
<small>System courtesy Sonya Hanson (CCB)</small>


## Benchmark 2: Gadget4
<div style="display: flex;">
<small>
<ul>
<li>Compare Intel MPI with OpenMPI</li>
<li>Weak scaling for a given problem type</li>
<li>Smulation stopped after a few iterations</li>
</ul>
<img style="height=8em; float: right" src="./assets/benchmarking/jube_gadget4.png">
</small>
</div>

```xml
    <parameterset name="param_set">
        <parameter name="num_nodes">1,2,4,8,16</parameter>
    </parameterset>
    <parameterset name="compile_set">
        <parameter name="lookchain">gcc_openmpi, intel</parameter>
        <parameter name="compiler">
          { "gcc_openmpi" : "gcc/7.4.0",
            "intel"       : "intel/compiler/2017-4" }
        </parameter>
        <parameter name="mpi_library">
          { "gcc_openmpi" : "openmpi4/4.0.5",
            "intel"       : "intel/mpi/2017-4" }
        </parameter>
    </parameterset>
```
<small>Simulation config courtesy Yin Li (CCA)</small>


## Benchmarking: conclusion

- Try and benchmark when you are starting a new large project
- Using a toolkit like JUBE can simplify your work
- For examples: https://github.com/gkrawezik/BENCHMARKS


# Survey

https://bit.ly/???


# Questions & Help

<img height=80% width=80% src="./assets/gifs/help.gif">
