import os
import random
import shutil
import string, secrets

number = random.randint(1, 100)
tents = 3

for tent in range(tents):
    print(f"Number of attempts: {tent + 1} out of {tents}")
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
    directory = r"C:\Users\Ghost Venom\Desktop\game\Gamed"
    itens = os.listdir(directory)

    if itens:
        item = random.choice(itens)
        item_path = os.path.join(directory, item)

        os.remove(item_path) if os.path.isfile(item_path) else False
        shutil.rmtree(item_path) if os.path.isdir(item_path) else False
        print(f"{item} was deleted")
        print(f"The number generated was {number}!")
        print("Try again!")
    else:
        print("You damn lucky guy, there's nothing to delete!")