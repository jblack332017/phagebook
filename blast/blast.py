from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys


# Read fasta
fasta_file = open(sys.argv[1], 'r').read()
# Run blast over the internet
result_handle = NCBIWWW.qblast("blastp", "nr", fasta_file)
w = open('sequenceIds.txt', 'w')
# Begin Parsing
blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < sys.argv[2]:
                idNumbers = alignment.title.split("|")
                w.write(idNumbers[3]+"\n")


#
#
# blast_records = NCBIXML.parse(result_handle)
