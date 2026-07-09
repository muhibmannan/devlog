
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


PRIORITY_LABELS = ("low", "medium", "high")

DEBUG = False

def toggle_debug():
    global DEBUG
    DEBUG = not DEBUG
    print()
    print(f"   DEBUG is {'ON' if DEBUG else 'OFF'}.")
