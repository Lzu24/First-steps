
tasks=[]
tasks.append("posprzątaj")
tasks.append("naucz sie tego")


user_answer=-2


def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + "[" + str(task_index)+"]")
        task_index += 1

def add_task():
    task=input("Jakie zadanie chcesz dodać?")
    tasks.append(task)
    print("zadanie zostało dodane")        

def task_delete():
    task_index = int(input("podaj indeks"))
    if task_index < 0 or task_index > len(tasks) - 1:
        print("takie zadanie nie istnieje")
        return
    tasks.pop(task_index)
    print("usunięto zadanie")


def save_tasks_to_file():  
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()    

def load_tasks_from_file():
    try:
        file = open("tasks.txt") 

        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return



load_tasks_from_file()


while user_answer != 4:
    if user_answer == 1:
        show_tasks()



    if user_answer == 2:
        add_task()



    if user_answer == 3:
        task_delete()


    if user_answer == 5:
        save_tasks_to_file()

    print()
    print("plik został zapisany")
    print()

    print("1.pokaż zadania")
    print("2.dodaj zadania")
    print("3.usuń zadania")
    print("4.wyjdź")
    print("5.zapisz zmiany w obecnym pliku")
    

    user_answer=int(input("wybierz z listy: "))
    print()


    if int(user_answer) > 5:
        print("nie ma takiej pozycji")

