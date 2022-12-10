from dronekit import connect, VehicleMode

vehicle = connect('tcp:127.0.0.1:5762',wait_ready=True, timeout=60)

#vehicle.home_locationに値がセットされるまで
#dowloadを繰り返し実行する
while not vehicle.home_location:
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()
    
    if not vehicle.home_location:
        print("Waiting for home location …")
        
#ホームロケーションの取得完了
print("Home location: %s " % vehicle.home_location)