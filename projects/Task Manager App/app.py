def addTask():
    n=int(input("Enter number of task you want to do in a hold day "))
    for i in range(1,n+1):
        task=input("Enter task {} : ".format(i)).capitalize()
        tasks.append(task)

def displayAllTask():

    if len(tasks) == 0:
        print("Task list is empty")
    else:
        for count,i in enumerate(tasks):
            print(f"{count+1} : {i}")

def deleteTask():
    taskname=input("Enter taks name you want to delete : ").capitalize()
    if taskname not in tasks:
        print(f"{taskname} is not presented in list")
    else:
        tasks.remove(taskname)
        print(f"{taskname} is deleted succefully")

def updateTask():
    old_task=input("Enter old task : ").capitalize()
    new_task=input("Enter new task : ").capitalize()
    if old_task not in tasks:
        print(f"{old_task} is not presented in list")
    else:
        for i in tasks:
            index=tasks.index(i)

        tasks[index]=new_task
        print(f"{new_task} is update succefully")
if __name__=="__main__":
    #Task maneger app
    tasks=[]
    while True:
        user=int(input('''
Welcome to task manager
1.Display all task    
2.add task     
3.Delete Task
4.Update task
5.Exit to the app
'''))
        if user==1:
            displayAllTask()
        elif user==2:
            addTask()
        elif user==3:
            deleteTask()
        elif user==4:
            updateTask()
        elif user==5:
            print("Tank you for using this app\nHave a nice day a head")
            break
