import os
print("Welcome to Task manager")
if(os.path.exists("task.txt")!=True): open("task.txt","x")
while True:
    print("Write '/add [task]' to add task")
    print("Write '/view' to view all tasks")
    print("Write '/remove' to remove a task")
    print("Write 'exit' to leave")
    task=input("")
    if(task.split(" ")[0].lower()=="/add"):
        file=open("task.txt","r")
        text=file.read()
        file.close()
        file=open("task.txt",'a')
        if(text==""):
            file.write(f"{' '.join(task.split(' ')[1:len(task)])}")
        else:
            file.write(f"\n{' '.join(task.split(' ')[1:len(task)])}")
        file.close()

    elif(task.split(" ")[0].lower()=="/view"):
        print("Task are")
        print("")
        file=open("task.txt","r")
        lines=file.readlines()
        for line in lines:
            print(f"{str(lines.index(line)+1)}. {line}")
        file.close()
        print("")
    elif(task.split(" ")[0].lower()=="/remove"):
        print("Task are")
        print("")
        file=open("task.txt","r")
        lines=file.readlines()
        for line in lines:
            print(f"{str(lines.index(line)+1)}. {line}",end="")
        file.close()
        no=int(input("\nEnter your file index no.\n"))-1
        del lines[no]
        file=open("task.txt","w")
        file.writelines(lines)
        file.close()
    elif(task.lower()=="exit"):
        exit()
    else: print("Wrong command try again")       