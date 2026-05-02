def add_task(tasks, title):
    task = {
        "title": title,
        "done": False,
    }
    tasks.append(task)
    return tasks


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "tick" if task["done"] else "cross"
        print(f"{i}. {task['title']} [{status}]")


def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    return tasks


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks

