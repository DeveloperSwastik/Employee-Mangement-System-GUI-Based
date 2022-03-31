from tkinter import *


def calculator():
    root = Toplevel()

    root.geometry("305x452")
    root.resizable(0, 0)
    root.title("Calculator")
    root.config(background="#e8eaed")
    var = StringVar()

    def getValue(a):
        if len(var.get()) > 14:
            queryArea.config(font=(r"Times New Roman", 15))
        elif len(var.get()) > 9:
            queryArea.config(font=(r"Times New Roman", 30))
        if a == 1:
            var.set(f"{var.get()}1")
        elif a == 2:
            var.set(f"{var.get()}2")
        elif a == 3:
            var.set(f"{var.get()}3")
        elif a == 4:
            var.set(f"{var.get()}4")
        elif a == 5:
            var.set(f"{var.get()}5")
        elif a == 6:
            var.set(f"{var.get()}6")
        elif a == 7:
            var.set(f"{var.get()}7")
        elif a == 8:
            var.set(f"{var.get()}8")
        elif a == 9:
            var.set(f"{var.get()}9")
        elif a == 0:
            var.set(f"{var.get()}0")
        elif a == "+":
            var.set(f"{var.get()}+")
        elif a == "-":
            var.set(f"{var.get()}-")
        elif a == "*":
            var.set(f"{var.get()}*")
        elif a == "÷":
            var.set(f"{var.get()}/")
        elif a == "(":
            var.set(f"{var.get()}(")
        elif a == ")":
            var.set(f"{var.get()})")
        elif a == "=":
            try:
                answer = eval(var.get())
            except Exception as error:
                answer = "Bad Expression"
                print(error)
            if len(str(answer)) > 14:
                queryArea.config(font=(r"Times New Roman", 15))
            elif len(str(answer)) > 9:
                queryArea.config(font=(r"Times New Roman", 30))
            var.set(answer)
        elif a == "Clear":
            var.set("")
            queryArea.config(font=(r"Times New Roman", 45))

    def hoverOnBtn(a, button):
        if a == 1:
            button.config(background="#c8c8c9")
        elif a == 2:
            button.config(background="#d8dadd")

    queryArea = Entry(root, background="#c8c8c9", foreground="black", font=(
        r"Times New Roman", 45), justify=RIGHT, cursor="hand2", textvariable=var)
    queryArea.place(x=2, y=2, width=300, height=120)

    clear = Button(root, width=11, height=1, text="Clear", font=(
        r"Times New Roman", 10), command=lambda: getValue("Clear"), border=0, background="#d8dadd")
    clear.place(x=209, y=125)

    clear.bind("<Enter>", lambda event: hoverOnBtn(1, clear))
    clear.bind("<Leave>", lambda event: hoverOnBtn(2, clear))

    bracketOpen = Button(root, width=11, height=1, text="(", font=(
        r"Times New Roman", 10), command=lambda: getValue("("), border=0, background="#d8dadd")
    bracketOpen.place(x=10, y=125)
    bracketOpen.bind("<Enter>", lambda event: hoverOnBtn(1, bracketOpen))
    bracketOpen.bind("<Leave>", lambda event: hoverOnBtn(2, bracketOpen))

    bracketClose = Button(root, width=11, height=1, text=")", font=(
        r"Times New Roman", 10), command=lambda: getValue(")"), border=0, background="#d8dadd")
    bracketClose.place(x=110, y=125)
    bracketClose.bind("<Enter>", lambda event: hoverOnBtn(1, bracketClose))
    bracketClose.bind("<Leave>", lambda event: hoverOnBtn(2, bracketClose))

    button = Frame(root, background="#e8eaed")
    button.place(x=0, y=150, width=325, height=350)

    num1 = Button(button, width=5, height=1, text="1", font=(
        r"Times New Roman", 20), command=lambda: getValue(1), border=0, background="#d8dadd")
    num1.place(x=10, y=3)
    num1.bind("<Enter>", lambda event: hoverOnBtn(1, num1))
    num1.bind("<Leave>", lambda event: hoverOnBtn(2, num1))

    num2 = Button(button, width=5, height=1, text="2", font=(
        r"Times New Roman", 20), command=lambda: getValue(2), border=0, background="#d8dadd")
    num2.place(x=110, y=3)
    num2.bind("<Enter>", lambda event: hoverOnBtn(1, num2))
    num2.bind("<Leave>", lambda event: hoverOnBtn(2, num2))

    num3 = Button(button, width=5, height=1, text="3", font=(
        r"Times New Roman", 20), command=lambda: getValue(3), border=0, background="#d8dadd")
    num3.place(x=210, y=3)
    num3.bind("<Enter>", lambda event: hoverOnBtn(1, num3))
    num3.bind("<Leave>", lambda event: hoverOnBtn(2, num3))

    num4 = Button(button, width=5, height=1, text="4", font=(
        r"Times New Roman", 20), command=lambda: getValue(4), border=0, background="#d8dadd")
    num4.place(x=10, y=63)
    num4.bind("<Enter>", lambda event: hoverOnBtn(1, num4))
    num4.bind("<Leave>", lambda event: hoverOnBtn(2, num4))

    num5 = Button(button, width=5, height=1, text="5", font=(
        r"Times New Roman", 20), command=lambda: getValue(5), border=0, background="#d8dadd")
    num5.place(x=110, y=63)
    num5.bind("<Enter>", lambda event: hoverOnBtn(1, num5))
    num5.bind("<Leave>", lambda event: hoverOnBtn(2, num5))

    num6 = Button(button, width=5, height=1, text="6", font=(
        r"Times New Roman", 20), command=lambda: getValue(6), border=0, background="#d8dadd")
    num6.place(x=210, y=63)
    num6.bind("<Enter>", lambda event: hoverOnBtn(1, num6))
    num6.bind("<Leave>", lambda event: hoverOnBtn(2, num6))

    num7 = Button(button, width=5, height=1, text="7", font=(
        r"Times New Roman", 20), command=lambda: getValue(7), border=0, background="#d8dadd")
    num7.place(x=10, y=123)
    num7.bind("<Enter>", lambda event: hoverOnBtn(1, num7))
    num7.bind("<Leave>", lambda event: hoverOnBtn(2, num7))

    num8 = Button(button, width=5, height=1, text="8", font=(
        r"Times New Roman", 20), command=lambda: getValue(8), border=0, background="#d8dadd")
    num8.place(x=110, y=123)
    num8.bind("<Enter>", lambda event: hoverOnBtn(1, num8))
    num8.bind("<Leave>", lambda event: hoverOnBtn(2, num8))

    num9 = Button(button, width=5, height=1, text="9", font=(
        r"Times New Roman", 20), command=lambda: getValue(9), border=0, background="#d8dadd")
    num9.place(x=210, y=123)
    num9.bind("<Enter>", lambda event: hoverOnBtn(1, num9))
    num9.bind("<Leave>", lambda event: hoverOnBtn(2, num9))

    sum = Button(button, width=5, height=1, text="+", font=(r"Times New Roman",
                 20), command=lambda: getValue("+"), border=0, background="#d8dadd")
    sum.place(x=10, y=183)
    sum.bind("<Enter>", lambda event: hoverOnBtn(1, sum))
    sum.bind("<Leave>", lambda event: hoverOnBtn(2, sum))

    num0 = Button(button, width=5, height=1, text="0", font=(
        r"Times New Roman", 20), command=lambda: getValue(0), border=0, background="#d8dadd")
    num0.place(x=110, y=183)
    num0.bind("<Enter>", lambda event: hoverOnBtn(1, num0))
    num0.bind("<Leave>", lambda event: hoverOnBtn(2, num0))

    sub = Button(button, width=5, height=1, text="-", font=(r"Times New Roman",
                 20), command=lambda: getValue("-"), border=0, background="#d8dadd")
    sub.place(x=210, y=183)
    sub.bind("<Enter>", lambda event: hoverOnBtn(1, sub))
    sub.bind("<Leave>", lambda event: hoverOnBtn(2, sub))

    mul = Button(button, width=5, height=1, text="*", font=(r"Times New Roman",
                 20), command=lambda: getValue("*"), border=0, background="#d8dadd")
    mul.place(x=10, y=243)
    mul.bind("<Enter>", lambda event: hoverOnBtn(1, mul))
    mul.bind("<Leave>", lambda event: hoverOnBtn(2, mul))

    div = Button(button, width=5, height=1, text="÷", font=(
        r"Times New Roman", 20), command=lambda: getValue("÷"), border=0, background="#d8dadd")
    div.place(x=110, y=243)
    div.bind("<Enter>", lambda event: hoverOnBtn(1, div))
    div.bind("<Leave>", lambda event: hoverOnBtn(2, div))

    ans = Button(button, width=5, height=1, text="=", font=(
        r"Times New Roman", 20), command=lambda: getValue("="), border=0, background="#d8dadd")
    ans.place(x=210, y=243)
    ans.bind("<Enter>", lambda event: hoverOnBtn(1, ans))
    ans.bind("<Leave>", lambda event: hoverOnBtn(2, ans))

    root.mainloop()
