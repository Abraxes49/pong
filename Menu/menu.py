import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage





from game import Game
from gameki import Game2

def add_label():
    game = Game()


def add_label2():
    gameki = Game2()

def add_label3():
    pass

def add_label4():
    pass
    #pygame.quit()

                        # tutorial basteln
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hauptmenü")
    root.geometry("1792x1072")

    background_image = PhotoImage(file="Keen.png")                  #bild

    background_label = tk.Label(root, image=background_image)       #bild
    background_label.place(relwidth=1, relheight=1)                  #bild

    position = (0,0)                                                # muss immer oben links


    button = tk.Button(
        root,
        text="Let Us Play Pong",
        command=add_label,
        width=50,
        height=5,
        font= ("Courier",9),
        fg="#39FF14",
        background="grey",
        activebackground="grey",
        activeforeground="#39FF14",

    )
    button2 = tk.Button(
        root,
        text="Gegen die Ki",
        command=add_label2,
        width=50,
        height=5,
        font=("Courier", 9),
        fg="#39FF14",
        background="grey",
        activebackground="grey",
        activeforeground="#39FF14",
    )
    button3 = tk.Button(
        root,
        text="Highscore",
        command=add_label3,
        width=50,
        height=5,
        font=("Courier", 9),
        fg="#39FF14",
        background="grey",
        activebackground="grey",
        activeforeground="#39FF14",
    )
    button4 = tk.Button(
        root,
        text="Beenden",
        command=add_label4,
        width=50,
        height=5,
        font=("Courier", 9),
        fg="#39FF14",
        background="grey",
        activebackground="grey",
        activeforeground="#39FF14",

    )
    ### label = tk.Label(root, text="", font=("Courier", 100))

    button.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button.place(relx=0.51, rely=0.35, anchor="center")
    button2.place(relx=0.51, rely=0.44, anchor="center")
    button3.place(relx=0.51, rely=0.53, anchor="center")
    button4.place(relx=0.51, rely=0.62, anchor="center")
    root.mainloop()


