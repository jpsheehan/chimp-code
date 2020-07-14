import tkinter as tk

class GuiInformationFrame(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
	
	def create_widgets(self):
		self.lbl_title = tk.Label(master=self, text="Chimpanzee Overview", font=("Helvetica", 24))
		self.lbl_title.pack()
		
		self.lbl_author = tk.Label(master=self, text="By Jesse Sheehan <jps111@uclive.ac.nz>")
		self.lbl_author.pack()

		self.lbl_background_title = tk.Label(master=self, text="Background", font=("Helvetica", 16))
		self.lbl_background_title.pack()

		self.lbl_background_info = tk.Label(master=self, text="...")
		self.lbl_background_info.pack()

		self.lbl_firmware_title = tk.Label(master=self, text="Firmware", font=("Helvetica", 16))
		self.lbl_firmware_title.pack()

		self.lbl_firmware_info = tk.Label(master=self, text="...")
		self.lbl_firmware_info.pack()

		self.lbl_software_title = tk.Label(master=self, text="Software", font=("Helvetica", 16))
		self.lbl_software_title.pack()

		self.lbl_software_info = tk.Label(master=self, text="...")
		self.lbl_software_info.pack()

		self.lbl_issues_title = tk.Label(master=self, text="Known Issues", fg="red", font=("Helvetica", 16))
		self.lbl_issues_title.pack()

		self.lbl_issues_info = tk.Label(master=self, text="""The hardware to drive the motors consists of several H-Bridges made from P-FET and N-FET transistors.
However, some of these transistors have suffered from damage due to overcurrent.
Because of this, the H-Bridges for the head yaw, head pitch, upper lip movement, and vertical eye movement are not operational.""")
		self.lbl_issues_info.pack()
