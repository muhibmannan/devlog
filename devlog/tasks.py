from . import utils

STATUSES = ("todo", "in-progress", "done")

SORT_MENU = (
    ("Priority", lambda task: task['priority'], True),
    ("Title", lambda task: task['title'].lower(),    False),
)

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


def tasks_matching_tags(tasks, tags):
    return [task for task in tasks if task['tags'] & tags]


def calculate_stats(tasks):
    status_counts = {}
    for task in tasks:
        status = task['status']
        status_counts[status] = status_counts.get(status, 0) + 1

    total = sum(status_counts.values())

    done_count = status_counts.get("done", 0)
    rate = (done_count /len(tasks) * 100) if tasks else 0

    return status_counts, total, rate


class Task:

    VALID_STATUSES = {"todo", "in-progress", "done"}

    def __init__(self, title, priority=2, status="todo", tags=None):
        self.title = title
        self.priority = priority
        self.status = status
        self.tags = {Task.normalise_tag(tag) for tag in tags} if tags else set()
        self.id = None

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if value not in range(1, len(utils.PRIORITY_LABELS) + 1):
            raise ValueError(f"Invalid priority {value}. Must be between 1 and {len(utils.PRIORITY_LABELS)}")
        self._priority = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.VALID_STATUSES:
            allowed = ", ".join(sorted(self.VALID_STATUSES))
            raise ValueError(f"Invalid status {value}. Must be one of: {allowed}")
        self._status = value

    @property
    def priority_label(self):
        return utils.PRIORITY_LABELS[self.priority - 1]

    @staticmethod
    def normalise_tag(tag):
        return tag.strip().lower()

    @classmethod
    def from_dict(cls, data):
        title = data.get("title", "")
        priority = data.get("priority", 2)
        status = data.get("status", "todo")
        tags = data.get("tags")
        return cls(title, priority=priority, status=status, tags=tags)

    def mark_done(self):
        self.status = "done"

    def is_done(self):
        return self.status == "done"

    def add_tag(self, tag):
        clean = Task.normalise_tag(tag)
        if clean:
            self.tags.add(clean)

    def matches_tags(self, tags):
        return bool(self.tags & tags)

    def summary(self):
        id_display = self.id if self.id is not None else "?"
        tags_display = ", ".join(sorted(self.tags)) if self.tags else "(no tags)"
        return f"[#{id_display}] - {self.title} - {self.priority_label} - {self.status} - {tags_display}"

