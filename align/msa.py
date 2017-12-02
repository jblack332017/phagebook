import sys
import os
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO

if len(sys.argv) < 2:
  print "msa.py usage: python msa.py [infile]"
  sys.exit(1)
if not os.path.exists(sys.argv[1]):
  print "msa.py: Could not find file: " + sys.argv[1]
  sys.exit(1)
cline = ClustalwCommandline("./clustalw2", infile=sys.argv[1])
stdout, stderr = cline()
