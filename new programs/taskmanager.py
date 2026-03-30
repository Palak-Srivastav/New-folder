#######

tasks = []

#Auxiliary function
def displaytask(all_tasks):
    print('\nYour Tasks:')
    for index, in task enumerate(all_tasks):

def newOperations(all_tasks):
    operations = input("Press 'A' to add new task, Press 'E' to edit a task,  Press 'R' to remove a task, Press 'F' to exit application" )

    if operations == 'A':
        addTask(all_tasks)
    elif operations == 'E':
        pass
    elif operations == 'R':
        pass
    elif operations == 'F':
        return
    else:
        newOperations(all_tasks)


def addTask(all_tasks):
    new_tasks = input('Add a new task:')
    all_tasks.append(new_tasks)

    for  tasks in all_tasks:
        print(tasks)

addTask(tasks)

