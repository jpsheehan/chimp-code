import serial
import tkinter as tk
import time
from ChimpApi import ChimpApi

class ChimpGui(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		self.api = ChimpApi("/dev/ttyUSB1")
	
	def create_widgets(self):
		self.lbl_ping = tk.Label(text="??? ms")
		self.lbl_ping.pack()

		self.btn_ping = tk.Button(text="Ping")
		self.btn_ping.bind("<Button-1>", self.handle_btn_ping_press)
		self.btn_ping.pack()

		self.btn_eyebrows_up = tk.Button(text="Eyebrows Up")
		self.btn_eyebrows_up.bind("<Button-1>", self.handle_btn_eyebrows_up_press)
		self.btn_eyebrows_up.bind("<ButtonRelease-1>", self.handle_btn_eyebrows_up_release)
		self.btn_eyebrows_up.pack()

		self.btn_eyebrows_down = tk.Button(text="Eyebrows Down")
		self.btn_eyebrows_down.bind("<Button-1>", self.handle_btn_eyebrows_down_press)
		self.btn_eyebrows_down.bind("<ButtonRelease-1>", self.handle_btn_eyebrows_down_release)
		self.btn_eyebrows_down.pack()
	
	def handle_btn_ping_press(self, ev):
		ok, data = self.api.ping()

		if ok:
			self.lbl_ping["text"] = "{:.1f} ms".format(data)
		else:
			self.lbl_ping["text"] = "error"
	
	def handle_btn_eyebrows_up_press(self, ev):
		ok, err = self.api.move_eyebrows('up')

		if not ok:
			pass
	
	def handle_btn_eyebrows_up_release(self, ev):
		ok, err = self.api.move_eyebrows('none')

		if not ok:
			pass

	def handle_btn_eyebrows_down_press(self, ev):
		ok, err = self.api.move_eyebrows('down')

		if not ok:
			pass
	
	def handle_btn_eyebrows_down_release(self, ev):
		ok, err = self.api.move_eyebrows('none')

		if not ok:
			pass

def main():
	window = tk.Tk()
	app = ChimpGui(master=window)
	app.mainloop()

if __name__ == "__main__":
	main()

