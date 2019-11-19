import os
import sys

# automate script to cread md runs
f_sum = open("ROSETTA_README", "w")

target_dir = "/work/chem991e/cjurich/rosetta_runs"
# making new directory for md runs
os.mkdir(target_dir)


for i in range(10):
  job_str = """#!/bin/bash                                                             
#SBATCH -t 12:00:00
cd $WORK/rosetta_runs/"""+str(i)

  job_str +="""\nAbinitioRelax.default.linuxgccrelease -in:file:native ../../rosetta/1l2y.pdb -in:file:frag3 ../../rosetta/aa1l2yA03_05.200_v1_3 -in:file:frag9 ../../rosetta/aa1l2yA09_05.200_v1_3 -out:nstruct 100 -out:file:silent 1l2y_silent.out """

  os.mkdir(target_dir+ "/" + str(i))

  job_path = target_dir+"/" + str(i) + "/" + str(i) + ".sh"
  f = open(job_path, "w")
  f.write(job_str)
  f.close()

  f_sum.write("sbatch " + job_path + "\n")

f_sum.close()
