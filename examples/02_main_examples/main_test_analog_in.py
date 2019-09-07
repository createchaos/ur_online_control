from __future__ import print_function
import time
import sys
import os
 # set the paths to find library
path = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
sys.path.append(path)

import ur_online_control.communication.container as container
from ur_online_control.communication.server import Server
from ur_online_control.communication.client_wrapper import ClientWrapper
from ur_online_control.communication.formatting import format_commands


 if len(sys.argv) > 1:
    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    ur_ip = sys.argv[3]
    print(sys.argv)
else:
    server_address = "192.168.10.1"
    server_port = 30003
    ur_ip = "192.168.10.13"
 def main():
     # start the server
    server = Server(server_address, server_port)
    server.start()
    server.client_ips.update({"UR": ur_ip})

    ur = ClientWrapper("UR")
    ur.wait_for_connected()

    for i in range(100):

        analog_in = ur.wait_for_current_analog_in(1)
        print("analog_in", analog_in)
        # also working:
        #digital_in = ur.wait_for_current_digital_in(1)
        #print("digital_in", digital_in)
        #current_pose_joint = ur.wait_for_current_pose_joint()
        #print("current_pose_joint", current_pose_joint)
        #current_pose_cartesian = ur.wait_for_current_pose_cartesian()
        #print("current_pose_cartesian", current_pose_cartesian)
        time.sleep(0.5)
        print("============================================================")

    ur.quit()
    server.close()
    print("Please press a key to terminate the program.")
    junk = sys.stdin.readline()
    print("Done.")

 if __name__ == "__main__":
    main()
