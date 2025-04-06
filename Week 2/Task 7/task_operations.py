from file_handler import read_tasks, write_tasks

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)

def remove_task(num):
    tasks = read_tasks()
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        write_tasks(tasks)
        return True
    return False

def update_task(num, new_task):
    tasks = read_tasks()
    if 1 <= num <= len(tasks):
        tasks[num - 1] = new_task
        write_tasks(tasks)
        return True
    return False

def view_tasks():
    tasks = read_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks!")