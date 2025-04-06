def read_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks))