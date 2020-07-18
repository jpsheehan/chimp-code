from tkinter import *
from tkinter.ttk import *

class GuiCardinalButtonFrame(Frame):
	
	def __init__(self, master=None, title=None, buttons={}):
		super().__init__(master)
		self.master = master
		self.btns =	{}
		self.title = title
		self.create_widgets(buttons)
	
	def get_coordinates(self, direction):
		""" Returns a (row, col) tuple based on a direction string. """
		if direction == "n":
			return (1, 1)
		if direction == "s":
			return (3, 1)
		if direction == "w":
			return (2, 0)
		if direction == "e":
			return (2, 2)
		if direction == "c":
			return (2, 1)
		if direction == "nw":
			return (1, 0)
		if direction == "ne":
			return (1, 2)
		if direction == "sw":
			return (3, 0)
		if direction == "se":
			return (3, 2)

		# otherwise return Nones
		return (None, None)

	def create_widgets(self, buttons):
		
		if self.title:
			self.lbl_title = Label(master=self, text=self.title, font=("Helvetica", 16))
			self.lbl_title.grid(row=0, column=1)
		else:
			self.lbl_title = None

		for direction in buttons.keys():
			data = buttons[direction]

			# ensure that we are only processing keys that are n, s, e, w, c, nw, ne, sw, se
			r, c = self.get_coordinates(direction)
			if r is None or c is None:
				continue

			self.btns[direction] = Button(master=self, text=data["text"])
			self.btns[direction].bind("<Button-1>", data["press"])

			# two optional keys
			if "release" in data:
				self.btns[direction].bind("<ButtonRelease-1>", data["release"])
			if "state" in data:
				self.btns[direction]["state"] = data["state"]

			# place the button at the correct position
			self.btns[direction].grid(row=r, column=c)
			
