"""DevLog — a personal developer productivity tool for the terminal."""

from .tasks import STATUSES, make_task, next_task_id, index_by_id, find_task_by_id, filter_by_status, parse_tags, filtered_by_tags, calculate_stats
from . import VERSION

MENU_OPTIONS = (
    "Add Task",
    "List Tasks",
    "Sort Tasks",
    "Mark Complete",
    "Delete Task",
    "Filter by Status",
    "Filter by Tag(s)",
    "Stats",
    "DEBUG mode ON/OFF",
    "Quit"
    )

SORT_BY = ("Priority", "Date Added", "Status", "Back")

PRIORITY_LABELS = ("low", "medium", "high")

DEBUG = False

def toggle_debug():
    global DEBUG
    DEBUG = not DEBUG
    print()
    print(f"   DEBUG is {'ON' if DEBUG else 'OFF'}.")


def show_banner():
    print()
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")


def show_menu():
    print()
    for i, option in enumerate(MENU_OPTIONS):
        print(f"   {(i + 1):>2}. {option}")


def get_menu_choice():
    raw = input("\nChoose an option: ").strip()
    if not raw.isdigit():
        return None
    value = int(raw)
    if value not in range(1, len(MENU_OPTIONS) + 1):
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


def get_task_input():
    title = get_task_title()
    if title is None:
        return None
    priority = get_priority()
    tags = parse_tags()
    return {"title": title, "priority": priority, "tags": tags}


def display_task(task):
    print(f"        ID: {task['id']}")
    print(f"        Task: {task['title']}")
    print(f"        Priority: {PRIORITY_LABELS[task['priority'] - 1]} ({task['priority']})")
    print(f"        Status: {task['status']}")
    if not task['tags']:
        tags_display = "(no tags)"
    else:
        tags_display = ", ".join(sorted(task['tags']))
    print(f"        Tags: {tags_display}")
    if DEBUG:
        print(f"        [debug] raw tags: {task['tags']!r}")
        print(f"        [debug] obj id: {id(task)}")


def list_tasks(tasks):
    if not tasks:
        print("\n(no tasks yet)")
        return
    
    for position, task in enumerate(tasks, start=1):
        print(f"\n  Task {position}")
        display_task(task)
    

SORT_MENU = (
    ("Priority", lambda task: task['priority'], True),
    ("Title", lambda task: task['title'].lower(),    False),
)

def get_sort_choice():
    raw = input("\nChoose an option: ").strip()
    if not raw.isdigit():
        return None
    value = int(raw)
    if value not in range(1, len(SORT_MENU) + 1):
        return None
    return value


def choose_sort(tasks):
    if not tasks:
        return tasks
    
    print("\nSort by:")
    for i, row in enumerate(SORT_MENU):
        print(f"   {i + 1}. {row[0]}")

    choice = get_sort_choice()
    if choice is None:
        print("Invalid choice.")
        return tasks
        
    display_name, key_fn, reverse = SORT_MENU[choice - 1]
    return sorted(tasks, key=key_fn, reverse=reverse)


def complete_task(tasks):
    if not tasks:
        print("\nNo tasks to mark complete.")
        return
    task = find_task_by_id(tasks)
    if task is None:
        return
    if task['status'] == "done":
        print("Task was completed before.")
    else:
        task['status'] = "done"
        print(f"\nTask '{task['title']}' is now marked as done.")


def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return
    
    task = find_task_by_id(tasks)

    if task is None:
        return

    tasks.remove(task)
    print(f"Removed: {task['title']}")


def show_stats(tasks):
    if not tasks:
        print("(no tasks yet)")
        return

    counts_status, total, rate = calculate_stats(tasks)

    labels = [f"{status}:" for status in counts_status] + ["Total:"]
    width = max(len(label) for label in labels)

    print("\nDevLog Stats")
    print(" " + "-" * (width + 4))

    for status, count in counts_status.items():
        label = f"{status}:"
        print(f" {label:<{width}}  {count}")
    print(f" {'Total:':<{width}}  {total}")
    print(f"Completion rate: {rate:.1f}%")
    pending = [task['title'] for task in tasks if task['status'] != "done"]
    if pending:
        tasks_list = ", ".join(pending)
        print(f"Pending: {tasks_list}")


def confirm_action():
    response = input("Are you sure you want to quit? (y/n): ").strip().lower()
    return response in ["y", "yes"]


def handle_choice(choice, tasks):
    if choice == 1:
        raw = get_task_input()
        if raw is not None:
            title = raw['title']
            priority = raw['priority']
            tags = raw['tags']
        
            task = make_task(title, *tags, priority=priority, status="todo")
            task['id'] = next_task_id(tasks)
            tasks.append(task)
            print(f"\nTask '{task['title']}' added.")
        return True
    
    elif choice == 2:
        list_tasks(tasks)
        return True
    
    elif choice == 3:
        sorted_tasks = choose_sort(tasks)
        list_tasks(sorted_tasks)
        return True

    elif choice == 4:
        complete_task(tasks)
        return True
    
    elif choice == 5:
        delete_task(tasks)
        return True
    
    elif choice == 6:
        similar_status = filter_by_status(tasks)
        list_tasks(similar_status)
        return True
    
    elif choice == 7:
        similar_tags = filtered_by_tags(tasks)
        list_tasks(similar_tags)
        return True
    
    elif choice == 8:
        show_stats(tasks)
        return True
    
    elif choice == 9:
        toggle_debug()
        return True

    elif choice == 10:
        if confirm_action():
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