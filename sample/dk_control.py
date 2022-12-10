from dronekit import connect, VehicleMode, LocationGlobalRelative

vehicle = connect('tcp:127.0.0.1:5763',wait_ready=True, timeout=60)


#モードはGUIDED
vehicle.mode = VehicleMode("GUIDED")

#目標の緯度・経度、高度を設定する
aLocation = LocationGlobalRelative(35.8783452, 140.3384972, 20)

#simple_gotoを実行する
vehicle.simple_goto(aLocation, groundspeed=1000, airspeed=1000)