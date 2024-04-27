def print_pole(m):
    print("\tA B C")
    for balls in range(len(m)):
        print(balls+1, *m[balls])
def proverka_pobedi_x(polyak):
    if (polyak[0][0] == polyak[0][1] == polyak[0][2] == "X" or
        polyak[1][0] == polyak[1][1] == polyak[1][2] == "X" or
        polyak[2][0] == polyak[2][1] == polyak[2][2] == "X" or
        polyak[0][0] == polyak[1][0] == polyak[2][0] == "X" or
        polyak[0][1] == polyak[1][1] == polyak[2][1] == "X" or
        polyak[0][2] == polyak[1][2] == polyak[2][2] == "X" or
        polyak[0][0] == polyak[1][1] == polyak[2][2] == "X" or
        polyak[0][2] == polyak[1][1] == polyak[2][0] == "X"):
            return True
    return False
def proverka_pobedi_o(polyak):
    if (polyak[0][0] == polyak[0][1] == polyak[0][2] == "O" or
        polyak[1][0] == polyak[1][1] == polyak[1][2] == "O" or
        polyak[2][0] == polyak[2][1] == polyak[2][2] == "O" or
        polyak[0][0] == polyak[1][0] == polyak[2][0] == "O" or
        polyak[0][1] == polyak[1][1] == polyak[2][1] == "O" or
        polyak[0][2] == polyak[1][2] == polyak[2][2] == "O" or
        polyak[0][0] == polyak[1][1] == polyak[2][2] == "O" or
        polyak[0][2] == polyak[1][1] == polyak[2][0] == "O"):
            return True
    return False
def game():
    pole = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]
    STROCHKI = {"A": 0, "B": 1, "C": 2}
    print_pole(pole)
    counter = 0
    while True:
        while True:
            koordinata_1 = int(input())
            koordinata_2 = input()
            if STROCHKI.get(koordinata_2) == None:
                print("Неверная координата!")
            elif pole[koordinata_1 - 1][STROCHKI[koordinata_2]] != "":
                print("Там уже стоит знак!")
            else:
                break
        pole[koordinata_1 - 1][STROCHKI[koordinata_2]] = "X"
        if proverka_pobedi_x(pole) == True:
            print("1 ИГРОК победил!")
            print("Ты свободен!")
            break
        print_pole(pole)
        counter += 1
        if counter == 9:
            print("Ничья!")
            break
        while True:
            koordinata_1_0 = int(input())
            koordinata_2_0 = input()
            if STROCHKI.get(koordinata_2_0) == None:
                print("Неверная координата!")
            elif pole[koordinata_1_0-1][STROCHKI[koordinata_2_0]] != "":
                print("Там уже стоит знак!")
            else:
                break
        pole[koordinata_1_0-1][STROCHKI[koordinata_2_0]] = "O"
        if proverka_pobedi_o(pole) == True:
            print("2 ИГРОК победил!")
            print("Потрачено")
            break
        print_pole(pole)
        counter += 1
        if counter == 9:
            print("Ничья!")
            print("Конец!")
            break
