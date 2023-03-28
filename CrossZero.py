# в ключе: первый элемент - срока;
#          второй элемент - столбец
game = {
    (0, 0): "-",
    (1, 0): "-",
    (2, 0): "-",
    (0, 1): "-",
    (1, 1): "-",
    (2, 1): "-",
    (0, 2): "-",
    (1, 2): "-",
    (2, 2): "-"
}

i = 0 # счетчик количества ходов для фиксирования ничейного результата
correct_coord = list(map(int, [0, 1, 2])) #перечень допустимых значений координат

print("Приветствуем вас в игре! \n    КРЕСТИКИ - НОЛИКИ")
#игровое поле
def game_field():
    print(" ")
    print("  0 1 2")
    print("0", game[0, 0], game[0, 1], game[0, 2])
    print("1", game[1, 0], game[1, 1], game[1, 2])
    print("2", game[2, 0], game[2, 1], game[2, 2])
    print(" ")

game_field()
#
print("-*-*-*-*-*-*-")
player_1 = input("Введите  имя первого игрока. Он будет играть Крестиками и ходить первым :) ")
print(f"Привет, {player_1}! Как настроение? :)")
print("-*-*-*-*-*-*-")
player_2 = input("Введите  имя второго игрока: ")
print(f"Здравствуй, {player_2}! Тебе играть Ноликами. Готов к состязанию? ;)")
#
print(" ")
enter = input("Если вы готовы, нажмите Enter ")

while i < 5:

    def enter_coord_pl(pl):
        if pl == player_1:
            print(f"{player_1}, твой ход!")
            x_1 = int(input("Номер строки: "))
            y_1 = int(input("Номер столбца: "))
            return x_1, y_1
        if pl == player_2:
            if i == 4:
                print("Ничья!")
                quit()
            print(f"{player_2}, твой ход!")
            x_2 = int(input("Номер строки: "))
            y_2 = int(input("Номер столбца: "))
            return x_2, y_2

    x_1, y_1 = enter_coord_pl(player_1) #ход игрока 1


    def check_coord(pl, x, y):
        if x not in (correct_coord): #проверка верно веденных координат
            print("Неверные координаты")
            enter_coord_pl(pl)
        elif y not in (correct_coord): #проверка верно веденных координат
            print("Неверные координаты")
            enter_coord_pl(pl)
        elif game[(x, y)] != "-": #проверка, если ячейка уже занята
            print("Занято!")
            enter_coord_pl(pl)

    check_coord(player_1, x_1, y_1)
    game[(x_1, y_1)] = "X"


    def check_victory_player(player, cz): #функция проверки победы
        if game[(0, 0)] == game[(0, 1)] and game[(0, 0)] == game[(0, 2)] and game[(0, 0)] == cz:
            print(f"Победил {player}! Поздравляем!")
            quit()
        if game[(1, 0)] == game[(1, 1)] and game[(1, 0)] == game[(1, 2)] and game[(1, 0)] == cz:
            print(f"Победил {player}! Поздравляем!")
            quit()
        if game[(2, 0)] == game[(2, 1)] and game[(2, 0)] == game[(2, 2)] and game[(2, 0)] == cz:
            print(f"Победил {player}! Поздравляем!")
            quit()
        if game[(0, 0)] == game[(1, 0)] and game[(0, 0)] == game[(2, 0)] and game[(0, 0)] == cz:
            print(f"Победил {player}! Поздравляем!")
            quit()
        if game[(0, 1)] == game[(1, 1)] and game[(0, 1)] == game[(2, 1)] and game[(0, 1)] == cz:
            print(f"Победил {player}! Поздравляем!")
            quit()
        if game[(0, 2)] == game[(1, 2)] and game[(0, 2)] == game[(2, 2)] and game[(0, 2)] == cz:
            print(f"Победил {player}! Поздравляем!")
            quit()
        if game[(0, 0)] == game[(1, 1)] and game[(0, 0)] == game[(2, 2)] and game[(0, 0)] == cz:
            print(f"Победил {player}! Поздравляем!")
            quit()
        if game[(0, 2)] == game[(1, 1)] and game[(0, 2)] == game[(2, 0)] and game[(0, 2)] == cz:
            print(f"Победил {player}! Поздравляем!")
            quit()


    game_field() #печать игрового поля

    check_victory_player(player_1, "X")

    x_2, y_2 = enter_coord_pl(player_2)

    check_coord(player_2, x_2, y_2)
    game[(x_2, y_2)] = "0"
    game_field() #печать игрового поля

    check_victory_player(player_2, "0")
    i += 1




