from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO

def align(fasta_path, path_to_clustal, system, outformat="clustal"):
  if system == "linux" or system == "linux2":
    path_to_clustal += ".lin"
  elif system == "darwin":
    path_to_clustal += ".mac"
  elif system == "win32":
    path_to_clustal += ".win"
  else:
    click.echo("Operating system not supported.")
    return
  cline = ClustalwCommandline(path_to_clustal, infile=fasta_path, output=outformat)
  stdout, stderr = cline()
