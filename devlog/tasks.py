STATUSES = ("todo", "in-progress", "done")

def make_task(title, *tags, priority=2, status="todo"):
    return {"title": title, "tags": set(tags), "priority": priority, "status": status}


def next_task_id(tasks):
    if not tasks:
        return 1
    
    highest = tasks[0]["id"]

    for task in tasks:
        if task["id"] > highest:
            highest = task["id"]
    return highest + 1


def index_by_id(tasks):
    return {task['id']: task for task in tasks}


def find_task_by_id(tasks):
    index = index_by_id(tasks)
    while True:
        prompt = input("\nWhat's the task ID? (number, or 'cancel'): ").strip()

        if prompt.lower() == "cancel":
            return None
        
        if not prompt.isdigit():
            print("Please enter a number.")
            continue

        target_id = int(prompt)
        task = index.get(target_id)

        if task is None:
            print(f"\nTask not found. Enter valid ID.")
            continue
        return task


def filter_by_status(tasks):
    chosen = input(f"\nStatus to filter by ({' / '.join(STATUSES)}): ").strip().lower()
    return [task for task in tasks if task['status'] == chosen]


def parse_tags():
    raw = input("Tags (comma-separated, blank for none): ")
    pieces = raw.split(",")
    tags = {piece.strip().lower() for piece in pieces if piece.strip()}
    return tags


def filtered_by_tags(tasks):
    if not tasks:
        print("\nNo tasks to filter.")
        return
    tags = parse_tags()

    matches = [task for task in tasks if task['tags'] & tags]

    if not matches:
        print("No task found.")

    return matches


def calculate_stats(tasks):
    status_counts = {}
    for task in tasks:
        status = task['status']
        status_counts[status] = status_counts.get(status, 0) + 1

    total = sum(status_counts.values())

    done_count = status_counts.get("done", 0)
    rate = (done_count /len(tasks) * 100) if tasks else 0

    return status_counts, total, rate
