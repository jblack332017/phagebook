#! /usr/bin/env python
import subprocess
import os
import sys

def runGepard(abs_path,seq1file,seq2file):
	command_line = "java -cp "+abs_path+"Gepard-1.40.jar org.gepard.client.cmdline.CommandLine -seq1 "+ seq1file +" -seq2 "+ seq1file +" -matrix " + abs_path +  "matrices/edna.mat -outfile plot.png -upper 45 -lower 10"
	subprocess.call(command_line, shell=True)
