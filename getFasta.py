#! /usr/bin/env python
import sys
from Bio import Entrez
Entrez.email = sys.argv[2] #this parameter is the user's email address    

for accession_no in open(sys.argv[1],"r"): #this parameter is a file with accession numbers
    accession_no = accession_no.strip()
    handle = Entrez.efetch(db="protein", id=accession_no, rettype="fasta")
    file = open(accession_no+".fasta","w+")
    file.write(handle.read())
    file.close()
#each fasta file will be a separate file - named after accession number
