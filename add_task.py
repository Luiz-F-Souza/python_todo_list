def add_task(tasks_list, task):
    print("\n")
    tasks_list.append({
        "description": task,
        "status": "pending"
    })

    print("Tarefa adicionada com sucesso!\n")
    return