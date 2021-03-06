# -*- coding: UTF-8 -*-

import olympe
import time
import opencv
from olympe.messages.ardrone3.Piloting import TakeOff, Landing

# DRONE_IP = "192.168.42.1" # Real drone IP address
DRONE_IP = "10.202.0.1" # Simulated drone IP address


def main():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    assert drone(TakeOff()).wait().success()
    time.sleep(10)
    assert drone(Landing()).wait().success()
    drone.disconnect()


if __name__ == "__main__":
    main()
