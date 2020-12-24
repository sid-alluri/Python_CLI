import sys
import datetime
date = str(datetime.datetime.now().date())


# print(date.date())
TODOPATH  = 'PATH/todo.txt'
DONEPATH = 'PATH/done.txt'

tasks_todo = len(list(open(TODOPATH,'r')))
tasks_done = int(len(list(open(DONEPATH,'r')))/2)
# print(tasks_done)

# print(sys.argv)

def help():
    print("\n\t\t\t   HELP")
    print("\n\t\tCommand format: ./todo FUNCTION\n")
    print("\n\t     Functions     \t      Description")
    print('\t---------------------------------------------')
    print('\tls               \t       Show Pending Todos')
    print('\tadd "new item"   \t       Add a new item in  Todo list')
    print('\tdelete item_number\t       Delete an item in todo list')
    print('\tdone   item_number\t       Complete the item in todo list')
    print('\treport           \t       Statistics')
    print('\tclear_todo            \t       Clears the whole Todo list')
    print('\tclear_done            \t       Clears the whole Done list')
    print('\thelp             \t       Gives the usage details of command')
    print("\n\t\t\t   Developer Info")
    print('\t Developed by Alluri L S V Siddhartha Varma')
    print('\t Email: siddhartha18101@iiitnr.edu.in\n')

def ls():
    file = open(TODOPATH,'r')
    for i,x in reversed(list(enumerate(file, start=1))):
        print ("[{}]. {}".format(i,x))

def add(newtask, tasks_todo):
    file = open(TODOPATH,'a+')
    file.seek(0)
    file.write(newtask+"\n")
    print('Added todo: "{}"'.format(newtask))
    tasks_todo = tasks_todo + 1 

def delete(tasknumber, tasks_todo):
    if (tasknumber <= tasks_todo):
        file = open(TODOPATH,'r+')
        todolist = list(file)
        deltask = todolist.pop(tasknumber - 1)
        print('Deleted todo #{}'.format(tasknumber))

        file.truncate(0)

        for x in todolist:
            file.write(x)

    else:
        print("Error: todo #() does not exist. Nothing deleted.".format(tasknumber))

def done(tasknumber, tasks_todo, tasks_done):
    if (tasknumber <= tasks_todo): 
        file = open(TODOPATH,'r+')
        donefile = open(DONEPATH,'a+')
        todolist = list(file)
        donetask = todolist.pop(tasknumber - 1)
        print('Marked todo #{} as done'.format(tasknumber))
        file.truncate(0)
        donefile.write('x '+ date + " " + donetask+"\n")
        for x in todolist:
            file.write(x)
    else:
        print("Error: todo #{} does not exist.".format(tasknumber))

def clear_todo():
    file = open(TODOPATH,'r+')
    file.truncate(0)
def clear_done():
    file = open(DONEPATH,'r+')
    file.truncate(0)

def report(tasks_done, tasks_todo):
    print('{} Pending: {} Completed: {}'.format(date,tasks_todo, tasks_done))


if (len(sys.argv) ):
    msg = sys.argv[2]

if (len(sys.argv) > 1):
    command = sys.argv[1]
    

    if command == 'ls':
        ls()
    elif command == 'add':
        add(msg,tasks_todo)
    elif command == 'delete':
        delete(int(msg), tasks_todo)
    elif command == 'done':
        done(int(msg), tasks_todo, tasks_done)
    elif command == 'clear_todo':
        clear_todo()
    elif command == 'clear_done':
        clear_done()
    elif command == 'help':
        help()
    elif command == 'report':
        report(tasks_done, tasks_todo)
    else:
        help()
else:
    help()




