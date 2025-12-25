def load_task():
    try:
        with open("tasks.txt","r",encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
def save_task(tasks):
    with open("tasks.txt","w",encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
def show_task(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}.{task}")
def add_task(tasks):
    task=input("Enter new task:")
    tasks.append(task)
    save_task(tasks)
    print("Task added successfully!")
def complete_task(tasks):
    show_task(tasks)
    user_input=input("Enter task number to mark completed:")
    if not user_input.isdigit():
        print("Please enter a valid number!")
        return
    num=int(user_input)
    if num < 1 or num > len(tasks):
            print("Invalid task!")
            return
    if "✔️" in tasks[num-1]:
        print("Task already complete!")
        return
    tasks[num - 1] += "✔️"
    save_task(tasks)
    print("Task marked as completed!")

def delete_task(tasks):
    show_task(tasks)
    try:
        num=int(input("Enter task number to delete:").strip())
        if num < 1 or num > len(tasks):
            print("Invalid task!")
        else:
            tasks.pop(num -1)
            save_task(tasks)
            print("Task deleted!")
    except ValueError:
        print("Please enter a number!")

def main():
    tasks=load_task()

    while True:
        print("\n-----TO-DO LIST MENU-----")
        print("1.View tasks")
        print("2.Add tasks")
        print("3.Complete tasks")
        print("4.Delete tasks")
        print("5.Exit")

        choice=input("Enter your choice:")

        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
main()