import click
from words import words
from function import play_hang 

           
# @click.option('--attempts',default=6, help='number of attempts')
@click.command()
def hangman():
    play_hang()



if __name__ == '__main__':
    hangman()


