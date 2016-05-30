fieldworklowerlimb2sidegenerationstep
======================================
MAP Client plugin for generating left and right lower limb geometry.

The lower limb model contains the following models:
pelvis, femur-l, femur-r, tibia-l, tibia-r, fibula-l, fibula-r,
patella-l, patella-r.

The articulated model is fitted to mocap landmarks using
a statistical shape model.

Requires
--------
GIAS2: https://bitbucket.org/jangle/gias2,

Inputs
------
landmarks : dict : Dictionary of [marker names]:[marker coordinates]

Outputs
-------
fieldworkmodeldict : dict : A dictionary of customised fieldwork models of
lower limb bones. Dictionary keys are: pelvis, femur-l, femur-r, tibia-l,
tibia-r, fibula-l, fibula-r, patella-l, patella-r.

gias-lowerlimb : LowerLimbAtlas instance : The customised articulated lower
limb model.

Supported Landmarks
-------------------
pelvis-LASIS : pelvis left anterior superior iliac spine
pelvis-LPSIS : pelvis left posterior superior iliac spine
pelvis-LHJC : pelvis left hip joint centre
pelvis-LIS : pelvis left ischial spine 
pelvis-LIT : pelvis left ischial tuberosity
pelvis-LPS : pelvis left pubis symphysis
pelvis-RASIS : pelvis right anterior superior iliac spine
pelvis-RPSIS : pelvis right posterior superior iliac spine
pelvis-RHJC : pelvis right hip joint centre
pelvis-RIS : pelvis right ischial spine 
pelvis-RIT : pelvis right ischial tuberosity
pelvis-RPS : pelvis right pubis symphysis
pelvis-Sacral : pelvis sacral
femur-GT-l : femur left greater trochanter
femur-HC-l : femur left head centre
femur-LEC-l : femur left lateral epicondyle
femur-MEC-l : femur left medial epicondyle
femur-kneecentre-l : femur left knee centre
femur-GT-r : femur right greater trochanter
femur-HC-r : femur right head centre
femur-LEC-r : femur right lateral epicondyle
femur-MEC-r : femur right medial epicondyle
femur-kneecentre-r : femur right knee centre
tibiafibula-LC-l : tibia-fibula left tibia plateau most lateral point
tibiafibula-MC-l : tibia-fibula left tibia plateau most medial point
tibiafibula-LM-l : tibia-fibula left lateral malleolus
tibiafibula-MM-l : tibia-fibula left medial malleolus
tibiafibula-TT-l : tibia-fibula left tibial tuberosity
tibiafibula-LC-r : tibia-fibula right tibia plateau most lateral point
tibiafibula-LM-r : tibia-fibula right tibia plateau most medial point
tibiafibula-MC-r : tibia-fibula right lateral malleolus
tibiafibula-MM-r : tibia-fibula right medial malleolus
tibiafibula-TT-r : tibia-fibula right tibial tuberosity
