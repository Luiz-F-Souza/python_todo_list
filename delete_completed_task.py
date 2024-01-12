def delete_completed_tasks(tasks_list):

    for task in tasks_list:
        if (task["status"] == "ok"):
            tasks_list.remove(task)

    print("Tarefas completas deletadas")
    return