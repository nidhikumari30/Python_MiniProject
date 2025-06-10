from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')
    expression_label.config(text='')

def get_operator(op):
    global first_number, operator
    first_number = int(result_label['text'])
    operator = op
    expression_label.config(text=f"{first_number} {op}")
    result_label.config(text='')

def get_result():
    global first_number, second_number, operator
    second_number = int(result_label['text'])
    expression_label.config(text=f"{first_number} {operator} {second_number} =")
    
    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text='error')
        else:
            result_label.config(text=str(round(first_number / second_number, 2)))

root = Tk()
root.title('calculator')
root.geometry('280x380')
root.resizable(0, 0)
root.configure(background='black')

# Expression label
expression_label = Label(root, text='', bg='black', fg='lightgrey')
expression_label.grid(row=0, column=0, columnspan=5, pady=(20, 5), sticky='W')
expression_label.config(font=('verdana', 16))

# Result label
result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=1, column=0, columnspan=5, pady=(0, 20), sticky='W')
result_label.config(font=('verdana', 30, 'bold'))

# Buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('/', 5, 3)
]

for (text, row, col) in buttons:
    if text.isdigit():
        action = lambda x=text: get_digit(int(x))
    elif text == 'C':
        action = clear
    elif text == '=':
        action = get_result
    else:
        action = lambda x=text: get_operator(x)

    btn = Button(root, text=text, bg='#00a65a', fg='white', width=5, height=2, command=action)
    btn.grid(row=row, column=col)
    btn.config(font=('verdana', 14))

root.mainloop()
