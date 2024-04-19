import tkinter as tk
calculation=""

def add_cal(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def delete_last():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluation():
    global  calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")



root= tk.Tk()
root.geometry("300x275")
root.title("CALCULATOR")
display_frame = tk.Frame(root)
display_frame.grid(row=0, column=0, columnspan=5)
text_result = tk.Text(display_frame, height=2, width=14, font=("Arial", 24),bg="purple",fg="white")
text_result.pack()

btn_1=tk.Button(root,text="1",command=lambda :add_cal(1),width=3,font=("Aril",14),bg="#E6E6FA")
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",command=lambda :add_cal(2),width=3,font=("Aril",14),bg="#E6E6FA")
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3",command=lambda :add_cal(3),width=3,font=("Aril",14),bg="#E6E6FA")
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4",command=lambda :add_cal(4),width=3,font=("Aril",14),bg="#E6E6FA")
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root,text="5",command=lambda :add_cal(5),width=3,font=("Aril",14),bg="#E6E6FA")
btn_5.grid(row=3,column=2)

btn_6=tk.Button(root,text="6",command=lambda :add_cal(6),width=3,font=("Aril",14),bg="#E6E6FA")
btn_6.grid(row=3,column=3)

btn_7=tk.Button(root,text="7",command=lambda :add_cal(7),width=3,font=("Aril",14),bg="#E6E6FA")
btn_7.grid(row=4,column=1)

btn_8=tk.Button(root,text="8",command=lambda :add_cal(8),width=3,font=("Aril",14),bg="#E6E6FA")
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root,text="9",command=lambda :add_cal(9),width=3,font=("Aril",14),bg="#E6E6FA")
btn_9.grid(row=4,column=3)

btn_0=tk.Button(root,text="0",command=lambda :add_cal(0),width=3,font=("Aril",14),bg="#E6E6FA")
btn_0.grid(row=5,column=2)


btn_plus=tk.Button(root,text="+",command=lambda :add_cal("+"),width=3,font=("Aril",14),bg="#E6E6FA")
btn_plus.grid(row=2,column=4)

btn_minus=tk.Button(root,text="-",command=lambda :add_cal("-"),width=3,font=("Aril",14),bg="#E6E6FA")
btn_minus.grid(row=3,column=4)

btn_mul=tk.Button(root,text="*",command=lambda :add_cal("*"),width=3,font=("Aril",14),bg="#E6E6FA")
btn_mul.grid(row=4,column=4)

btn_div=tk.Button(root,text="/",command=lambda :add_cal("/"),width=3,font=("Aril",14),bg="#E6E6FA")
btn_div.grid(row=5,column=4)

btn_open=tk.Button(root,text="(",command=lambda :add_cal("("),width=3,font=("Aril",14),bg="#E6E6FA")
btn_open.grid(row=5,column=1)

btn_close=tk.Button(root,text=")",command=lambda :add_cal(")"),width=3,font=("Aril",14),bg="#E6E6FA")
btn_close.grid(row=5,column=3)


btn_delete = tk.Button(root, text="Del", command=delete_last, width=3, font=("Arial", 14),bg="#E6E6FA")
btn_delete.grid(row=6, column=2)

btn_clear=tk.Button(root,text="C",command=clear_field,width=3,font=("Aril",14),bg="purple",fg="white")
btn_clear.grid(row=6,column=1)


btn_equals=tk.Button(root,text="=",command= evaluation,width=3,font=("Aril",14),bg="#E6E6FA")
btn_equals.grid(row=6,column=3)


root.mainloop()