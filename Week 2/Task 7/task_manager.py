from task_operations import add_task, remove_task, update_task, view_tasks

def main():
    while True:
        print("\n1. Add\n2. Remove\n3. Update\n4. View\n5. Exit")
        choice = input("Choose (1-5): ")

        if choice == "1":
            add_task(input("Task: "))
            print("Added!")

        elif choice == "2":
            view_tasks()
            if remove_task(int(input("Number: "))):
                print("Removed!")
            else:
                print("Invalid number!")

        elif choice == "3":
            view_tasks()
            num = int(input("Number: "))
            if update_task(num, input("New task: ")):
                print("Updated!")
            else:
                print("Invalid number!")

        elif choice == "4":
            view_tasks()

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Pick 1-5!")

if __name__ == "__main__":
    main()