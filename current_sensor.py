from ina219 import INA219
from ina219 import DeviceRangeError
import ambient
from machine import I2C, Pin
import utime

#INA219 config
I2C_INTERFACE_NO = 0
SHUNT_OHMS = 0.1  # Check value of shunt used with your INA219
MAX_EXPECTED_AMPS = 1

ina = INA219(SHUNT_OHMS, I2C(I2C_INTERFACE_NO), MAX_EXPECTED_AMPS)

ina.configure(ina.RANGE_16V)

#Ambient config
WRITEKEY = '36424e868ea87d98'
am = ambient.Ambient(45401, WRITEKEY)

print("Bus Voltage: %.3f V" % ina.voltage())
while True:
    try:
        print("Bus Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())

        r = am.send({'d1': ina.current(), 'd2': ina.power(), 'd3': ina.shunt_voltage()})
        r.close()
    except DeviceRangeError as e:
        print("Current overflow")
    utime.sleep(0.01)