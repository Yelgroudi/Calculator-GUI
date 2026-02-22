import tkinter as tk

def addieren(a, c):
   ergebnis = a + c
   return ergebnis

def subtrahieren(a, c):
   ergebenis = a - c
   return ergebenis

def multiplizieren(a, c):
   ergebnis = a * c
   return ergebnis

def dividieren(a, c):
   if(c == 0):
      return("Ungültige Zahl.")
   ergebnis = a / c
   return ergebnis

def button_klick(zahl):
   display.insert(tk.END, str(zahl))

def button_clear():
   display.delete(0, tk.END)  

def button_gleich():
   try:
      rechnung = display.get()
      ergebnis = eval(rechnung)
      display.delete(0, tk.END)
      display.insert(0, str(ergebnis))

   except:
      display.delete(0, tk.END)
      display.insert(0, "Fehler")



root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

display = tk.Entry(root, font = ("Arial", 24), justify = "right", borderwidth = 5, relief = "sunken")
display.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 10)

button1 = tk.Button(root, font = "bold", text = "1", width = 6, height = 3, command = lambda: button_klick(1))
button1.grid(row = 1, column = 0, sticky = "nsew")

button2 = tk.Button(root, font = "bold", text = "2", width = 6, height = 3, command = lambda: button_klick(2))
button2.grid(row = 1, column = 1, sticky = "nsew")

button3 = tk.Button(root, font = "bold", text = "3", width = 6, height = 3, command = lambda: button_klick(3))
button3.grid(row = 1, column = 2, sticky = "nsew")

button_plus = tk.Button(root, font = ("Arial", 12, "bold"), text = "+", bg = "#17505E", fg = "white", width = 6, height = 3, command = lambda: button_klick("+"))
button_plus.grid(row = 1, column = 3, sticky = "nsew")

button4 = tk.Button(root, font = "bold", text = "4", width = 6, height = 3, command = lambda: button_klick(4))
button4.grid(row = 2, column = 0, sticky = "nsew")

button5 = tk.Button(root, font = "bold", text = "5", width = 6, height = 3, command = lambda: button_klick(5))
button5.grid(row = 2, column = 1, sticky = "nsew")

button6 = tk.Button(root, font = "bold", text = "6", width = 6, height = 3, command = lambda: button_klick(6))
button6.grid(row = 2, column = 2, sticky = "nsew")

button_minus = tk.Button(root, font = ("Arial", 12, "bold"), text = "-", bg = "#17505E", fg = "white", width = 6, height = 3, command = lambda: button_klick("-"))
button_minus.grid(row  = 2, column = 3, sticky = "nsew")

button7 = tk.Button(root, font = "bold", text = "7", width = 6, height = 3, command = lambda: button_klick(7))
button7.grid(row = 3, column = 0, sticky = "nsew")

button8 = tk.Button(root, font = "bold", text = "8", width = 6, height = 3, command = lambda: button_klick(8))
button8.grid(row = 3, column = 1, sticky = "nsew")

button9 = tk.Button(root, font = "bold", text = "9", width = 6, height = 3, command = lambda: button_klick(9))
button9.grid(row = 3, column = 2, sticky = "nsew")

button_multi = tk.Button(root, font = ("Arial", 12, "bold"), text = "*", bg = "#17505E", fg = "white", width = 6, height = 3, command = lambda: button_klick("*"))
button_multi.grid(row = 3, column = 3, sticky = "nsew")

buttonC = tk.Button(root, font = "bold", text = "C", width = 6, height = 3, command = button_clear)
buttonC.grid(row = 4, column = 0, sticky = "nsew")

button0 = tk.Button(root, font = "bold", text  = "0", width = 6, height = 3, command = lambda: button_klick(0))
button0.grid(row = 4, column = 1, sticky = "nsew")

buttonGleich = tk.Button(root, font = "bold", text = "=", width = 6, height = 3, command = button_gleich)
buttonGleich.grid(row = 4, column= 2, sticky = "nsew")

buttonDiv =  tk.Button(root, font = ("Arial", 12, "bold"), text = "/", bg = "#17505E", fg = "white", width = 6, height = 3, command = lambda: button_klick("/"))
buttonDiv.grid(row = 4, column= 3, sticky = "nsew")


root.mainloop()