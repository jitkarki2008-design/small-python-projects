# 06 - Password Generator using random + string
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase  # A-Z
    if use_lower:
        char_pool += string.ascii_lowercase  # a-z
    if use_digits:
        char_pool += string.digits           # 0-9
    if use_symbols:
        char_pool += string.punctuation      # !@#$ etc

    if not char_pool:
        return None

    # make sure at least one from each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # fill remaining length
    for _ in range(length - len(password)):
        password.append(random.choice(char_pool))

    random.shuffle(password)
    return "".join(password)

print("--- Password Generator [random + string] ---")

while True:
    try:
        length = int(input("\nEnter password length: "))
    except:
        print("Please enter a number!")
        continue

    upper = input("Include UPPERCASE? (y/n): ").lower() == 'y'
    lower = input("Include lowercase? (y/n): ").lower() == 'y'
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not (upper or lower or digits or symbols):
        print("Select at least one type!")
        continue

    if length < 4:
        print("Make it at least 4")
        continue

    pwd = generate_password(length, upper, lower, digits, symbols)
    print(f"\nYour password: {pwd}")

    again = input("\nGenerate again? (y/n): ").lower()
    if again != 'y':
        print("Done! Copy it safe.")
        break
    #edit
    