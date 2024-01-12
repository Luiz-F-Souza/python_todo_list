from add_task import add_task
from see_list import see_list
from update_task import update_task
from complete_task import complete_task
from delete_completed_task import delete_completed_tasks
from valid_number import valid_number
import DATA


print("\nMenu de tarefas\n")

while True:
    for currentItem in DATA.menu_options:
        print(f"{currentItem['value']}. {currentItem['description']}")

    userInput = valid_number(input("Digite sua escolha: "))

    if userInput != 400:
        if (userInput == 1):
            task_description = input("Digite a tarefa que deseja adicionar: ")
            add_task(DATA.tasks_list, task_description)
        elif (userInput == 2):
            see_list(DATA.tasks_list)
        elif (userInput == 3):
            see_list(DATA.tasks_list)
            index_to_update = valid_number(
                input("Digite o número da tarefa para atualizar: ")) - 1

            if index_to_update != 400:
                update_task(DATA.tasks_list, index_to_update)
        elif (userInput == 4):
            see_list(DATA.tasks_list)
            index = valid_number(
                input("Digite o número da tarefa para completar: "))
            if index != 400:
                complete_task(DATA.tasks_list, index - 1)
        elif (userInput == 5):
            delete_completed_tasks(DATA.tasks_list)
        elif (userInput == 9):
            break

print("\nPrograma finalizado")
