import random 
import string

def password_strenght(password):
    if len(password) < 8:
        return "Weak ❌"
    elif len(password) < 12:
        return "Medium ⚠️"
    else:
        return "Strong ✔️"

def password_generator():
    try:
        lenght=int(input("Enter password lenght:"))
        if lenght <=0:
            print("Lenght must be positive!")
            return
        
        letters=input("Include letters? (yes/no):").lower()
        numbers=input("Include numbers? (yes/no):").lower()
        symbols=input("Include symbols? (yes/no):").lower()

        characters=""

        if letters == "yes":
            characters += string.ascii_letters
        if numbers == "yes":
            characters += string.digits
        if symbols == "yes":
            characters += string.punctuation

        if characters == "":
            print("❌ You must select at least one option!")
            return
    
        password= "".join(random.choice(characters)for _ in range(lenght))
        print("\n ✔️ Generated Password:")
        print(password)
        print("Strenght:",password_strenght(password))
    except ValueError:
        print("❌ Please enter a valid number!")
def generate_multiple():
    try:
        count=int(input("How many password?:"))
        lenght =int(input("Password lenght:"))

        characters=string.ascii_letters+string.digits+string.punctuation

        for i in range(count):
            password= "".join(random.choice(characters)for _ in range(lenght))
            print(f"{i+1}.{password}")
    except ValueError:
        print("❌ Invalid input!")
def main():
    while True:
        print("\n 🔐PASSWORD GENERATOR MENU🔐")
        print("1. Generate Password")
        print("2. Generate Multiple Password")
        print("3. Exit")
        choice=input("Enter your choice:")

        if choice == "1":
            password_generator()
        elif choice == "2":
            generate_multiple()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice")
main()