import sys
import os
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO

def align(fasta_path, path_to_clustal):
  if not os.path.exists(fasta_path):
    print "msa.py: Could not find file: " + fasta_path
    sys.exit(1)
  cline = ClustalwCommandline(path_to_clustal, infile=fasta_path)
  stdout, stderr = cline()
