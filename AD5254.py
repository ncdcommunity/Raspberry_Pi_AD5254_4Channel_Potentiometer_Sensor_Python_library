# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# AD5254
# This code is designed to work with the AD5254_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Potentiometers?sku=AD5254_I2CPOT_10K#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# I2C address of the device
AD5254_DEFAULT_ADDRESS				= 0x2C

# AD5254 Command Set
AD5254_WORD_RDAC0_EEMEM0			= 0x00 # Store RDAC0 setting to EEMEM0
AD5254_WORD_RDAC1_EEMEM1			= 0x01 # Store RDAC1 setting to EEMEM1
AD5254_WORD_RDAC2_EEMEM2			= 0x02 # Store RDAC2 setting to EEMEM2
AD5254_WORD_RDAC3_EEMEM3			= 0x03 # Store RDAC3 setting to EEMEM3
AD5254_WORD_STORE_EEMEM4			= 0x04 # Store user data to EEMEM4
AD5254_WORD_STORE_EEMEM5			= 0x05 # Store user data to EEMEM5
AD5254_WORD_STORE_EEMEM6			= 0x06 # Store user data to EEMEM6
AD5254_WORD_STORE_EEMEM7			= 0x07 # Store user data to EEMEM7
AD5254_WORD_STORE_EEMEM8			= 0x08 # Store user data to EEMEM8
AD5254_WORD_STORE_EEMEM9			= 0x09 # Store user data to EEMEM9
AD5254_WORD_STORE_EEMEM10			= 0x0A # Store user data to EEMEM10
AD5254_WORD_STORE_EEMEM11			= 0x0B # Store user data to EEMEM11
AD5254_WORD_STORE_EEMEM12			= 0x0C # Store user data to EEMEM12
AD5254_WORD_STORE_EEMEM13			= 0x0D # Store user data to EEMEM13
AD5254_WORD_STORE_EEMEM14			= 0x0E # Store user data to EEMEM14
AD5254_WORD_STORE_EEMEM15			= 0x0F # Store user data to EEMEM15

class AD5254():
	def set_channel(self):
		"""Select the Channel user want to use from 0-3"""
		self.channel = int(input("Enter the Channel No. = "))
		if self.channel > 3 :
			self.channel = int(input("Enter the Channel No. = "))
		
		return self.channel
	
	def set_resistance(self):
		"""Enter the value from 0-256 position for channel"""
		self.resistance = int(input("Enter the Value from (0-256)= "))
		if self.resistance > 256 :
			self.resistance = int(input("Enter the Value from (0-256)= "))
		
		return self.resistance
	
	def write_resistance(self):
		if self.channel == 0 :
			bus.write_i2c_block_data(AD5254_DEFAULT_ADDRESS, AD5254_WORD_RDAC0_EEMEM0, [self.resistance])
		elif self.channel == 1 :
			bus.write_i2c_block_data(AD5254_DEFAULT_ADDRESS, AD5254_WORD_RDAC1_EEMEM1, [self.resistance])
		elif self.channel == 2 :
			bus.write_i2c_block_data(AD5254_DEFAULT_ADDRESS, AD5254_WORD_RDAC2_EEMEM2, [self.resistance])
		elif self.channel == 3 :
			bus.write_i2c_block_data(AD5254_DEFAULT_ADDRESS, AD5254_WORD_RDAC3_EEMEM3, [self.resistance])
		
	
	def get_resistance(self):
		"""Read data back from AD5254_WORD_RDACx_EEMEMx, 1 byte"""
		if self.channel == 0 :
			data = bus.read_byte_data(AD5254_DEFAULT_ADDRESS, AD5254_WORD_RDAC0_EEMEM0)
		elif self.channel == 1 :
			data = bus.read_byte_data(AD5254_DEFAULT_ADDRESS, AD5254_WORD_RDAC1_EEMEM1)
		elif self.channel == 2 :
			data = bus.read_byte_data(AD5254_DEFAULT_ADDRESS, AD5254_WORD_RDAC2_EEMEM2)
		elif self.channel == 3 :
			data = bus.read_byte_data(AD5254_DEFAULT_ADDRESS, AD5254_WORD_RDAC3_EEMEM3)
		
		# Convert the data
		resistance_wb = (data / 256.0) * 1.0 + 0.075
		resistance_wa = 1.0 - resistance_wb
		
		return {'a' : resistance_wa, 'b' : resistance_wb}

from AD5254 import AD5254
ad5254 = AD5254()

while True:
	ad5254.set_channel()
	ad5254.set_resistance()
	ad5254.write_resistance()
	ad5254.get_resistance()
	res = ad5254.get_resistance()
	print "Resistance at WB: %.2f K"%(res['b'])
	print "Resistance at WA: %.2f K"%(res['a'])
	print " ******************************** "
	time.sleep(1)
