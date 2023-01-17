# Username generator

## Want to generate a username for your online account?
- Well you can use this short program to generate a username with your names

## How to use it?

- First install click module
> To do that type the following command:
```bash
pip install click


# if you end up having pip error try using pip3
pip3 install click

# if you don't have pip installed just run this command
sudo apt install python3-pip
```

### Now let's use it

```bash
# Options:
#   -fn, --fname TEXT  Enter your first name  [required]
#   -ln, --lname TEXT  Enter your last name  [required]
#   --help             Show this message and exit.

python gen_username.py -fn John -ln Doe
# [output]: JohnDoe12

python gen_username.py -fname John -lname Doe
# [output]: DoeJohn43
```
