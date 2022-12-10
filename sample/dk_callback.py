from dronekit import connect, VehicleMode
import time
import sys

vehicle = connect('tcp:127.0.0.1:5763',wait_ready=True, timeout=60)

@vehicle.parameters.on_attribute('RTL_ALT')
def location_callback(self, attr_name, value):
    print("PARAMETER CALLBACK: %s change to %s", (attr_name, value))

# vehicle.add_attribute_listener('location.global_frame', location_callback)

time.sleep(10)

# vehicle.remove_attribute_listener('location.global_frame', location_callback)
