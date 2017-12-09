from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO

def align(fasta_path, path_to_clustal):
  cline = ClustalwCommandline(path_to_clustal, infile=fasta_path)
  stdout, stderr = cline()
