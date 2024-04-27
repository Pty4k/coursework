import XO
import Veselchak



def main():
    print("Я хочу сыграть с тобой в одну игру...")
    print("Выбор за тобой")
    otvet = input("hleb или bulka")
    if otvet == "hleb":
        XO.game()
    else:
        Veselchak.f1()


main()
