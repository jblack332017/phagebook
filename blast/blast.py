from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys


def runBlast(input_file, max_e):
    # Read fasta
    fasta_file = open(input_file, 'r').read()
    # Run blast over the internet
    result_handle = NCBIWWW.qblast("blastp", "nr", fasta_file)
    w = open('phagebook-results/sequenceIds.txt', 'w')
    # Begin Parsing
    blast_records = NCBIXML.parse(result_handle)
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < max_e:
                    idNumbers = alignment.title.split("|")
                    w.write(idNumbers[3]+"\n")
