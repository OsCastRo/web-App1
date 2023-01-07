def get_tasks(filepath = "tasks.txt"):
    """"
    read a text file and return the list of tasks items
    """
    with open(filepath, 'r') as file_local:
        task_list = file_local.readlines()
    return task_list

def write_tasks(new_task,filepath = 'tasks.txt'):
    """
    Write a new task

    """
    with open(filepath, 'w') as file:
        file.writelines(new_task)


if __name__ == "__main__":
    print("Hello from functions")