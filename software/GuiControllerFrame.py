from tkinter import *
from tkinter.ttk import *
import serial

from GuiCardinalButtonFrame import GuiCardinalButtonFrame
from ChimpApi import ChimpApi

def nop(event):
	print("NOP", event)
	return None

class GuiControllerFrame(Frame):
	
	def __init__(self, master=None, device=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		self.device = device
		self.api = None
		if self.device is not None:
			self.connect_serial(self.device)
	
	def connect_serial(self, device):
		self.device = device
		self.api = ChimpApi(device)

		# hide the disconnected frame
		self.disconnected_frame.pack_forget()

		# show the connected frame
		self.connected_frame.pack()
	
	def disconnect_serial(self):
		if self.api:
			self.api.close()
			self.api = None

		# hide the connected frame
		self.connected_frame.pack_forget()

		# show the disconnected frame
		self.disconnected_frame.pack()

	def create_widgets(self):
		
		self.disconnected_frame = Frame(master=self)
		self.lbl_disconnected = Label(master=self.disconnected_frame, text="Disconnected!", font=("Helvetica", 16, "bold italic"))
		self.lbl_disconnected.pack()

		self.connected_frame = Frame(master=self)
		
		chimp_photo = PhotoImage(file="chimp.png")
		self.img_chimp = Label(master=self.connected_frame, image=chimp_photo)
		self.img_chimp.image = chimp_photo

		self.ping_frame = Frame(master=self.connected_frame)
		
		self.lbl_ping = Label(master=self.ping_frame, text="??? ms")
		self.lbl_ping.pack()

		self.btn_ping = Button(master=self.ping_frame, text="Ping")
		self.btn_ping.bind("<Button-1>", self.handle_ping_press)
		self.btn_ping.pack()

		self.btns_upper_lip = GuiCardinalButtonFrame(master=self.connected_frame, title="Upper Lip", buttons={
			"n": { "text": "Raise", "press": self.handle_upper_lip_up_press, "release":  self.handle_upper_lip_release, "state": "disabled" },
			"s": { "text": "Lower", "press": self.handle_upper_lip_down_press, "release": self.handle_upper_lip_release, "state": "disabled" },
			"c": { "text": "Off", "press": self.handle_upper_lip_release }
		})

		self.btns_eyebrows = GuiCardinalButtonFrame(master=self.connected_frame, title="Eyebrows", buttons={
			"n": { "text": "Raise", "press": self.handle_eyebrows_up_press, "release":  self.handle_eyebrows_release },
			"s": { "text": "Lower", "press": self.handle_eyebrows_down_press, "release": self.handle_eyebrows_release },
			"c": { "text": "Off", "press": self.handle_eyebrows_release }
		})
		
		self.btns_head = GuiCardinalButtonFrame(master=self.connected_frame, title="Head", buttons={
			"n": { "text": "Up", "press": self.handle_head_up_press, "release": self.handle_head_v_release, "state": "disabled" },
			"s": { "text": "Down", "press": self.handle_head_down_press, "release": self.handle_head_v_release, "state": "disabled" },
			"w": { "text": "Left", "press": self.handle_head_left_press, "release": self.handle_head_h_release, "state": "disabled" },
			"e": { "text": "Right", "press": self.handle_head_right_press, "release": self.handle_head_h_release, "state": "disabled" },
			"c": { "text": "Off", "press": self.handle_head_off },
		})

		self.btns_eyes = GuiCardinalButtonFrame(master=self.connected_frame, title="Eyes", buttons={
			"n": { "text": "Up", "press": self.handle_eyes_up_press, "release": self.handle_eyes_v_release, "state": "disabled" },
			"s": { "text": "Down", "press": self.handle_eyes_down_press, "release": self.handle_eyes_v_release, "state": "disabled" },
			"w": { "text": "Left", "press": self.handle_eyes_left_press, "release": self.handle_eyes_h_release },
			"e": { "text": "Right", "press": self.handle_eyes_right_press, "release": self.handle_eyes_h_release },
			"c": { "text": "Off", "press": self.handle_eyes_off }
		})

		self.btns_eyelids = GuiCardinalButtonFrame(master=self.connected_frame, title="Eyelids", buttons={
			"n": { "text": "Open", "press": self.handle_eyelids_open_press, "release": self.handle_eyelids_release },
			"s": { "text": "Close", "press": self.handle_eyelids_close_press, "release": self.handle_eyelids_release },
			"c": { "text": "Off", "press": self.handle_eyelids_release },
		})

		self.btns_jaw = GuiCardinalButtonFrame(master=self.connected_frame, title="Jaw", buttons={
			"n": { "text": "Open", "press": self.handle_jaw_open_press, "release": self.handle_jaw_release },
			"s": { "text": "Close", "press": self.handle_jaw_close_press, "release": self.handle_jaw_release },
			"c": { "text": "Off", "press": self.handle_jaw_release },
		})

		self.btns_head.grid(row=1, column=0, padx=16, pady=16)
		self.btns_eyes.grid(row=1, column=2, padx=16, pady=16)
		self.btns_eyebrows.grid(row=0, column=0, padx=16, pady=16)
		self.btns_eyelids.grid(row=0, column=2, padx=16, pady=16)
		self.btns_upper_lip.grid(row=1, column=1, padx=16, pady=16)
		self.btns_jaw.grid(row=2, column=1, padx=16, pady=16)
		self.img_chimp.grid(row=0, column=1, padx=16, pady=16)
		self.ping_frame.grid(row=2, column=0, padx=16, pady=16)

		self.disconnected_frame.pack()
	
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

