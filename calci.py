import tkinter as tk

def calculate_add():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        result_label.config(text=f"Result = {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input. Please try again.")

def calculate_subtract():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        result_label.config(text=f"Result = {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input. Please try again.")

def calculate_multiply():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        result_label.config(text=f"Result = {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input. Please try again.")

def calculate_divide():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 != 0:
            result = num1 / num2
            result_label.config(text=f"Result = {result}")
        else:
            result_label.config(text="Divide By Zero Error")
    except ValueError:
        result_label.config(text="Error: Invalid input. Please try again.")

root = tk.Tk()
root.title("Simple Calculator")
root.minsize(300,250)
root.configure(bg="#b2ebf2")

num1_label = tk.Label(root, text="Number 1:",bg="#b2ebf2",font=("Helvetica", 10, "bold"),fg="#003366")
num1_label.pack(padx=5, pady=5)
num1_entry = tk.Entry(root)
num1_entry.pack(padx=5, pady=5)
num2_label = tk.Label(root, text="Number 2:",bg="#b2ebf2",font=("Helvetica", 10, "bold"),fg="#003366")
num2_label.pack(padx=5, pady=5)
num2_entry = tk.Entry(root)
num2_entry.pack(padx=5, pady=5)

button_frame = tk.Frame(root,bg="#b2ebf2")
button_frame.pack(padx=5, pady=10)
add_button = tk.Button(button_frame, text="+", command=calculate_add,height= 1, width=3)
add_button.pack(side=tk.LEFT,padx=10)
subtract_button = tk.Button(button_frame, text="-", command=calculate_subtract,height= 1, width=3)
subtract_button.pack(side=tk.LEFT,padx=10)
button_frame = tk.Frame(root,bg="#b2ebf2")
button_frame.pack(padx=5, pady=5)
multiply_button = tk.Button(button_frame, text="*", command=calculate_multiply,height= 1, width=3)
multiply_button.pack(side=tk.LEFT,padx=10,)
divide_button = tk.Button(button_frame, text="/", command=calculate_divide,height= 1, width=3)
divide_button.pack(side=tk.LEFT,padx=10)

result_label = tk.Label(root, text="",bg="#b2ebf2",fg="#4a235a",font=("Helvetica", 10, "bold"))
result_label.pack()
root.mainloop()