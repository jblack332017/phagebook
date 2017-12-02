#! /usr/bin/env python
import sys
import os
import shutil
from Bio import Entrez
Entrez.email = sys.argv[2] #this parameter is the user's email address

organisms = []
for fasta_file in os.listdir('proteins'):
    f = open('proteins/' + fasta_file)
    first_line = f.readline()
    start = first_line.index( "[" ) + 1
    end = first_line.index( "]", start )
    organism = first_line[start:end]
    if organism not in organisms:
        organisms.append(organism)


genome_ids = []
for organism in organisms:
    organism = organism.strip()
    search_term = organism+"[orgn] AND " + organism + "[title] AND complete genome[title]"
    print search_term
    handle=Entrez.esearch(db="nucleotide", retmax=100000, term=search_term, idtype="acc")
    genome_id=Entrez.read(handle)['IdList']
    if genome_id:
        genome_ids.append(genome_id[0])

w = open('genomeIds.txt', 'w')
for genome_id in genome_ids:
    w.write(genome_id+"\n")
