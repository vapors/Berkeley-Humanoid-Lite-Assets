# Copyright (c) 2025, The Berkeley Humanoid Lite Project Developers.

import os

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

ISAACLAB_ASSET_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))

LILGREEN_LEG_JOINTS = [
    "leg_left_hip_roll_joint",
    "leg_left_hip_yaw_joint",
    "leg_left_hip_pitch_joint",
    "leg_left_knee_pitch_joint",
    "leg_left_ankle_pitch_joint",
    "leg_left_ankle_roll_joint",
    "leg_left_toe_pitch_joint",
    "leg_right_hip_roll_joint",
    "leg_right_hip_yaw_joint",
    "leg_right_hip_pitch_joint",
    "leg_right_knee_pitch_joint",
    "leg_right_ankle_pitch_joint",
    "leg_right_ankle_roll_joint",
    "leg_right_toe_pitch_joint",
]

LILGREEN_ARM_JOINTS = [
    "arm_left_shoulder_pitch_joint",
    "arm_left_shoulder_roll_joint",
    "arm_left_shoulder_yaw_joint",
    "arm_left_elbow_pitch_joint",
    "arm_left_elbow_roll_joint",
    "arm_right_shoulder_pitch_joint",
    "arm_right_shoulder_roll_joint",
    "arm_right_shoulder_yaw_joint",
    "arm_right_elbow_pitch_joint",
    "arm_right_elbow_roll_joint",
]

#LILGREEN_JOINTS = LILGREEN_ARM_JOINTS + LILGREEN_LEG_JOINTS
LILGREEN_JOINTS = LILGREEN_LEG_JOINTS

LILGREEN_BIPED_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAACLAB_ASSET_DIR}/usd/lilgreen.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=8, solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.0),
        joint_pos={
            "leg_left_hip_roll_joint": 0.0,
            "leg_left_hip_yaw_joint": 0.0,
            "leg_left_hip_pitch_joint": 0.1,
            "leg_left_knee_pitch_joint": -0.5,
            "leg_left_ankle_pitch_joint": 0.5,
            "leg_left_ankle_roll_joint": -0.1,
            "leg_left_toe_pitch_joint": 0.0,
            "leg_right_hip_roll_joint": 0.0,
            "leg_right_hip_yaw_joint": 0.0,
            "leg_right_hip_pitch_joint": 0.1,
            "leg_right_knee_pitch_joint": -0.5,
            "leg_right_ankle_pitch_joint": 0.5,
            "leg_right_ankle_roll_joint": -0.1,
            "leg_right_toe_pitch_joint": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                "leg_.*_hip_yaw_joint",
                "leg_.*_hip_roll_joint",
                "leg_.*_hip_pitch_joint",
                "leg_.*_knee_pitch_joint",
            ],
            effort_limit=6,
            velocity_limit=10.0,
            stiffness=20,
            damping=2,
            armature=0.007,
        ),
        "ankles": ImplicitActuatorCfg(
            joint_names_expr=[
                "leg_.*_ankle_pitch_joint",
                "leg_.*_ankle_roll_joint",
            ],
            effort_limit_sim=6,
            velocity_limit_sim=10.0,
            stiffness=20,
            damping=2,
            armature=0.002,
        ),

        "toes": ImplicitActuatorCfg(
            joint_names_expr=["leg_.*_toe_pitch_joint",],
            effort_limit_sim=0.0001,
            velocity_limit_sim=0.0001,
            stiffness=0.01,
            damping=0.05,
            armature=0.001,
        ),

    },
)
"""Configuration for the Berkeley Humanoid Lite robot in bipedal mode."""

LILGREEN_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAACLAB_ASSET_DIR}/usd/lilgreen.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=8, solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.0),
        joint_pos={
            #"arm_left_shoulder_pitch_joint": 0.0,
            #"arm_left_shoulder_roll_joint": 0.0,
            #"arm_left_shoulder_yaw_joint": 0.0,
            #"arm_left_elbow_pitch_joint": 0.0,
            #"arm_left_elbow_roll_joint": 0.0,
            #"arm_right_shoulder_pitch_joint": 0.0,
            #"arm_right_shoulder_roll_joint": 0.0,
            #"arm_right_shoulder_yaw_joint": 0.0,
            #"arm_right_elbow_pitch_joint": 0.0,
            #"arm_right_elbow_roll_joint": 0.0,
            "leg_left_hip_roll_joint": 0.0,
            "leg_left_hip_yaw_joint": 0.0,
            "leg_left_hip_pitch_joint": 0.1,
            "leg_left_knee_pitch_joint": -0.5,
            "leg_left_ankle_pitch_joint": 0.5,
            "leg_left_ankle_roll_joint": -0.1,
            "leg_left_toe_pitch_joint": 0.0,
            "leg_right_hip_roll_joint": 0.0,
            "leg_right_hip_yaw_joint": 0.0,
            "leg_right_hip_pitch_joint": 0.1,
            "leg_right_knee_pitch_joint": -0.5,
            "leg_right_ankle_pitch_joint": 0.5,
            "leg_right_ankle_roll_joint": -0.1,
            "leg_right_toe_pitch_joint": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        '''
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[
                "arm_.*_shoulder_pitch_joint",
                "arm_.*_shoulder_roll_joint",
                "arm_.*_shoulder_yaw_joint",
                "arm_.*_elbow_pitch_joint",
                "arm_.*_elbow_roll_joint",
            ],
            effort_limit=4,
            velocity_limit=10.0,
            stiffness=10,
            damping=2,
            armature=0.002,
        ),
        '''
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                "leg_.*_hip_yaw_joint",
                "leg_.*_hip_roll_joint",
                "leg_.*_hip_pitch_joint",
                "leg_.*_knee_pitch_joint",
            ],
            effort_limit=6,
            velocity_limit=10.0,
            stiffness=20,
            damping=2,
            armature=0.007,
        ),
        "ankles": ImplicitActuatorCfg(
            joint_names_expr=[
                "leg_.*_ankle_pitch_joint",
                "leg_.*_ankle_roll_joint",
            ],
            effort_limit_sim=6,
            velocity_limit_sim=10.0,
            stiffness=20,
            damping=2,
            armature=0.002,
        ),

        "toes": ImplicitActuatorCfg(
            joint_names_expr=["leg_.*_toe_pitch_joint",],
            effort_limit_sim=0.0001,
            velocity_limit_sim=0.0001,
            stiffness=0.01,
            damping=0.05,
            armature=0.001,
        ),

    },
)
"""Configuration for the Berkeley Humanoid Lite robot."""
