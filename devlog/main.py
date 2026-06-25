
"""DevLog — a personal developer productivity tool for the terminal."""

from .tasks import make_task, next_task_id, find_task_by_id, filter_by_status, tasks_matching_tags, calculate_stats, SORT_MENU
from .input import get_menu_choice, get_sort_choice, get_task_input, parse_tags, confirm_action
from .display import show_banner, show_menu, list_tasks
from .utils import toggle_debug


def choose_sort(tasks):
    if not tasks:
        return tasks
    
    print("\nSort by:")
    for i, row in enumerate(SORT_MENU):
        print(f"   {i + 1}. {row[0]}")

    choice = get_sort_choice(len(SORT_MENU))
    if choice is None:
        print("Invalid choice.")
        return tasks
        
    display_name, key_fn, reverse = SORT_MENU[choice - 1]
    return sorted(tasks, key=key_fn, reverse=reverse)

def complete_task_handler(tasks):
    if not tasks:
        print("\nNo tasks to mark complete.")
        return True
    task = find_task_by_id(tasks)
    if task is None:
        return True
    if task['status'] == "done":
        print("Task was completed before.")
    else:
        task['status'] = "done"
        print(f"\nTask '{task['title']}' is now marked as done.")
    return True

def delete_task_handler(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return True
    
    task = find_task_by_id(tasks)

    if task is None:
        return True

    tasks.remove(task)
    print(f"\nREMOVED: {task['title']}")
    return True

def show_stats_handler(tasks):
    if not tasks:
        print("\n(no tasks yet)")
        return True

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
    return True

def add_task_handler(tasks):
    raw = get_task_input()
    if raw is not None:
        task = make_task(raw['title'], *raw['tags'], priority=raw['priority'], status='todo')
        task['id'] = next_task_id(tasks)
        tasks.append(task)
        print(f"\nTask '{task['title']}' added.")
    return True

def list_tasks_handler(tasks):
    list_tasks(tasks)
    return True

def quit_handler(tasks):
    if confirm_action():
        print("\nGoodbye!")
        return False
    return True

def sort_tasks_handler(tasks):
    sorted_tasks = choose_sort(tasks)
    list_tasks(sorted_tasks)
    return True

def filter_by_status_handler(tasks):
    similar_status = filter_by_status(tasks)
    list_tasks(similar_status)
    return True

def filter_by_tags_handler(tasks):
    tags = parse_tags()
    matches = tasks_matching_tags(tasks, tags)
    list_tasks(matches)
    return True

def toggle_debug_handler(tasks):
    toggle_debug()
    return True

ACTIONS = {
    1: add_task_handler,
    2: list_tasks_handler,
    3: sort_tasks_handler,
    4: complete_task_handler,
    5: delete_task_handler,
    6: filter_by_status_handler,
    7: filter_by_tags_handler,
    8: show_stats_handler,
    9: toggle_debug_handler,
    10: quit_handler
}

def handle_choice(choice, tasks):
    handler = ACTIONS.get(choice)
    if handler is None:
        print("Invalid choice, try again.")
        return True
    return handler(tasks)


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