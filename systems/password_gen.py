import random 
import string 

def generate_password(length: int ): # function to generate password
    alphabet =string.ascii_letters + string.digits + string.punctuation # every possible character that can be used in the password
    password = ''.join( random.choice(alphabet) for i in range(length)) # makes the password by randomly choosing characters from the alphabet
    return password # return password


def run_password_tool():
    length = int(input("how long do you want your password? : ")) # ask user for length of password

    if length <= 8: # checks if the password is less then 8 characters
        print("Warning: a password with les then 8 characters is not so save.")

    else: 
        print("your password is save.")



    print(generate_password(length)) # print wachtwoord in de terminal 

if __name__ == "__main__":
    run_password_tool()