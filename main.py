from task_manager import add_task, view_tasks, mark_done, delete_task
from storage import load_tasks, save_tasks

def main():
    tasks = load_tasks()
    while True:
        print("\n==== TO-DO APP ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Tasks")
        print("4. Delete Done")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task: ")
            tasks = add_task(tasks, title)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            num = int(input("Task number: ")) - 1
            tasks = mark_done(tasks, num)
            save_tasks(tasks)
        elif choice == "4":
            view_tasks(tasks)
            num = int(input("Task number: ")) - 1
            tasks = delete_task(tasks, num)
            save_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
        
            