import tkinter as tk

from GuiControllerFrame import GuiControllerFrame
from GuiInformationFrame import GuiInformationFrame

def main():
	window = tk.Tk()
	app = GuiControllerFrame(master=window)
	app.mainloop()

if __name__ == "__main__":
	main()

