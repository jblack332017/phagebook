from Bio.Blast import NCBIWWW
import sys


for index in xrange(1,len(sys.argv)):
    # Read fasta
    fasta_file = open(sys.argv[index], 'r').read()
    # Run blast over the internet
    result_handle = NCBIWWW.qblast("blastp", "nr", fasta_file)

    # Begin Parsing
    blast_records = NCBIXML.parse(result_handle)
    print blast_records

#
#
# blast_records = NCBIXML.parse(result_handle)
