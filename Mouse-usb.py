import sys
import usb.core

dev = usb.core.find(idVendor=0x046d, idProduct=0xc077)

if dev is None:
    raise ValueError('Mouse Device not found. Please ensure it is connected to the tablet.')
    sys.exit(1)
else:
    print("Mouse Device found")

ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(i) is True:
    dev.detach_kernel_driver(i)
    print("Kernel driver is detached")

# Set the active configuration. With no arguments, the first configuration will be the active one
dev.set_configuration()

# Claim interface 0 - this interface provides IN and OUT endpoints to write to and read from
usb.util.claim_interface(dev, i)

eaddr = ep.bEndpointAddress

r = dev.read(eaddr, 1024)

print("Read:",len(r))

usb.util.release_interface(dev, i)
