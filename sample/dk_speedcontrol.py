import math
import time
from dronekit import connect

vehicle = connect('tcp:127.0.0.1:5762',wait_ready=True, timeout=60)

def to_quaternion(roll = 0.0, pitch = 0.0, yaw = 0.0):
    """
    Convert degrees to quaternions
    """
    t0 = math.cos(math.radians(yaw * 0.5))
    t1 = math.sin(math.radians(yaw * 0.5))
    t2 = math.cos(math.radians(roll * 0.5))
    t3 = math.sin(math.radians(roll * 0.5))
    t4 = math.cos(math.radians(pitch * 0.5))
    t5 = math.sin(math.radians(pitch * 0.5))

    w = t0 * t2 * t4 + t1 * t3 * t5
    x = t0 * t3 * t4 - t1 * t2 * t5
    y = t0 * t2 * t5 + t1 * t3 * t4
    z = t1 * t2 * t4 - t0 * t3 * t5

    return [w, x, y, z]

#MAVLinkメッセージを生成する
msg = vehicle.message_factory.set_position_target_local_ned_encode(
    0, #ブートからの時間（今回は未使用）
    0, 0, #ターゲットシステム、コンポーネント
    mavutil.mavlink.MAV_FRAME_LOCAL_NED, #フレーム
    0b0000111111000111, # タイプマスク、0：有効、1：無効
    0, 0, 0, # x、y、z位置（今回は未使用）
    1.0, 1.0, -0.2, # 速度 m/s
    0, 0, 0, #x、y、z加速度（未サポート）
    0, 0) #ヨー、ヨーレート
#MAVLinkメッセージ送信
for x in range(0, 100):
    vehicle.send_mavlink(msg)
    time.sleep(1)
