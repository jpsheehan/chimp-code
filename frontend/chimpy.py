from tkinter import *
from tkinter.ttk import *

from GuiControllerFrame import GuiControllerFrame
from GuiInformationFrame import GuiInformationFrame
from GuiSerialPortSelector import GuiSerialPortSelector


class GuiMaster(Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title("Chimpanzee Controller")
		self.master.minsize(800, 600)
		self.master.maxsize(800, 600)
		self.pack(fill=BOTH)
		self.create_widgets()
	
	def create_widgets(self):
		self.lbl_title = Label(master=self, text="Chimpanzee Controller", font=("Helvetica", 24))
		self.lbl_title.pack()

		self.lbl_author = Label(master=self, text="Jesse Sheehan <jps111@uclive.ac.nz>", font=("Helvetica", 12, "italic"))
		self.lbl_author.pack()

		self.serial = GuiSerialPortSelector(master=self, on_connect=self.on_serial_connect, on_disconnect=self.on_serial_disconnect)
		self.serial.pack()

		self.tabs = Notebook(master=self, width=800)

		self.tab_information = GuiInformationFrame(master=self.tabs)
		self.tab_controller = GuiControllerFrame(master=self.tabs)

		self.tabs.add(self.tab_information, text="Information")
		self.tabs.add(self.tab_controller, text="Controller")
		self.tabs.pack()
	
	def on_serial_connect(self, device):
		self.tab_controller.connect_serial(device)
	
	def on_serial_disconnect(self):
		self.tab_controller.disconnect_serial()

def main():
	window = Tk()
	app = GuiMaster(master=window)
	app.mainloop()

if __name__ == "__main__":
	main()

