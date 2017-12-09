#! /usr/bin/env python
import os
import shutil
from Bio import Entrez

def getGenomes(input_file, email):
    Entrez.email = email
    if os.path.exists("phagebook-results/genomes"):
        shutil.rmtree("phagebook-results/genomes")
    os.makedirs("phagebook-results/genomes")

    try:
        os.remove("phagebook-results/genomes/full.fasta")
    except OSError:
        pass

    file = open("phagebook-results/genomes/full.fasta","a")
    for accession_no in open(input_file,"r"): #this parameter is a file with accession numbers
        accession_no = accession_no.strip()
        handle = Entrez.efetch(db="nucleotide", id=accession_no, rettype="fasta")
        file.write(handle.read())
    file.close()
    #each fasta file will be and entry in the genomes/full.fasta - named after accession number
