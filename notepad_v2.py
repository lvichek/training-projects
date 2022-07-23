def show_menu():
    print("\ndo: - to add a task ")
    print("done: - to mark as done")
    print("check: - to check your lists")
    print("exit: - to exit obvi")

def do(task):
    todo_list.append(task)
    print(f"{task} added to your list") 

def done(task):
    todo_list.remove(task)
    done_list.append(task)
    print(f"{task} marked as done")

def print_tasks(tasks):
    for i in tasks:
        print (f"- {i}")      


print("hello to use this notepad simply print")
show_menu()

entry = input("\n ")
entry = entry.split(" ",1)


todo_list = []
done_list = []
options_list = ["do:", "done:", "check:", "exit"]


while entry[0] != "exit":


    if entry[0] in options_list:

        if entry[0] =="do:":
            do(entry[1])
            entry = input(" ")
            entry = entry.split(" ",1)   
            continue

        elif entry[0] == "done:":
             done(entry[1]) 
             entry = input(" ")
             entry = entry.split(" ",1)
             continue

        elif entry[0] == "check:":
             check_what = input("wanna see your todo or done? ")
             if check_what == "todo":

                 if len(todo_list) != 0:
                     print("\nok heres what you still have to do: ")
                     print_tasks(todo_list)
                 else:
                     print("oh you have nothing to do")

                 
             else:
                 if len(done_list) != 0:
                    print("\nheres what you have already done")
                    print_tasks(done_list)

                 else:
                    print("nothing to see here, do anything!")
            
             entry = input(" ")
             entry = entry.split(" ",1)  
             continue
              
            

        continue    

    else:
        print(f"ugh sorry i dont understand :( \ntell me something i know, i'll show you the menu again: {show_menu()}")  
        continue       

    

print("ok see ya!")

  
