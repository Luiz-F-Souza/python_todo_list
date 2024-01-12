def complete_task(tasks_list, index):

    tasks_list[index]["status"] = "ok"

    print("\nTarefa completada com sucesso \n")
    return