from tkinter import *

#create application main window
root= Tk()

#app title
root.title('Pizza Order App')

#app size
root.geometry('200x150')

#creating a frame
f = Frame(root, relief=SUNKEN , borderwidth=5, bg='#f5f5dc')
f.place(relx=0.5, rely=0.5, anchor= CENTER)

#label 1
my_label1= Label(f, text= 'Select Size:',font=('Verdana', 12, 'bold'), bg='#F1E586' )
my_label1.grid(row=0, column=0, sticky=W, padx=10, pady=10)

medium_price= 10.0
large_price=  15.0
extralarge_price= 20.0

Radio_buttons= {'Medium': medium_price,
                'Large': large_price,
                'Extra Large': extralarge_price}

medium_price= 10.0
large_price=  15.0
extralarge_price= 20.0

#control variable for radio button
var= IntVar()
var.set(medium_price)

#looping through the radio button widgets
row = 1
column = 0
for (text, value) in Radio_buttons.items():
    Radiobutton(f, text=text, variable=var, value=value, justify=LEFT, bg='#ffcc33', font=10).grid(
        row=row, column=column, padx=10, pady=10)
    column += 1

#label 2
my_label2= Label(f, text= 'Select Toppings:',font=('Verdana', 12, 'bold'), bg='#F1E586')
my_label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)

#checkbuttons control variables
cv1= IntVar()
cv2= IntVar()
cv3= IntVar()
cv4= IntVar()
cv5= IntVar()
cv6= IntVar()
cv7= IntVar()

#check button parameters
Checkboxes_widget= ( #Text, Variable, Row, Column
            ('Sausage', cv1, 3, 0),
            ('Pepperoni', cv2, 4, 0),
            ('Chicken', cv3, 5, 0),
            ('Mushroom', cv4, 6, 0),
            ('Black Olive', cv5, 7, 0),
            ('Red Pepper', cv6, 8, 0),
            ('Onion', cv7, 9, 0),
)

 #iterating through check buttons   
checkboxes= []
for _Text, _Variable, _Row, _Column,  in Checkboxes_widget:
    _Check= Checkbutton(f, text=_Text, variable= _Variable, bg='#ffcc33', font=10)
    _Check.grid(row= _Row, column= _Column, padx=10, pady=10, sticky=W,)
    checkboxes.append(_Check)
    
#call back fn for reset button         
def reset():
    cv1.set(0)
    cv2.set(0)
    cv3.set(0)
    cv4.set(0)
    cv5.set(0)
    cv6.set(0)
    cv7.set(0)
    entry1.delete(0, END)  #deletes existing text in the entry widget
    var.set(medium_price)
    
button1= Button(f, text= 'Reset',font=('Verdana', 15, 'bold'), command=reset, bg='#A88905')
button1.grid(row=10, column=1, padx=10, pady=10)

var_list = [cv1, cv2, cv3, cv4, cv5, cv6, cv7]  

#call back fn for calculate button
def calculate():
    x=0
    for i in var_list:
        if i.get() == 1:
            x += 1
    if var.get() == medium_price:
        price = 10 + 1.5*x
    if var.get() == large_price:
        price = 20 + 2.5*x
    if var.get() == extralarge_price:
        price = 30 + 3.5*x
        
    strPrice= '${}'.format(price)
    entry1.delete(0, END)
    entry1.insert(0, strPrice)
    
#button widget for Calculate price   
button2= Button(f, text='Calculate Price',font=('Verdana', 15, 'bold'), command=calculate, bg='#A88905')
button2.grid(row=10, column= 2, padx=10, pady=10)

#label widget for Total
label2= Label(f, text='Total:', bg='#F1E586', font=('Verdana', 15, 'bold'))
label2.grid(row=12, column=1, padx=10, pady=10, sticky=W)

#Entry widget 
entry1= Entry(f, width=10, bg='#F4F6F7', font=('Verdana', 15, 'bold'))
entry1.grid(row=12, column=2)


mainloop()
