#! /usr/bin/env python
import os
import shutil
from Bio import Entrez

def getGenomes(input_file, email):
    Entrez.email = email
    if os.path.exists("genomes"):
        shutil.rmtree("genomes")
    os.makedirs("genomes")

    try:
        os.remove("genomes/full.fasta")
    except OSError:
        pass

    file = open("genomes/full.fasta","a")
    for accession_no in open(input_file,"r"): #this parameter is a file with accession numbers
        accession_no = accession_no.strip()
        handle = Entrez.efetch(db="nucleotide", id=accession_no, rettype="fasta")
        file.write(handle.read())
    file.close()
    #each fasta file will be and entry in the genomes/full.fasta - named after accession number
