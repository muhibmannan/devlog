
from . import utils

def get_menu_choice():
    raw = input("\nChoose an option: ").strip()
    if not raw.isdigit():
        return None
    value = int(raw)
    if value not in range(1, len(utils.MENU_OPTIONS) + 1):
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


def parse_tags():
    raw = input("Tags (comma-separated, blank for none): ")
    pieces = raw.split(",")
    tags = {piece.strip().lower() for piece in pieces if piece.strip()}
    return tags


def get_task_input():
    title = get_task_title()
    if title is None:
        return None
    priority = get_priority()
    tags = parse_tags()
    return {"title": title, "priority": priority, "tags": tags}


def get_sort_choice(option_count):
    raw = input("\nChoose an option: ").strip()
    if not raw.isdigit():
        return None
    value = int(raw)
    if value not in range(1, option_count + 1):
        return None
    return value


def confirm_action():
    response = input("Are you sure you want to quit? (y/n): ").strip().lower()
    return response in ["y", "yes"]
