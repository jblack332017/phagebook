#! /usr/bin/env python
import shlex, subprocess
import sys

def runGepard(seq1file,seq2file):
	command_line = "java -cp Gepard-1.40.jar org.gepard.client.cmdline.CommandLine -seq1 "+ seq1file +" -seq2 "+ seq1file +" -matrix matrices/edna.mat -outfile plot.png"
	args = shlex.split(command_line)
	print args
	p = subprocess.Popen(args)
	p.wait()

#runGepard(sys.argv[1],sys.argv[2])
#can run gepard from command line using 2 files names as arguments