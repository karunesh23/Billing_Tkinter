# importing libraries
import tkinter as tk
import sqlite3

myconnection = sqlite3.connect('mydbfile.db')
curr = myconnection.cursor()

curr.execute('''
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY,
        order_id integer,
        item TEXT NOT NULL,
        price integer,
        quantity integer
    )
''')

curr.close()

WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 300
center = WINDOW_SIZE_X//2




def genrate_bill():
    bill_text = ""
    for i in LABLES:
        print(i)








# creating a window 
root = tk.Tk()


#####################################
########### root functions ##########
#####################################
# resizing window
root.geometry(f"{WINDOW_SIZE_X}x{WINDOW_SIZE_Y}")

# changing title
root.title("Billing System")

# no resizing
root.resizable(True, False)

SOFTWARE_TITLE = "BILLING SYSTEM"
myTitle = tk.Label(text=SOFTWARE_TITLE)
myTitle.place(x=center - (len(SOFTWARE_TITLE)*6//2) , y=20)



LABLES = {}






Namkeen = tk.Label(text = "Namkeen", font=("arial", 12, "bold"))
Q_Namkeen = tk.Entry()
LABLES["Namkeen"]  = [Namkeen, 50, Q_Namkeen]











SoftDrink = tk.Label(text = "SoftDrink", font=("arial", 12, "bold"))
Q_SoftDrink = tk.Entry()
LABLES["SoftDrink"]  = [SoftDrink, 40, Q_SoftDrink]

Chips = tk.Label(text = "Chips", font=("arial", 12, "bold"))
Q_Chips = tk.Entry()
LABLES["Chips"]  = [Chips, 20, Q_Chips]

Chocolates = tk.Label(text = "Chocolates", font=("arial", 12, "bold"))
Q_Chocolates = tk.Entry()
LABLES["Chocolates"]  = [Chocolates, 100, Q_Chocolates]





B_Total = tk.Button(text="Calculate Bill", font=("arial", 12), command=genrate_bill)
B_Total.place(x=250, y=250)






Lable_position_x = 12
Lable_position_y = 50
increment = 0

for i in LABLES:
    #print(LABLES[i])
    # LABELS have Lable object at index 0
    # LABELS have price at index 1
    # Lables Have entry at index 2

    # placing the lables at position according to x and y axies
    LABLES[i][0].place(x=Lable_position_x, y=Lable_position_y + increment)

    # placing the price at position accoding to x and y
    tk.Label(text=f"₹ {LABLES[i][1]}", font=("arial", 10)).place(x=Lable_position_x + 150,  y=Lable_position_y + increment)
    
    # placing the Entry at position accoding to x and y
    LABLES[i][2].place(x=Lable_position_x + 250, y=Lable_position_y + increment)
    
    # placing every item after 30 pixels below the preceding 
    increment += 30

# running the window
root.mainloop()

