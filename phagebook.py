import click


@click.group()
def cli():
    pass

@cli.command()
@click.option('--maxresults', default=20, type=int,
                help='The max number of phage genomes to compare and return')
@click.option('--maxevalue', default=.15, type=float,
                help='The max E value accepted in blast')
@click.option('--outputlocation', default='/', help='The output location of the results, defaults to the current directory.')
@click.argument('email', type=str, required=True)
@click.argument('input', type=str, required=True)
def run(maxresults, maxevalue, outputlocation, email, input):
    """
    This script takes one protein fasta file and then compares it against phages and outputs a gepard file
    \nArguments:
    \nemail: The email you supply to ncbi, required
    \ninput: The file containing the protein in fasta format
    """
    click.echo(email)
    click.echo(input)
