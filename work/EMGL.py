from dronekit import connect, VehicleMode, Command
from pymavlink import mavutil
import time
import sys

vehicle = connect('tcp:127.0.0.1:5763',wait_ready=True, timeout=60)

vehicle.parameters['SIM_BATT_VOLTAGE']= 11.1

try:
    vehicle.wait_for_armable()
    vehicle.wait_for_mode("GUIDED")
    vehicle.arm()
    time.sleep(1)
    vehicle.wait_simple_takeoff(10, timeout=20)

except TimeoutError as takeoffError:
    print("Takeoff is timeout!!!")
    sys.exit()

print("Starting mission")
# Reset mission set to first (0) waypoint
vehicle.commands.next=0

cmds = vehicle.commands
cmds.clear()
lat1 = 35.8782484
lon1 = 140.3382839
altitude = 30.0
cmds.add(Command(0,0,0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
    0, 0, 0, 0, 0, 0,
    lat1, lon1, altitude))

lat2 = 35.8785484
lon2 = 140.3382539

cmds.add(Command(0,0,0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
    0, 0, 0, 0, 0, 0,
    lat2, lon2, altitude))

#add dummy waypoint "5" at point 4 (lets us know when have reached destination)
cmds.add(Command(0,0,0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
    0, 0, 0, 0, 0, 0,
    lat2, lon2, altitude))

cmds.upload()

print("Starting mission")
# Reset mission set to first (0) waypoint
vehicle.commands.next=0

# Set mode to AUTO to start mission
vehicle.mode = VehicleMode("AUTO")

time.sleep(10)
vehicle.parameters['SIM_BATT_VOLTAGE']= 9.7


