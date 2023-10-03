import random

gmail = 'qwertyuiopasdfghjkllzxcvbnmm1234567890'
quantity_gmail = int(input('quantity gmail: '))
length_gmail = int(input('length gmail: '))
length_password = int(input('length password: '))



for n in range(quantity_gmail):
    password =''
    gmails =''
    for i in range(length_gmail):
        gmails += random.choice(gmail)
    for i in range(length_gmail):
        password += random.choice(gmail)
    print(gmails + '@gmail.com', password)
