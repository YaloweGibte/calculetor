from tkinter import *
import  ast

root = Tk()
i = 0
# global variable

def get_number(num):
    global i
    display.insert(i,num)
    i += 1


def get_operatot(operator):
    global i
    lenght = len(operator)
    display.insert(i,operator)
    i += lenght


def clear_all():
    display.delete(0,END)


def clear_one():
    ##option 1
    # entire_string = display.get()
    # if len(entire_string):
    #     new_string = entire_string[:-1]
    #     clear_all()
    #     display.insert(0,new_string)
    # else:
    #     clear_all()
    #     # insert empty string
    #     display.insert(0,"")

    #option 2
    new_str = display.get()
    new_list = list(new_str)
    lengths = len(new_list)
    new_str = ""
    for i in range(lengths - 1):
        new_str += new_list[i]
    clear_all()
    display.insert(0, new_str)


def calculetor():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string,mode="eval")
        result = eval(compile(node,'<string','eval'))
        clear_all()
        display.insert(0,result)

    except Exception:
        clear_all()
        display.insert(0,"Eror")

display = Entry(root)
display.grid(row=1,columnspan=5)


numbers = [1,2,3,4,5,6,7,8,9]
counter = 0

for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=2,height=1,command=lambda text = button_text:get_number(text))
        button.grid(row=x+2,column=y)
        counter += 1

button = Button(root, text="0", width=2,height=1,command=lambda :get_number(0))
button.grid(row=5,column=1)

counter = 0
operations = ['+','-',"*","/","%","(",")","**","**2","."]
for x in range(4):
    for y in range(3):
        if counter < len(operations):
            button = Button(root,text=operations[counter],width=2,command=lambda text=operations[counter]:get_operatot(text))
            button.grid(row=x + 2, column=y+4)
            counter += 1

Button(root,text="AC",width=2,height=1,command=clear_all).grid(row=5,column=0)
Button(root,text="=",width=2,height=1,command=calculetor).grid(row=5,column=2)
Button(root,text='<-',width=2,height=1,command=clear_one).grid(row=5,column=5)

root.mainloop()
# button.grid(row)
print("test")