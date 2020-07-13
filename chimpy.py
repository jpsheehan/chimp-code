import serial
import tkinter as tk
import time

class Chimp:
	
	def __init__(self, device):
		self.ser = serial.Serial(device, 115200)

	def __del__(self):
		self.ser.close()
	
	def _send(self, b):
		self.ser.write(b)
		res = self.ser.read(3)

		ok = True
		data = None

		# check the command id matches
		if res[0] != b[0]:
			ok = False
			data = ValueError("Command ID doesn't match.")
		elif res[1] != 0x00:
			ok = False
			if res[1] == 0x01:
				data = ValueError("Invalid command sent.")
			elif res[2] == 0x02:
				data = ValueError("Invalid direction sent.")
			else:
				data = ValueError("Unknown error code received.")
		
		return (ok, data)
	
	def reset_all(self):
		return self._send(b'\x20\x00')
	
	def ping(self):
		start = time.time()
		ok, err = self._send(b'\x00\x00')

		end = time.time()
		diff = end - start
		
		if ok:
			return (ok, diff * 1000)
		else:
			return (False, err)

class ChimpGui(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		self.api = Chimp("/dev/ttyUSB1")
	
	def create_widgets(self):
		self.lbl_ping = tk.Label(text="??? ms")
		self.lbl_ping.pack()

		self.btn_ping = tk.Button(text="Ping", command=self.handle_btn_ping)
		self.btn_ping.pack()
	
	def handle_btn_ping(self):
		ok, data = self.api.ping()

		if ok:
			self.lbl_ping["text"] = "{:.1f} ms".format(data)
		else:
			self.lbl_ping["text"] = "error"

def main():
	window = tk.Tk()
	app = ChimpGui(master=window)
	app.mainloop()

if __name__ == "__main__":
	main()

