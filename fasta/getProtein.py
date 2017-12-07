#! /usr/bin/env python
import os
import shutil
from Bio import Entrez

def getProteins(input_file, email):
    Entrez.email = email #this parameter is the user's email address
    if os.path.exists("proteins"):
        shutil.rmtree("proteins")
    os.makedirs("proteins")

    for accession_no in open(input_file,"r"): #this parameter is a file with accession number
        accession_no = accession_no.strip()
        handle = Entrez.efetch(db="protein", id=accession_no, rettype="fasta")
        file = open("proteins/"+accession_no+".fasta","w+")
        file.write(handle.read())
        file.close()
    #each fasta file will be a separate file - named after accession number
