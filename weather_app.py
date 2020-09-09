import tkinter as tk
from tkinter import *
import requests
from tkinter.scrolledtext import ScrolledText

def clear():
	viewBox.configure(state=NORMAL)
	viewBox.delete(1.0, END)
	viewBox.configure(state=DISABLED)

def check():
	address = "https://api.openweathermap.org/data/2.5/weather?appid=a5da043b07499da9b964e606695c64e2&q="
	location = loc_ent.get()
	if location == "":
		print("app")
	else:
		try:
			url = address+location
			req = requests.get(url).json()
			weather = req["weather"][0]["main"]
			description = req["weather"][0]["description"]
				
			print(weather)
			viewBox.configure(state=NORMAL)
			viewBox.delete(1.0, END)
			viewBox.insert(END, f"Location: {location}\n\n")
			viewBox.insert(END, f"Temperature: {weather}\n\n")
			viewBox.insert(END, f"Description: {description.title()}\n\n")
			viewBox.configure(state=DISABLED)

			loc_ent.delete(0, END)
		except:
			viewBox.configure(state=NORMAL)
			viewBox.delete(1.0, END)
			viewBox.insert(END, f"Error: Network Error")
			viewBox.configure(state=DISABLED)



root = tk.Tk()
root.title("Weather App")
root.geometry("600x400")
root.configure(bg="#232323")
root.resizable(width=False, height=False)

global loc_ent
global viewBox

f = Frame(bg="#232323")
f.grid(row=1, column=0, pady=20, padx=30)

f1 = Frame(bg="grey")
f1.grid(row=2, column=0, padx=30)

loc_intro = tk.Label(f, text="Location", font=("Comic Sans MS", 16), fg="white", bg="#232323")
loc_intro.grid(row=0, column=0)

loc_ent = tk.Entry(f, width=20, font=("Candara", 15))
loc_ent.grid(row=0, column=1, padx=10)

check_btn = tk.Button(f, text="Check", font=("Candara", 13), fg='white', bg="grey", bd=0, width=10, command=check)
check_btn.grid(row=1, column=1, pady=4)

viewBox = ScrolledText(f1, width=57, height=10, font=("Comic Sans MS", 11), state=DISABLED, bg="grey")
viewBox.grid(row=0, column=0, columnspan=1)

clearBtn = tk.Button(f1, text="Clear", font=("Lucida Sans Unicode", 11, "bold"), bg="#232323", fg="white", width=10, command=clear, bd=1)
clearBtn.grid(row=3, column=0, pady=4)

mainloop()
