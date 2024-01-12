def see_list(tasks_list):
    print("\n")
    for index, task in enumerate(tasks_list):
        description = task["description"]
        is_checked = task["status"] == "ok"

        print(f"{index + 1}. [{'✓' if is_checked else ' '}] {description}")
    print("\n")
    return