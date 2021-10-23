import csv
import numpy as np
import quaternion
import math
from copy import deepcopy

def main() :
    # fname_sb = '/home/aqua/catkin_ws/src/Aqua/Aqua2021/aqua/entry_point2021/waypoints/2021-10-05-sb10_demo.csv'
    # fname_tc = '/home/aqua/catkin_ws/src/Aqua/Aqua2021/aqua/entry_point2021/waypoints/20211009_tc_waypoints_new.csv'
    # ofname_tc = '/home/aqua/catkin_ws/src/Aqua/Aqua2021/aqua/entry_point2021/waypoints/20211009_tc_waypoints.csv'

    output = []

    with open(fname_tc) as f:
        reader = csv.reader(f)
        for row in reader :
            x = float(row[3])
            y = float(row[4])
            z = float(row[5])
            w = float(row[6])
            quat = np.quaternion(w, x, y, z)
            axis = quaternion.as_rotation_vector(quat)
            axis[1] = 0
            quat_res = quaternion.from_rotation_vector(axis)
            row_output = deepcopy(row)
            row_output[3] = quat_res.x
            row_output[4] = quat_res.y
            row_output[5] = quat_res.z
            row_output[6] = quat_res.w
            output.append(row_output)

    with open(ofname_tc, 'w') as f:
        writer = csv.writer(f) 
        writer.writerows(output)

if __name__=="__main__" :
    main()