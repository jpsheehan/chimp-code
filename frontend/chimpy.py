from tkinter import *
from tkinter.ttk import *

from GuiControllerFrame import GuiControllerFrame
from GuiInformationFrame import GuiInformationFrame

class GuiMaster(Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
	
	def create_widgets(self):
		self.lbl_title = Label(master=self, text="Chimpanzee Controller", font=("Helvetica", 24))
		self.lbl_title.pack()

		self.lbl_author = Label(master=self, text="Jesse Sheehan <jps111@uclive.ac.nz>", font=("Helvetica", 12, "italic"))
		self.lbl_author.pack()

		self.tabs = Notebook(master=self)

		self.tab_information = GuiInformationFrame(master=self.tabs)
		self.tab_controller = GuiControllerFrame(master=self.tabs)

		self.tabs.add(self.tab_information, text="Information")
		self.tabs.add(self.tab_controller, text="Controller")
		self.tabs.pack()

def main():
	window = Tk()
	app = GuiMaster(master=window)
	app.mainloop()

if __name__ == "__main__":
	main()

