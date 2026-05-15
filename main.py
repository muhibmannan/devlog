"""<DevLog — a personal developer productivity tool for the terminal.>"""

VERSION = "0.1.0"

def show_banner():
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")

# The display name of the task, shown in all list views
task_title = "Test task"

# Current status of the task; "todo", "in-progress" or "done"
task_status = "in-progress"

# The task priority level: 1, 2 or 3
priority_level = 1

# A completion flag: True or False
completion_flag = False

# An estimated duration in hours
est_duration = 2.5


def get_task_input():
    title = input("Task title: ").strip()

    if not title:
        print("Nothing was typed.")
        return

    while True:
        priority_input = input("Priority (1=low, 2=medium, 3=high): ").strip()
        if priority_input in ["1", "2", "3"]:
            priority = int(priority_level)
            break
        else:
            print("Invalid input. Please enter 1, 2 or 3.")
            
        
    print(f"Task title: {title}, Priority level: {priority}")


def main():
    show_banner()
    print("DevLog is ready.")


    # Raw type() output is verbose: <class 'str'>
    # We can get just the name cleanly:
    print(f"task_title      = {task_title!r} ({type(task_title).__name__})")
    print(f"task_status     = {task_status!r} ({type(task_status).__name__})")
    print(f"priority_level  = {priority_level!r} ({type(priority_level).__name__})")
    print(f"completion_flag = {completion_flag!r} ({type(completion_flag).__name__})")
    print(f"est_duration    = {est_duration!r} ({type(est_duration).__name__})")

    get_task_input()


if __name__ == "__main__":
    main()