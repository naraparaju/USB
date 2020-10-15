import os
#os.environ['PYUSB_DEBUG'] = 'debug' # uncomment for verbose pyusb output
import sys
import platform
import usb.core
import usb.backend.libusb1

VENDOR_ID = 0x2341 # Arduino ID
PRODUCT_ID = 0x0043 # UNO

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if device is None:
    raise ValueError('Arduino Device not found. Please ensure it is connected to Computer.')
    sys.exit(1)
else:
     print("Device found")

# # Claim interface 0 - this interface provides IN and OUT endpoints to write to and read from
# interface = 0
# if device.is_kernel_driver_active(interface):
#    print("Kernel driver is active")
#    device.detach_kernel_driver(interface)
# device.set_configuration()
# usb.util.claim_interface(device, interface)

# #usb.util.claim_interface(device, 0)

ep = device[0].interfaces()[0].endpoints()[0]
i = device[0].interfaces()[0].bInterfaceNumber
print("Interface:", i)

#device.reset()

if device.is_kernel_driver_active(i):
    print("Kernel Driver is active")
    device.detach_kernel_driver(i)
else:
    print("Kernel Driver not active")

#device.set_configuration()

""" data = read_from_arduino(device, 200) # read from device with a 200 millisecond timeout

if data != None:
    print("Received string: {}".format(data))
    print("Received data as int: {}".format(int(data))) # the returned value is a string - we can convert it to a number (int) if we wish

usb.util.release_interface(device, 0)
device.close()


def read_from_arduino(dev, timeout):
    try:
        data = dev.read(0x81, 64, timeout)
    except usb.core.USBError as e:
        print ("Error reading response: {}".format(e.args))
        return None

    byte_str = ''.join(chr(n) for n in data[1:]) # construct a string out of the read values, starting from the 2nd byte
    result_str = byte_str.split('\x00',1)[0] # remove the trailing null '\x00' characters

    if len(result_str) == 0:
        return None

    return result_str """