import serial
import tkinter as tk
import time
from ChimpApi import ChimpApi

class CardinalButtonPanel(tk.Frame):
	
	def __init__(self, master=None, title=None, buttons={}):
		super().__init__(master, relief=tk.RAISED)
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
			self.lbl_title = tk.Label(master=self, text=self.title, font=("Helvetica", 16))
			self.lbl_title.grid(row=0, column=1)
		else:
			self.lbl_title = None

		for direction in buttons.keys():
			data = buttons[direction]

			# ensure that we are only processing keys that are n, s, e, w, c, nw, ne, sw, se
			r, c = self.get_coordinates(direction)
			if r is None or c is None:
				continue

			self.btns[direction] = tk.Button(master=self, text=data["text"])
			self.btns[direction].bind("<Button-1>", data["press"])

			# two optional keys
			if "release" in data:
				self.btns[direction].bind("<ButtonRelease-1>", data["release"])
			if "state" in data:
				self.btns[direction]["state"] = data["state"]

			# place the button at the correct position
			self.btns[direction].grid(row=r, column=c)
			
def nop(event):
	print("NOP", event)
	return None

class ChimpGui(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		# self.api = ChimpApi("/dev/ttyUSB1")
	
	def create_widgets(self):
		self.lbl_ping = tk.Label(text="??? ms")
		self.lbl_ping.pack()

		self.btn_ping = tk.Button(text="Ping")
		self.btn_ping.bind("<Button-1>", self.handle_ping_press)
		self.btn_ping.pack()

		self.btns_eyebrows = CardinalButtonPanel(master=self, title="Eyebrows", buttons={
			"n": { "text": "Raise", "press": self.handle_eyebrows_up_press, "release":  self.handle_eyebrows_release },
			"s": { "text": "Lower", "press": self.handle_eyebrows_down_press, "release": self.handle_eyebrows_release },
			"c": { "text": "Off", "press": self.handle_eyebrows_off }
		})
		
		self.btns_head = CardinalButtonPanel(master=self, title="Head", buttons={
			"n": { "text": "Up", "press": self.handle_head_up_press, "release": self.handle_head_v_release, "state": "disabled" },
			"s": { "text": "Down", "press": self.handle_head_down_press, "release": self.handle_head_v_release, "state": "disabled" },
			"w": { "text": "Left", "press": self.handle_head_left_press, "release": self.handle_head_h_release, "state": "disabled" },
			"e": { "text": "Right", "press": self.handle_head_right_press, "release": self.handle_head_h_release, "state": "disabled" },
			"c": { "text": "Off", "press": self.handle_head_off },
		})

		self.btns_eyes = CardinalButtonPanel(master=self, title="Eyes", buttons={
			"n": { "text": "Up", "press": self.handle_eyes_up_press, "release": self.handle_eyes_v_release, "state": "disabled" },
			"s": { "text": "Down", "press": self.handle_eyes_down_press, "release": self.handle_eyes_v_release, "state": "disabled" },
			"w": { "text": "Left", "press": self.handle_eyes_left_press, "release": self.handle_eyes_h_release },
			"e": { "text": "Right", "press": self.handle_eyes_right_press, "release": self.handle_eyes_h_release },
			"c": { "text": "Off", "press": self.handle_eyes_off }
		})

		self.btns_head.pack()
		self.btns_eyes.pack()
		self.btns_eyebrows.pack()
	
	def handle_error(self, error):
		print("An error occurred:", error)

	def handle_ping_press(self, ev):
		ok, data = self.api.ping()

		if ok:
			self.lbl_ping["text"] = "{:.1f} ms".format(data)
		else:
			self.lbl_ping["text"] = "error"
	
	### EYEBROWS
	def handle_eyebrows_up_press(self, ev):
		ok, err = self.api.move_eyebrows('up')
		if not ok:
			self.handle_error(err)
	
	def handle_eyebrows_down_press(self, ev):
		ok, err = self.api.move_eyebrows('down')
		if not ok:
			self.handle_error(err)
	
	def handle_eyebrows_release(self, ev):
		ok, err = self.api.move_eyebrows('none')
		if not ok:
			self.handle_error(err)

	def handle_eyebrows_off(self, ev):
		self.handle_eyebrows_release(ev)

	### EYES VERTICAL
	def handle_eyes_up_press(self, ev):
		ok, err = self.api.move_eyes_v('up')
		if not ok:
			self.handle_error(err)

	def handle_eyes_down_press(self, ev):
		ok, err = self.api.move_eyes_v('down')
		if not ok:
			self.handle_error(err)

	def handle_eyes_v_release(self, ev):
		ok, err = self.api.move_eyes_v('none')
		if not ok:
			self.handle_error(err)

	### EYES HORIZONTAL
	def handle_eyes_left_press(self, ev):
		ok, err = self.api.move_eyes_h('left')
		if not ok:
			self.handle_error(err)

	def handle_eyes_right_press(self, ev):
		ok, err = self.api.move_eyes_h('right')
		if not ok:
			self.handle_error(err)

	def handle_eyes_h_release(self, ev):
		ok, err = self.api.move_eyes_h('none')
		if not ok:
			self.handle_error(err)

	def handle_eyes_off(self, ev):
		self.handle_eyes_h_release(ev)
		self.handle_eyes_v_release(ev)

	### HEAD VERTICAL
	def handle_head_up_press(self, ev):
		ok, err = self.api.move_head_v('up')
		if not ok:
			self.handle_error(err)

	def handle_head_down_press(self, ev):
		ok, err = self.api.move_head_v('down')
		if not ok:
			self.handle_error(err)

	def handle_head_v_release(self, ev):
		ok, err = self.api.move_head_v('none')
		if not ok:
			self.handle_error(err)

	### HEAD HORIZONTAL
	def handle_head_left_press(self, ev):
		ok, err = self.api.move_head_h('left')
		if not ok:
			self.handle_error(err)

	def handle_head_right_press(self, ev):
		ok, err = self.api.move_head_h('right')
		if not ok:
			self.handle_error(err)

	def handle_head_h_release(self, ev):
		ok, err = self.api.move_head_h('none')
		if not ok:
			self.handle_error(err)

	def handle_head_off(self, ev):
		self.handle_head_h_release(ev)
		self.handle_head_v_release(ev)


def main():
	window = tk.Tk()
	app = ChimpGui(master=window)
	app.mainloop()

if __name__ == "__main__":
	main()

