import csv
Sneakers = {}
while True:
    print("Добро пожаловать! Ваш запрос?\n"
          "add - добавить\n"
          "show me all - показать всё\n"
          "add frome file - дозагрузить данные из файла(опт) \n"
          "delete smth - удаление позиции\n"
          "stats of position - статистика по всем позициям\n"
          "save to file - сохранение в файл\n")
    command = input()
    if command == "add":
        print("Задать название кроссовок:")
        sneakersname = input()
        print("Задать кол-во кроссовок:")
        sneakerscount = int(input())
        print("Задать имя производителя:")
        sneakersmanufactured = input()
        print("Задать цену:")
        sneakersprice = float(input())
        print("Задать размер:")
        sneakerssize = float(input())
        Sneakers[sneakersname] = list[sneakerscount, sneakersmanufactured, sneakersprice, sneakerssize]

    elif command == "show me all":
        print(Sneakers)

    elif command == "add frome file ":
        nolist = []
        with open("хранилово.csv", newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                nolist.append(row)
        for nolist in nolist:
            Sneakers[nolist[0]] = nolist[1:]
    elif command == "delete smth":
        print("Какое название кроссовок?")
        key = input()
        del Sneakers[key]
    elif command == "stats of position":
        print(len(Sneakers))
    elif command == "save to file":
        with open("сохраненки.csv", 'w') as f:
            w = csv.DictWriter(f, Sneakers.keys())
            w.writeheader()
            w.writerow(Sneakers)
