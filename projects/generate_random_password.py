import random 
import math 

# All available options and their amount.
alpha = "abcdefghijklmnopqrstuvwxyz"
numeric = "0123456789"
other = "%?@$^#"

# Get input from the user (Length of password).
password_len = int(input("Enter Password Length: "))

# Select the value of each option based on 50-30-20 formula.
alpha_element = password_len // 2
numeric_element = math.ceil(password_len * 30/100)
other_element = password_len - (alpha_element + numeric_element)

password = []

# Core of program(generate password).
def generate_password(length,array,is_alpha=False):
    for i in range(length):
        item = random.randint(0 , len(array) -1)
        character = array[item]
        if is_alpha:
            case =random.randint(0,1)
            if case == 1:
                character = character.upper()
        password.append(character)

# Alpha part of password
generate_password(alpha_element,alpha,True)
# numeric part of password
generate_password(numeric_element,numeric)
# other part of password
generate_password(other_element,other)

# mix the elements
random.shuffle(password)

# Convert list to string
gen_password = ""
for i in password:
    gen_password += str(i)
print(gen_password)

