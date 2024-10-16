print("----TASK MANAGER----")
def task():
    task_list = []

    total_tasks = int(input("Enter the number of tasks you want to Enter: "))
    for i in range(1, total_tasks+1):
        task_name = input("Enter the task name: ")
        task_list.append(task_name)
    
    print(f"Today's tasks are: {task_list}\n")

    while True:
        print("Enter\n1-Add\n2-Update\n3-View\n4-Delete\n5-Exit/Stop\n")
        operation = int(input("Enter a number to select operation: "))

        if operation == 1:
            add_task = input("Enter new task: ")
            if add_task in task_list:
                add_task = input("Enter a different task: ")
                task_list.append(add_task)
            else:
                task_list.append(add_task)
            print("The task has been added.\n")
        
        elif operation == 2:
            update_task = input("Enter the task you want to update: ")
            new_updated_task = input("Enter the updated task name: ")
            index = task_list.index(update_task)
            if new_updated_task in task_list:
                new_updated_task = input("The task already exists. Enter a different task: ")
                task_list[index] = new_updated_task
            else:
                task_list[index] = new_updated_task
            print("The task has been updated.\n")
        
        elif operation == 3:
            print(f"The updated task list is {task_list}")
        
        elif operation == 4:
            delete_task = input("Enter the task you want to delete: ")
            index = task_list.index(delete_task)
            del task_list[index]
            print("The task has been deleted.\n")
        
        elif operation == 5:
            print("Closing the program...\n")
            break

        else:
            print("Please enter a valid number.\n")


task()
