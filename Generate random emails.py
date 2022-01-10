from string import digits as numbers
from random import choice as generate

file = 'emails.txt'


nums = numbers
nums_len = [3,4]

email_links = ['@gmail','@hotmail','@yahoo','@outlook']
email_list = []
names = ['John','Peter','Mick','Bob','James','John','Max','Rob','Ronaldo','Harry']
com = '.com'

for i in range(100):

    email = generate(names) + ''.join(generate(nums) for i in range(generate(nums_len))) + generate(email_links) + com
    email_list.append(email)


write = open(file, 'w')

for email in email_list:

    write.write(email)
    write.write('\n')

write.close()


