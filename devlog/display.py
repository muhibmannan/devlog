
from . import VERSION
from . import utils

def show_banner():
    print()
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")


def show_menu():
    print()
    for i, option in enumerate(utils.MENU_OPTIONS):
        print(f"   {(i + 1):>2}. {option}")


def display_task(task):
    print(f"        ID: {task['id']}")
    print(f"        Task: {task['title']}")
    print(f"        Priority: {utils.PRIORITY_LABELS[task['priority'] - 1]} ({task['priority']})")
    print(f"        Status: {task['status']}")
    if not task['tags']:
        tags_display = "(no tags)"
    else:
        tags_display = ", ".join(sorted(task['tags']))
    print(f"        Tags: {tags_display}")
    if utils.DEBUG:
        print(f"        [debug] raw tags: {task['tags']!r}")
        print(f"        [debug] obj id: {id(task)}")


def list_tasks(tasks):
    if not tasks:
        print("\n(no tasks yet)")
        return
    
    for position, task in enumerate(tasks, start=1):
        print(f"\n  Task {position}")
        display_task(task)