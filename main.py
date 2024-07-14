from tkinter import *

main = Tk()

main.title('Calculator')

main.geometry('600x550')

# Creiamo un frame per i bottoni
frame = Frame(main)
frame.pack()

# Creiamo una variabile per memorizzare l'input
input_text = StringVar()

# Creiamo un campo di input
input_field = Entry(main, textvariable=input_text, justify="right", width=50)
input_field.pack(pady=10)

# Funzione per aggiungere caratteri all'input
def click(key):
    current = input_text.get()
    input_text.set(current + str(key))

# Funzione per calcolare il risultato
def calculate():
    try:
        result = eval(input_text.get())
        input_text.set(result)
    except:
        input_text.set("Errore")

# Funzione per cancellare l'input
def clear():
    input_text.set("")

# Creiamo i bottoni numerici e degli operatori
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '.', '=', '/'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        Button(frame, text=button, padx=20, pady=20, command=calculate).grid(row=row, column=col)
    else:
        Button(frame, text=button, padx=20, pady=20, command=lambda x=button: click(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Aggiungiamo un bottone per cancellare
Button(frame, text="C", padx=20, pady=20, command=clear).grid(row=row, column=col)

main.mainloop()