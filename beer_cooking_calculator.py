import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

lifeskills = ['Cooking', 'Production']
items = [['Beer', 'Pickled Vegetables', 'Cheese Pie', 'Vinegar'],['Wood/Planks/Plywood', 'Metal/Crystal', 'Flour', 'Dough']]

def calculate():
    recipes = [('beer', (6, 5, 2, 1), .6), ('cheese pie', (7, 5, 3, 3), .63), ('steamed bird', (), ), ('pickled vegetables', (8, 4, 2, 2), .88),
               ('vinegar', (1, 1, 1, 1), .22), ('wood', .5), ('metal', .3), ('flour', .1), ('dough', (1, 1), .11)]

    
    i = item.get()

    if i == 'Beer':
        wt = float(weight.get())
        runs = wt / recipes[0][2]

        messagebox.showinfo("Max Ingredients", 
                                "Grain: {}\n Water: {}\n Leavening Agent: {}\n Sugar: {}\n\n Total Runs: {}".format((recipes[0][1][1] * int(runs)),
                                (recipes[0][1][0] * int(runs)), (recipes[0][1][2] * int(runs)), (recipes[0][1][3] * int(runs)), int(runs)))

    if i == 'Cheese Pie':
        wt = float(weight.get())
        runs = wt / recipes[1][2]

        messagebox.showinfo("Max Ingredients", 
                                "Cheese: {}\n Dough: {}\n Eggs: {}\n Butter: {}\n\n Total Runs: {}".format((recipes[1][1][0] * int(runs)),
                                (recipes[1][1][1] * int(runs)), (recipes[1][1][2] * int(runs)), (recipes[1][1][3] * int(runs)), int(runs)))

    """if i == 'Steamed Bird':
        wt = float(weight.get())

        
        messagebox.showinfo("Max Ingredients", 
                                "Chicken Meat: {}\n Vinegar: {}\n ??: {}\n Cooking Liquor: {}".format(int(ch_cnt), int(d_cnt), int(eb_cnt), int(eb_cnt)))
    """

    if i == 'Pickled Vegetables':
        wt = float(weight.get())
        runs = wt / recipes[3][2]

        messagebox.showinfo("Max Ingredients", 
                                "Vegetable: {}\n Vinegar: {}\n Leavening Agent: {}\n Sugar: {}\n\n Total Runs: {}".format((recipes[3][1][0] * int(runs)),
                                (recipes[3][1][1] * int(runs)), (recipes[3][1][2] * int(runs)), (recipes[3][1][3] * int(runs)), int(runs)))

    if i == 'Vinegar':
        wt = float(weight.get())
        runs = wt / recipes[4][2]

        messagebox.showinfo("Max Ingredients", 
                                "Fruit: {}\n Leavening Agent: {}\n Grain: {}\n Sugar: {}\n\n Total Runs: {}".format((recipes[4][1][0] * int(runs)),
                                (recipes[4][1][1] * int(runs)), (recipes[4][1][2] * int(runs)), (recipes[4][1][3] * int(runs)), int(runs)))

    if i == 'Wood/Planks/Plywood':
        wt = float(weight.get())
        cnt = wt / recipes[4][1]
        
        messagebox.showinfo("Max Ingredients", 
                                "Inventory can hold {} Wood/Planks/Plywood".format(int(cnt)))

    if i == 'Metal/Crystal':
        wt = float(weight.get())
        cnt = wt / recipes[5][1]
        
        messagebox.showinfo("Max Ingredients", 
                                "Inventory can hold {} Metal/Crystal".format(int(cnt)))

    if i == 'Flour':
        wt = float(weight.get())
        cnt = wt / recipes[6][1]
        
        messagebox.showinfo("Max Ingredients", 
                                "Inventory can hold {} Wheat".format(int(cnt)))

    if i == 'Dough':
        wt = float(weight.get())
        runs = wt / recipes[7][2]
        
        messagebox.showinfo("Max Ingredients", 
                                "Wheat: {}\n Water: {}".format((recipes[7][1][0] * int(runs)), (recipes[7][1][1] * int(runs))))

def callback(eventObject):
    abc = eventObject.widget.get()
    skill = life.get()
    index=lifeskills.index(skill)
    item.config(values=items[index])



#Instantiate the window and name it
win = Tk()
win.title("Lifeskill Ingredient Calculator")

#Add a frame to hold all the widgets
frame = ttk.Frame(win, padding = "5 5 20 20")
frame.grid(column = 0, row = 0, sticky = (N, W, E, S))
win.columnconfigure(0, weight = 1)
win.rowconfigure(0, weight = 1)

#Add dropdown menus
life = ttk.Combobox(win, width = 30, value=(lifeskills))
life.set('Cooking') # default value

item = ttk.Combobox(win, width = 30, value=(items))
item.set("Beer") # default value

#Entry labels
Label(win, text='Life Skill:').grid(row = 0)
Label(win, text='Food Type:').grid(row = 1)
Label(win, text='Empty Inventory Weight:').grid(row = 2)

#instantiate entries
weight = Entry(win) 

#place entries into the frame
life.grid(row = 0, column = 1)
item.grid(row = 1, column = 1)
weight.grid(row = 2, column = 1)

#bind two menus together
item.bind('<Button-1>', callback)

#Instantiate a calculate button and place it into the frame
button = Button(win, text='Calculate', width=25, bg = 'Green',
                activebackground = 'White', command = lambda: calculate()) 
button.grid(row = 4)


win.mainloop()
