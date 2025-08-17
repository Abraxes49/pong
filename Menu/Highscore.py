import tkinter as tk
import gameki
import game

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Highscore")
    root.geometry("800x600")

    Highscore = ["numberone","zweiiiii","Blubberfischies"]
    # Highscore.append()
    # sort nach punktzahl

    button = tk.Button(
    root,
    text="1." + Highscore[0],
    width=50,
    height=5,
    font=("Courier", 9),
    fg="gold",
    background="Blue",

    )
    button2 = tk.Button(
    root,
    text="2." + Highscore[1],
    width=50,
    height=5,
    font=("Courier", 9),
    fg="silver",
    background="Blue",

    )
    button3 = tk.Button(
    root,
    text="3." + Highscore[2],
    width=50,
    height=5,
    font=("Courier", 9),
    fg="black",
    background="Blue",

    )

    button.pack()
    button.place(relx=0.51, rely=0.35, anchor="center")
    button.pack()
    button2.place(relx=0.51, rely=0.40, anchor="center")
    button.pack()
    button3.place(relx=0.51, rely=0.45, anchor="center")
    root.mainloop()
