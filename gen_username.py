from string import digits as numbers
from random import choice as generate
from random import randint
import click

file = 'emails.txt'

@click.command()
@click.option('-fn','--fname', help="Enter your first name", required=True)
@click.option('-ln','--lname', help="Enter your last name", required=True)
def create_email(fname, lname):

    if not len(fname) < 3:
        fname_length = randint(2, len(fname)//2)
        fname = fname[:fname_length]

    if not len(lname) < 3:
        lname_length = randint(2, len(lname)//2)
        lname = lname[:lname_length]


    list_info = []
    list_info.append(fname)
    list_info.append(lname)

    get_random = generate(list_info)
    get_other = list_info[list_info.index(get_random) -1]

    build_email = f"{get_random}{get_other}{''.join(generate(numbers) for _ in range(randint(2, 4)))}"
    print(build_email)



    
if __name__ == "__main__":
    create_email()

