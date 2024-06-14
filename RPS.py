import random

print(
    "Witaj w grze papier, kamień i nożyce\n"
    "ZASADY GRY:\n"
    "Papier vs kamień --> Papier wygrywa\n"
    "Papier vs nożyce --> Nożyce wygrywa\n"
    "Kamień vs nożyce --> Kamień wygrywa\n"
)

choices = {
    1: "Papier",
    2: "Kamień",
    3: "Nożyce"
}

while True:
    print(
        "Wybierz sposród podanych:\n"
        "1 - Papier\n"
        "2 - Kamień\n"
        "3 - Nożyce\n"
    )

    choice = int(input("Podaj cyfrę: \n"))
    if choice in range(1, 4):
        break
    else:
        print("Liczba spoza zakresu. Wybierz liczbę od 1 do 3\n")

player_hand_position = choices[choice]
print("Wybór gracza: {}".format(player_hand_position))

computer_choice = random.randint(1, 3)
computer_hand_position = choices[computer_choice]
print("Wybór komputera: {}".format(computer_hand_position))

if player_hand_position == computer_hand_position:
    print("Remis")
elif player_hand_position == "Papier" and computer_hand_position == "Kamień":
    print("Gracz wygrywa!")
elif player_hand_position == "Kamień" and computer_hand_position == "Nożyce":
    print("Gracz wygrywa!")
elif player_hand_position == "Nożyce" and computer_hand_position == "Papier":
    print("Gracz wygrywa!")
else:
    print("Komputer wygrywa!")
