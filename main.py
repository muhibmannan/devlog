"""DevLog — a personal developer productivity tool for the terminal."""

VERSION = "0.1.0"

MENU_OPTIONS = ["Add Task", "List Tasks", "Quit"]
SORT_BY = ["Priority", "Date Added", "Status", "Back"]


def show_banner():
    print()
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")


def show_menu():
    print()
    for i, option in enumerate(MENU_OPTIONS):
        print(f"{i + 1}. {option}")


def get_menu_choice():
    raw = input("\nChoose an option: ").strip()
    if not raw.isdigit():
        return None
    value = int(raw)
    if value not in {1, 2, 3}:
        return None
    return value


def get_task_title():
    while True:
        raw = input("\nTask title (or 'cancel' to abort): ")
        cleaned = raw.strip()
        if cleaned.lower() == "cancel":
            return None
        if cleaned:
            return cleaned
        print("Title cannot be empty.")


def get_priority():
    while True:
        priority_input = input("Priority (1=low, 2=medium, 3=high): ").strip()
        if priority_input in {"1", "2", "3"}:
            priority = int(priority_input)
            return priority
        else:
            print("Invalid input. Please enter 1, 2 or 3.")


def parse_tags(raw):
    pieces = raw.split(",")
    clean = []
    for piece in pieces:
        piece = piece.strip()
        piece = piece.lower()
        if piece and piece not in clean:
            clean.append(piece)
    return clean


def get_task_input():
    title = get_task_title()
    if title is None:
        return None
    priority = get_priority()
    tags = parse_tags(input("Tags (comma-separated, blank for none): "))
    return {"title": title, "priority": priority, "tags": tags}
        

def display_task(task):
    print(f"        Task: {task['title']}")
    print(f"        Priority: {task['priority']}")
    if not task['tags']:
        tags_display = "(no tags)"
    else:
        tags_display = ", ".join(task['tags'])
    print(f"        Tags: {tags_display}")


def list_tasks(tasks):
    print()
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks):
        print(f"\nTask {i + 1}: ")
        display_task(task)    


def confirm_action(prompt):
    response = input(prompt).strip().lower()
    return response in ["y", "yes"]


def handle_choice(choice, tasks):
    if choice == 1:
        task = get_task_input()
        if task is not None:
            tasks.append(task)
        return True
    elif choice == 2:
        list_tasks(tasks)
        return True        
    elif choice == 3:
        if confirm_action("Are you sure you want to quit? (y/n): "):
            print("\nGoodbye!")
            return False
        return True


def run():
    tasks = []
    while True:
        show_menu()
        choice = get_menu_choice()
        if choice is None:
            print("Invalid choice, try again.")
            continue
        if not handle_choice(choice, tasks):
            break


def main():
    show_banner()
    run()


if __name__ == "__main__":
    main()