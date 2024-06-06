import string
import random

def password_gen(x): #x is the length of the password which will be specified by the user
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    char = string.punctuation

    must_pass = upper+lower+digits+char

    password = [random.choice(upper),random.choice(lower),random.choice(digits),random.choice(char) ]

    password = password + random.choices(must_pass, k=x-4)

    random.shuffle(password)

    return ''.join(password)

x = int(input("enter the length of the password: "))
r=password_gen(x)
print("the password is: ")
print(r)



