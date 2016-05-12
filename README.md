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
landmarks : dict

    Dictionary of marker names : marker coordinates

Outputs
-------
fieldworkmodeldict : dict
    
    A dictionary of customised fieldwork models of lower limb bones.
    Dictionary keys are: pelvis, femur-l, femur-r, tibia-l, tibia-r,
    fibula-l, fibula-r, patella-l, patella-r.

gias-lowerlimb : LowerLimbAtlas instance
    
    The customised articulated lower limb model