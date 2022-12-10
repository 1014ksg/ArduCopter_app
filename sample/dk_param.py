from dronekit import connect, VehicleMode
import time
import sys

vehicle = connect('tcp:127.0.0.1:5762',wait_ready=True, timeout=60)

print('変更前：%s' % vehicle.parameters['RTL_ALT'])

vehicle.parameters['RTL_ALT'] = 500

print('変更後：%s' % vehicle.parameters['RTL_ALT'])


