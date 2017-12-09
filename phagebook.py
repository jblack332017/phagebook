import click
import os
from sys import platform
from os import path
from blast import blast
from fasta import getProtein, getId, getGenome
from gepard import runGepard
from align import msa


@click.group()
def cli():
    pass

@cli.command()
@click.option('--maxresults', default=20, type=int,
                help='The max number of phage genomes to compare and return')
@click.option('--maxevalue', default=.15, type=float,
                help='The max E value accepted in blast')
@click.option('--outputlocation', default='/', help='The output location of the results, defaults to the current directory.')
@click.option('--alignformat',default='clustal', help='Desired output from clustal. Default: clustal.')
@click.argument('email', type=str, required=True)
@click.argument('input', type=str, required=True)

def run(maxresults, maxevalue, outputlocation, alignformat, email, input):
    """
    This script takes one protein fasta file and then compares it against phages and outputs a gepard file
    \nArguments:
    \nemail: The email you supply to ncbi, required
    \ninput: The file containing the protein in fasta format
    """
    if not os.path.exists("phagebook-results"):
        os.makedirs("phagebook-results")
    abspath = path.dirname(__file__)
    # click.echo("Running Blast")
    # blast.runBlast(input, maxevalue)
    # click.echo("Getting Genomes")
    # getProtein.getProteins("phagebook-results/sequenceIds.txt", email)
    # getId.getIds(email)
    # getGenome.getGenomes("phagebook-results/genomeIds.txt", email)
    runGepard.runGepard(abspath+"/gepard/", "phagebook-results/genomes/full.fasta","genomes/full.fasta")
    # msa.align("phagebook-results/genomes/full.fasta", abspath + "/align/clustalw2", platform, alignformat)
