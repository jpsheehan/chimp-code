from tkinter import *
from tkinter.ttk import *

from GuiCardinalButtonFrame import GuiCardinalButtonFrame
from ChimpApi import ChimpApi

def nop(event):
	print("NOP", event)
	return None

class GuiControllerFrame(Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		#self.api = ChimpApi("/dev/ttyUSB1")
	
	def create_widgets(self):
		self.lbl_ping = Label(text="??? ms")
		self.lbl_ping.pack()

		self.btn_ping = Button(text="Ping")
		self.btn_ping.bind("<Button-1>", self.handle_ping_press)
		self.btn_ping.pack()

		self.btns_upper_lip = GuiCardinalButtonFrame(master=self, title="Upper Lip", buttons={
			"n": { "text": "Raise", "press": self.handle_upper_lip_up_press, "release":  self.handle_upper_lip_release, "state": "disabled" },
			"s": { "text": "Lower", "press": self.handle_upper_lip_down_press, "release": self.handle_upper_lip_release, "state": "disabled" },
			"c": { "text": "Off", "press": self.handle_upper_lip_release }
		})

		self.btns_eyebrows = GuiCardinalButtonFrame(master=self, title="Eyebrows", buttons={
			"n": { "text": "Raise", "press": self.handle_eyebrows_up_press, "release":  self.handle_eyebrows_release },
			"s": { "text": "Lower", "press": self.handle_eyebrows_down_press, "release": self.handle_eyebrows_release },
			"c": { "text": "Off", "press": self.handle_eyebrows_release }
		})
		
		self.btns_head = GuiCardinalButtonFrame(master=self, title="Head", buttons={
			"n": { "text": "Up", "press": self.handle_head_up_press, "release": self.handle_head_v_release, "state": "disabled" },
			"s": { "text": "Down", "press": self.handle_head_down_press, "release": self.handle_head_v_release, "state": "disabled" },
			"w": { "text": "Left", "press": self.handle_head_left_press, "release": self.handle_head_h_release, "state": "disabled" },
			"e": { "text": "Right", "press": self.handle_head_right_press, "release": self.handle_head_h_release, "state": "disabled" },
			"c": { "text": "Off", "press": self.handle_head_off },
		})

		self.btns_eyes = GuiCardinalButtonFrame(master=self, title="Eyes", buttons={
			"n": { "text": "Up", "press": self.handle_eyes_up_press, "release": self.handle_eyes_v_release, "state": "disabled" },
			"s": { "text": "Down", "press": self.handle_eyes_down_press, "release": self.handle_eyes_v_release, "state": "disabled" },
			"w": { "text": "Left", "press": self.handle_eyes_left_press, "release": self.handle_eyes_h_release },
			"e": { "text": "Right", "press": self.handle_eyes_right_press, "release": self.handle_eyes_h_release },
			"c": { "text": "Off", "press": self.handle_eyes_off }
		})

		self.btns_eyelids = GuiCardinalButtonFrame(master=self, title="Eyelids", buttons={
			"n": { "text": "Open", "press": self.handle_eyelids_open_press, "release": self.handle_eyelids_release },
			"s": { "text": "Close", "press": self.handle_eyelids_close_press, "release": self.handle_eyelids_release },
			"c": { "text": "Off", "press": self.handle_eyelids_release },
		})

		self.btns_jaw = GuiCardinalButtonFrame(master=self, title="Jaw", buttons={
			"n": { "text": "Open", "press": self.handle_jaw_open_press, "release": self.handle_jaw_release },
			"s": { "text": "Close", "press": self.handle_jaw_close_press, "release": self.handle_jaw_release },
			"c": { "text": "Off", "press": self.handle_jaw_release },
		})

		self.btns_head.pack()
		self.btns_eyes.pack()
		self.btns_eyebrows.pack()
		self.btns_eyelids.pack()
		self.btns_upper_lip.pack()
		self.btns_jaw.pack()
	
	def handle_error(self, error):
		print("An error occurred:", error)

	def handle_ping_press(self, ev):
		ok, data = self.api.ping()

		if ok:
			self.lbl_ping["text"] = "{:.1f} ms".format(data)
		else:
			self.lbl_ping["text"] = "error"
	
	### EYELIDS
	def handle_eyelids_open_press(self, ev):
		ok, err = self.api.move_eyelids('open')
		if not ok:
			self.handle_error(err)

	def handle_eyelids_close_press(self, ev):
		ok, err = self.api.move_eyelids('close')
		if not ok:
			self.handle_error(err)

	def handle_eyelids_release(self, ev):
		ok, err = self.api.move_eyelids('none')
		if not ok:
			self.handle_error(err)

	### JAW
	def handle_jaw_open_press(self, ev):
		ok, err = self.api.move_jaw('open')
		if not ok:
			self.handle_error(err)

	def handle_jaw_close_press(self, ev):
		ok, err = self.api.move_jaw('close')
		if not ok:
			self.handle_error(err)

	def handle_jaw_release(self, ev):
		ok, err = self.api.move_jaw('none')
		if not ok:
			self.handle_error(err)

	### UPPER LIP
	def handle_upper_lip_up_press(self, ev):
		ok, err = self.api.move_upper_lip('up')
		if not ok:
			self.handle_error(err)
	
	def handle_upper_lip_down_press(self, ev):
		ok, err = self.api.move_upper_lip('down')
		if not ok:
			self.handle_error(err)
	
	def handle_upper_lip_release(self, ev):
		ok, err = self.api.move_upper_lip('none')
		if not ok:
			self.handle_error(err)

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

