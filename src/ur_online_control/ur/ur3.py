from __future__ import print_function

import math

# from compas_fab import get_data
from compas_fab import get

from compas_fab.robots import Configuration
from .ur import UR


class UR3(UR):
    """The UR 3 robot class.

    Manual link:
    #define UR5_PARAMS
    https://github.com/ros-industrial/universal_robot/blob/kinetic-devel/ur_kinematics/src/ur_kin.cpp
    but in mm, not in m
    """

    # define UR3_PARAMS
    d1 = 151.9
    a2 = -243.65
    a3 = -213.25
    d4 = 112.35
    d5 = 85.35
    d6 = 81.9

    shoulder_offset = 119.85
    elbow_offset = -92.87

    # The UR has a very simple workspace definition: it is s sphere with a
    # cylinder in the center cut off. The axis of this cylinder is j0, the
    # diameter is defined below. For more info: UR manual.
    working_area_sphere_diameter = 1850.  # max. working area diameter, recommended 1700
    working_area_cylinder_diameter = 149.

    print("yes yes yes")

    def __init__(self):
        super(UR3, self).__init__()

    def get_model_path(self):
        return get_data("robots/ur/ur5")

    def forward_kinematics(self, configuration):
        q = configuration.values[:]
        q[5] += math.pi
        return super(UR3, self).forward_kinematics(Configuration.from_revolute_values(q))

    def inverse_kinematics(self, tool0_frame_RCS):
        configurations = super(UR3, self).inverse_kinematics(tool0_frame_RCS)
        for q in configurations:
            print(q)
        for i in range(len(configurations)):
            configurations[i].values[5] -= math.pi
        return configurations


if __name__ == "__main__":

    import math
    from compas_fab.utilities import sign
    from compas.geometry import Frame
    from .kinematics import format_joint_positions
    ur = UR3()

    q = [-0.44244, -1.5318, 1.34588, -1.38512, -1.05009, -0.4495]
    q = Configuration.from_revolute_values(q)
    Ts = ur.get_forward_transformations(q)
    for T in Ts:
        print(T)
        print()
    frame = ur.forward_kinematics(q)
    qsols = ur.inverse_kinematics(frame)
    for q in qsols:
        print(q)
    ur.get_transformed_model(Ts)
