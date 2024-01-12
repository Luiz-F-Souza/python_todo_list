def update_task(tasks_list, index_to_update):
    print("\n")
    if (index_to_update >= 0 and index_to_update < len(tasks_list)):

        new_task = input("Digite a descrição atualizada: ")
        tasks_list[index_to_update]["description"] = new_task
        print("Tarefa atualizada com sucesso")
    else:
        print(f"O número deve estar entre 1 e {len(tasks_list)}")

    print("\n")

    return