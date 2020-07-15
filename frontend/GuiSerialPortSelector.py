import serial.tools.list_ports
from tkinter import *
from tkinter.ttk import *

class GuiSerialPortSelector(Frame):
	def __init__(self, master=None, on_connect=None, on_disconnect=None):
		super().__init__(master)
		self.master = master

		self.connected = False
		self.on_connect = on_connect
		self.on_disconnect = on_disconnect
		self.device = None

		self.create_widgets()
		self.handle_refresh_press(None)

	def create_widgets(self):
		self.lbl_hint = Label(master=self, text="Device:")
		self.lbl_hint.pack(side=LEFT)

		self.cmb_devices = Combobox(master=self, state="readonly")
		self.cmb_devices.pack(expand=1, side=LEFT)

		self.btn_refresh = Button(master=self, text="Refresh")
		self.btn_refresh.bind("<Button-1>", self.handle_refresh_press)
		self.btn_refresh.pack(side=LEFT)

		self.btn_connect = Button(master=self, text="Connect")
		self.btn_connect.bind("<Button-1>", self.handle_connect_press)
		self.btn_connect.pack(side=LEFT)

	def handle_refresh_press(self, event):
		available_ports = serial.tools.list_ports.comports()

		if len(available_ports) == 0:
			self.cmb_devices["state"] = "disabled"
			self.cmb_devices.set("No Ports Found")
			self.btn_connect["state"] = "disabled"
		else:
			self.cmb_devices["state"] = "readonly"
			self.cmb_devices["values"] = available_ports
			self.btn_connect["state"] = "normal"
			if self.device is None or self.device not in available_ports:
				self.device = None
				self.cmb_devices.set(available_ports[0])

	
	def handle_connect_press(self, event):
		if self.connected:
			self.connected = False
			self.cmb_devices["state"] = "readonly"
			self.btn_refresh["state"] = "normal"
			self.btn_connect["text"] = "Connect"
			if self.on_disconnect:
				self.on_disconnect()
		else:
			# validate the combobox selection
			device = self.cmb_devices.get()
			self.device = device
			if device:
				# get the proper device identifier
				device = device.split(' ')[0]

				self.connected = True
				self.cmb_devices["state"] = "disabled"
				self.btn_refresh["state"] = "disabled"
				self.btn_connect["text"] = "Disconnect"

				if self.on_connect:
					self.on_connect(device)

