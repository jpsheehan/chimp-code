import serial
import time

RX_PACKET_SIZE = 3
TX_PACKET_SIZE = 2

CMD_PING = 0x00
CMD_MOVE_EYES_H = 0x10
CMD_MOVE_EYES_V = 0x11
CMD_MOVE_EYELIDS = 0x12
CMD_MOVE_EYEBROWS = 0x13
CMD_MOVE_JAW = 0x14
CMD_MOVE_UPPER_LIP = 0x15
CMD_MOVE_HEAD_H = 0x16
CMD_MOVE_HEAD_V = 0x17
CMD_ALL_NEUTRAL = 0x20

DIR_NONE = 0x00
DIR_NEUTRAL = 0x00
DIR_LEFT = 0x01
DIR_RIGHT = 0x02
DIR_UP = 0x01
DIR_DOWN = 0x02
DIR_OPEN = 0x01
DIR_CLOSE = 0x02

class ChimpApi:
	
	def __init__(self, device):
		self.ser = serial.Serial(device, 115200)

	def __del__(self):
		self.ser.close()
	
	def _send(self, command, direction=DIR_NONE):
		self.ser.write(bytes([command, direction]))
		res = self.ser.read(RX_PACKET_SIZE)

		ok = True
		data = None
		
		if res[0] != command: # check the command id matches
			ok = False
			data = ValueError("Command ID doesn't match.")
		elif res[1] != 0x00: # check the status is ok
			ok = False
			if res[1] == 0x01:
				data = ValueError("Invalid command sent.")
			elif res[2] == 0x02:
				data = ValueError("Invalid direction sent.")
			else:
				data = ValueError("Unknown error code received.")
		
		return (ok, data)
	
	def convert_dir(self, dir):
		if dir is None:
			return DIR_NONE
		if type(dir) is str:
			dir = dir.lower()
			if dir == 'none':
				return DIR_NONE
			if dir == 'neutral':
				return DIR_NEUTRAL
			if dir == 'left':
				return DIR_LEFT
			if dir == 'right':
				return DIR_RIGHT
			if dir == 'up':
				return DIR_UP
			if dir == 'down':
				return DIR_DOWN
			if dir == 'open':
				return DIR_OPEN
			if dir == 'close':
				return DIR_CLOSE
			raise ValueError("Invalid direction!")
	
	def reset_all(self):
		return self._send(CMD_ALL_NEUTRAL)
	
	def ping(self):
		start = time.time()
		ok, err = self._send(CMD_PING)

		end = time.time()
		diff = end - start
		
		if ok:
			return (ok, diff * 1000)
		else:
			return (False, err)

	def move_eyes_h(self, dir):
		return self._send(CMD_MOVE_EYES_H, self.convert_dir(dir))
	
	def move_eyes_v(self, dir):
		return self._send(CMD_MOVE_EYES_V, self.convert_dir(dir))
	
	def move_eyelids(self, dir):
		return self._send(CMD_MOVE_EYELIDS, self.convert_dir(dir))
	
	def move_eyebrows(self, dir):
		return self._send(CMD_MOVE_EYEBROWS, self.convert_dir(dir))
	
	def move_jaw(self, dir):
		return self._send(CMD_MOVE_JAW, self.convert_dir(dir))
	
	def move_upper_lip(self, dir):
		return self._send(CMD_MOVE_UPPER_LIP, self.convert_dir(dir))
	
	def move_head_h(self, dir):
		return self._send(CMD_MOVE_HEAD_H, self.convert_dir(dir))
	
	def move_head_v(self, dir):
		return self._send(CMD_MOVE_HEAD_V, self.convert_dir(dir))

