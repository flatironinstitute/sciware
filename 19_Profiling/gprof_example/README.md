# gprof example
- [code](main.cc)
- [run script](run.sh), example output:
   ```
   g++ -g -pg -Wall -std=c++20 -fopenmp -o run_array main.cc
   g++ -g -pg -Wall -std=c++20 -fopenmp -DUSE_UNORDERED_MAP=1 -o run_map main.cc

   time ./run_array
   init=0.000010 fill=8.851493 add=3.033038 total=11.884541 res=6.67935e+06
   5.63user 7.64system 0:13.27elapsed 99%CPU (0avgtext+0avgdata 16472896maxresident)k

   time ./run_map
   init=0.000004 fill=30.898140 add=11.052448 total=41.950591 res=6.67935e+06
   46.23user 0.61system 0:46.85elapsed 99%CPU (0avgtext+0avgdata 717820maxresident)k
   ```
- example gprof output: [array](gprof_array.txt), [map](gprof_map.txt)
