import wmi
import time


def list_all_pnp_entities():
    c = wmi.WMI()
    device_ids = []
    for entity in c.Win32_PnPEntity():
        device_ids.append(entity.DeviceID)
        print(f"DeviceID: {entity.DeviceID}, Description: {entity.Description}")
    return device_ids

def disable_usb_device(device_id):
    c = wmi.WMI()
    all_devices = [(device.DeviceID, device.Description) for device in c.Win32_PnPEntity()]
    print("All Devices:")
    for dev_id, desc in all_devices:
        print(f"DeviceID: {dev_id}, Description: {desc}")
    if device_id not in [dev_id for dev_id, _ in all_devices]:
        print(f"DeviceID {device_id} not found in the list of PnP entities")
        return
    print(f"Querying for DeviceID: {device_id}")
    usb_devices = [device for device in c.Win32_PnPEntity() if device.DeviceID.lower() == device_id.lower()]
    print(f"Querying result: {usb_devices}")
    if usb_devices:
        usb_device = usb_devices[0]
        usb_device.Disable()
        print(f"Disabled device with DeviceID: {device_id}")
    else:
        print(f"No USB device found with DeviceID: {device_id}")

def enable_usb_device(device_id):
    c = wmi.WMI()
    usb_devices = [device for device in c.Win32_PnPEntity() if device.DeviceID.lower() == device_id.lower()]
    if usb_devices:
        usb_device = usb_devices[0]
        usb_device.Enable()
    else:
        print(f"No USB device found with DeviceID: {device_id}")

device_ids = list_all_pnp_entities()

# Example usage
device_id = "xx"  # Replace with your Device Instance ID
if device_id in device_ids:
    print(f"Found device with DeviceID: {device_id}")
disable_usb_device(device_id)
time.sleep(5)  # Wait for 5 seconds
enable_usb_device(device_id)
