from multiprocessing.sharedctypes import Value
from tkinter import *

window = Tk()
window.title("Interest Calculater")
window.geometry("500x600")
window.configure(bg="lightblue")
window.resizable(width=False, height=False)


def calculate_Interest():

    result = ""

    try:
        p = float(pri_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        i = p*r*t/100

        si = round(i, 2)

        result = f"Simple Interset: ₹ {si}"

    except ValueError:
        result = "Please Enter a Number"

    output_msg = Label(result_frame, text=f"{result}", bg="lightyellow", font=(
        "Calibri", 12), width=50)
    output_msg.place(x=20, y=40)
    output_msg.pack()


app_title = Label(window, text="Interest Calculator", fg="black",
                  bg="lightblue", font="Calibri 25 bold italic")
app_title.place(x=140, y=25)


pri_lable = Label(window, text="Principal Amount (₹): ", fg="black",
                  bg="lightblue", font="Calibri 18")
pri_lable.place(x=20, y=110)

pri_entry = Entry(window, text="", bd=1, width=20)
pri_entry.place(x=270, y=120)


time_lable = Label(window, text="Interest Rate: ", fg="black",
                   bg="lightblue", font="Calibri 18")
time_lable.place(x=20, y=150)

time_entry = Entry(window, text="", bd=1, width=20)
time_entry.place(x=270, y=160)


rate_lable = Label(window, text="Interest Time: ", fg="black",
                   bg="lightblue", font="Calibri 18")
rate_lable.place(x=20, y=190)

rate_entry = Entry(window, text="", bd=1, width=20)
rate_entry.place(x=270, y=200)


submit = Button(window, text="Calculate",
                fg="black", font="Calibri 12", bg="green", width=15, bd=1, command=calculate_Interest)
submit.place(x=180, y=280)


result_frame = LabelFrame(window, text="Result",
                          bg="lightgreen", font=("Calibri", 12))
result_frame.pack()
result_frame.place(x=20, y=400)


result_label = Label(result_frame, text="",
                     bg="lightgreen", font="Calibri 12", width=50)
result_label.place(x=20, y=20)
result_label.pack()


window.mainloop()
