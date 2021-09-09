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

Different ways to run parallel jobs on the Flatiron cluster


## Slurm

- How do you share a set of computational resources among cycle-hungry scientists?
  - With a job scheduler! Also known as a queue system.
- Flatiron uses [Slurm](https://slurm.schedmd.com) to schedule jobs
- Wide adoption at universities and HPC centers. The skills you learn today will be highly transferrable!
- Flatiron has two clusters (Rusty & Popeye), each with multiple kinds of nodes
- The [wiki](https://docs.simonsfoundation.org/index.php/Public:Instructions_Iron_Cluster) lists all the options and what flags to use

<img height="40%" src="./assets/Slurm_logo.png">
<img height="40%" src="./assets/slurm_futurama.webp">


## Slurm Tips

- Jobs don't necessarily run in order; most run via "backfill".
  - Implication: specifying the smallest set of resources for your job will help it run sooner
  - But don't short yourself!
- How to estimate resource requirements:
  - Make a conservative guess based on your knowlege of the program. For scientific computing, think about the sizes of big arrays and any files being read.
  - Run a test job
  - Check the actual usage with: `sacct -j 1118837 -o MaxRSS,Elapsed`
    - `MaxRSS`: maximum "resident set size", usually corresponds to the memory requirement (`#SBATCH --mem`)
    - `Elapsed`: wall-clock runtime (`#SBATCH -t`)
- Recommendation: don't submit more than ~100 jobs at once. Job schedulers are notoriously unresponsive.
- Trick: use `-p ccX,gen` to submit to multiple partitions.
  - In general, give Slurm the maximum flexibility to run your job


## Running Jobs in Parallel

- You've written a script to post-process a simulation output
- Have 10–1000 outputs to process
- Each can be processed independently
- Ready to use Rusty! ... but how?


## Running Jobs in Parallel

- This pattern of independent parallel jobs is known as "embarrassingly parallel" or "pleasantly parallel"
- Two good options:
  - Slurm job arrays
  - disBatch
- Note: this job is a bad candidate for MPI
  - If the jobs don't need to communicate with each other, no need for MPI!


## Option 1: Slurm Job Arrays
- Queues up one job per output
- Syntax: `#SBATCH --array=0-9`, submits 10 jobs as an array
- Slurm is allowed to submit each job in the array individually; no need to wait for 10 nodes (assuming 1 job per node)


## Option 1: Slurm Job Arrays: Full Example
- Recommend organizing into two scripts: `./launch_slurm.sh` and `job.slurm`
```bash
    #!/usr/bin/env bash
    # File: launch_slurm.sh

    # Let's say
    projdir="/mnt/ceph/${USER}/projname/"
    jobname="job1"
    workingdir="${projdir}/${jobname}"

    mkdir -p ${workingdir}

    # Use the "find" command to write the list of files to process, 1 per line
    fn_list="${workingdir}/fn_list.txt"
    find ${projdir} -name 'output*.hdf5' > ${fn_list}
    nfiles=$(wc -l < ${fn_list})

    # Launch a Slurm job array with ${nfiles} entries
    sbatch --array=0-${nfiles} job.slurm ${fn_list}
```

```bash
    # File: job.slurm
    
    #SBATCH -p ccX,gen  # or "-p genx" if your job won't fill a node
    #SBATCH -N 1
    #SBATCH --mem=128G
    
    # the file with the list of files to process
    fn_list=${1}
    
    # the job array index
    i=${SLURM_ARRAY_TASK_ID}
    
    # get the line of the file belonging to this job
    fn=$(tail -n+${i} ${fn_list} | head -n1)
    
    ./my_analysis_script.py ${fn}
```


## Option 1: Slurm Job Arrays
- What did we just do?
  - Get the list of N files we want to process (one per job)
  - Write that list to a file
  - Launch a job array with N jobs
  - Have each job get the i-th line in the file
  - Execute our science script with that file


## Option 2: disBatch



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
    - Dynamic scheduling ensures jobs 
    - Status file of successful and failed jobs
    - Easy retries of failed jobs
    - Slurm just sees a single big job, which sometimes can go through faster than many small jobs
    
  - Disadvantages
    - Writing a disBatch task file can require multiple layers of bash escaping
    - disBatch is not builtin to Slurm


## Summary of Parallel Jobs
- Personally, I (Lehman) tend to use disBatch more than job arrays these days, even when I just need static scheduling
  - Status file, easy retries, and scalability to 100K+ jobs


# Survey

https://bit.ly/???


# Questions & Help

<img height=80% width=80% src="./assets/gifs/help.gif">