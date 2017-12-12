#! /usr/bin/env python
import os
import shutil
from Bio import Entrez

def getProteins(input_file, email):
    Entrez.email = email #this parameter is the user's email address
    if os.path.exists("phagebook-results/proteins"):
        shutil.rmtree("phagebook-results/proteins")
    os.makedirs("phagebook-results/proteins")
    full = open('phagebook-results/proteins.fasta', 'w')
    for accession_no in open(input_file,"r"): #this parameter is a file with accession number
        accession_no = accession_no.strip()
        handle = Entrez.efetch(db="protein", id=accession_no, rettype="fasta")
        file = open("phagebook-results/proteins/"+accession_no+".fasta","w+")
        protein = handle.read()
        file.write(protein)
        full.write(protein)
        file.close()
    #each fasta file will be a separate file - named after accession number
