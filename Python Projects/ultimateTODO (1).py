#Neha Tirunagiri                   #<11/4/2022>
# <assignment5>



from ast import Add
from operator import index
import sys
import pickle

def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    itemFound = False
    keyName = ""

    index = -1
    keyTodo=todoList.keys()
    print(keyTodo)

    for i in keyTodo:
         for j in  todoList[i]:
          if j==item:  
             itemFound=True
             keyName=i
             index=j.index(item)
          else:
             continue

    
    
    return itemFound, keyName, index

def addItem(item, toList, todoList):
    
     itemFound,keyName,index=checkItem(item,todoList)
     if itemFound==True:
        print('Error! The item already exists in the list',keyName,index)
     else:
        for i in todoList.keys():
            if toList==i:
                
                todoList[i].append(item)
                

    
     return todoList

def deleteItem(item, todoList):
    itemFound,keyName,index=checkItem(item,todoList)
    
    if itemFound==True:
         todoList[keyName].clear()
    else:
        print('item not found')
 
    

    return itemFound, todoList

def moveItem(item, toList, todoList):
    
    itemFound,keyName,index=checkItem(item,todoList)
    
    if itemFound==True:
        itemFound,todoList=deleteItem(item,todoList)
        todoList=addItem(item,toList,todoList)
    else:
        print('item not found')
    return todoList

def printTODOList(todoList):
    
    for i in todoList:
        print(i,':',todoList[i])
    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            
            item=input('enter item to add:')
            addItem(item,"backlog",todoList)
            printTODOList(todoList)
            pass
        elif choice == "m":

            keys=todoList.keys()
            for i in keys:
              
                if todoList[i]!=[]:
                    print('dictionary is not empty')
                    item=input('what item would you like to move:')
                    list=input('what list do you want to move it to:')
                       
                    if list not in keys:
                        
                        
                            print('error enter another list name,list not in dictionary ')
                        
                            list=input('what list do you want to move it to:')
                            
                            todoList=moveItem(item,list,todoList)
                            printTODOList(todoList)
                            runApplication(todoList)
                            break 



                            
                    else:
                
                         todoList=moveItem(item,list,todoList)
                

                         printTODOList(todoList)
                        
                         runApplication(todoList)
                         break
                
                print('Dictionary is empty')





            
            
        elif choice == "d":
           
            item=input('enter item you want to delete')
            deleteItem(item,todoList)
            printTODOList(todoList)
            
            
            
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    taskOver = False

    print("The Ultimate TODO List")
    print()
    
    
    print("By: <Neha Tirunagiri>")
    print("[COM S 127 <A>]")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()