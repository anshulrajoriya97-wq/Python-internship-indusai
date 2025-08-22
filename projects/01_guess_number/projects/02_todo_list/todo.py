tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✅ Task added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("📋 To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"❌ Task removed: {removed}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            num = int(input("Enter task number to delete: ")) - 1
            delete_task(num)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
