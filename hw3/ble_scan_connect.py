from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n = 0
addr = []

for dev in devices:
    print("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    addr.append(dev.addr)
    n += 1

    for (adtype, desc, value) in dev.getScanData():
        print(" %s = %s" % (desc, value))

number = input('Enter your device number: ')
print('Device', number)
num = int(number)
print(addr[num])

print("Connecting...")
dev = Peripheral(addr[num], 'random')

print("Services...")
for svc in dev.services:
    print(str(svc))

try:
    testService = dev.getServiceByUUID(UUID(0xfff0))
    for ch in testService.getCharacteristics():
        print(str(ch))

    ch = dev.getCharacteristics(uuid=UUID(0xfff1))[0]
    if ch.supportsRead():
        print("Start")
        print(str(ch))
        print(ch.read())
    cccd = ch.getDescriptors(forUUID=0x2902)[0]
    new_cccd_value = bytearray([0x01,0x00])
    cccd_value = cccd.read()
    print("Print CCCD")
    print(cccd_value)
    print("Change CCCD")
    cccd.write(new_cccd_value) 
    cccd_value = cccd.read()
    print("Print Changed CCCD")
    print(cccd_value)

    while True:
        if dev.waitForNotifications(1.0):
            print(ch.read())
            continue
        print("waiting")
        

# Enable notifications (set CCCD to 0x0002)
#cccd = ch.getDescriptors(forUUID=0x2902)[0]  # CCCD UUID
#cccd.write(b'\x02\x00', withResponse=True)

finally:
    dev.disconnect()
