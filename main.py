"""<DevLog — a personal developer productivity tool for the terminal.>"""

VERSION = "0.1.0"

def show_banner():
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")


def show_menu():
    print("\nWhat would you like to do?")
    print("  1. Add Task")
    print("  2. List Tasks")
    print("  3. Quit")

def run():
    while True:
        show_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "":
            print("\nInvalid choice. Try again.")
        elif choice == "1":
            print("\n[Add Task — coming soon]")
        elif choice == "2":
            print("\n[List Tasks — coming soon]")
        elif choice == "3":
            print("\nGoodbye!")
            break

def get_task_input():
    title = input("Task title: ").strip()

    if not title:
        print("Nothing was typed.")
        return

    while True:
        priority_input = input("Priority (1=low, 2=medium, 3=high): ").strip()
        if priority_input in ["1", "2", "3"]:
            priority = int(priority_input)
            break
        else:
            print("Invalid input. Please enter 1, 2 or 3.")
                   
    print(f"Task title: {title}, Priority level: {priority}")


def main():
    show_banner()
    run()

    choice = input("\nEnter your choice: ").strip()
    if not choice:
        print("No input received. Please make a selection.")
    elif choice == "1":
        get_task_input()
    elif choice == "2":
        print("List Tasks selected.")
    elif choice == "3":
        print("Quitting DevLog. Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")




if __name__ == "__main__":
    main()