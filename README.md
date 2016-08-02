Fieldwork Lowerlimb 2-side Generation Step
===========================================
MAP Client plugin for generating lower-limb bone models using
an articulated shape model.

The articulated model can be automatically registered to landmarks through
shape and pose optimisation to minimise the least squares distance between 
model landmarks and input target landmarks. Alternatively, models can be
manually generated by adjusting principal component weights and joint angles.

The step uses an articulated lower limb shape model containing the pelvis, left
and right femurs, tibias, fibulas, and patellas. The shapes of all bones are
controlled by one PCA-based shape model. The relative orientation of the bones
are controlled by a 6 dof (3 trans, 3 rot) ground-pelvis joint, 2 3-rotational
dof ball-and-socket hip joints, and 2 1-rotational dof knee joints. The 
tibia, fibula, and patella are considered as 1 rigid body. The model will
attempt to maintain a tibio-femoral joint spacing of 5.0 mm at whatever knee
angle to account for cartilage thickness.

Requires
--------
- GIAS2: https://bitbucket.org/jangle/gias2
- MAP Client: https://github.com/MusculoskeletalAtlasProject/mapclient

Inputs
------
- **landmarks** [dict] : Dictionary of [landmark names]:[landmark coordinates]

Outputs
-------
- **fieldworkmodeldict** [dict] : A dictionary of customised fieldwork models of
lower limb bones. Dictionary keys are: pelvis, femur-l, femur-r, tibia-l,
tibia-r, fibula-l, fibula-r, patella-l, patella-r.
- **gias-lowerlimb** [GIAS2 LowerLimbAtlas instance]: The customised articulated lower
limb model.

Configurations
--------------
- **identifier** : Unique name for the step.
- **Registration Mode**: How bone model shapes are adjusted during registration.
    Only shape changes via the shape model is currently supported.
- **PCs to Fit** : Number of principal components to adjust bone shape along 
    during registration. It is advisable to perform registration first with 1
    PC to encourage pose and size matching, then increasing to  5 PCs to fine
    tune bone shape.
- **Mahalanobis Weight** : Weighting on the Mahalanobis distance penalty term
    during registration. Higher weights penalise more against shape far
    from the mean. Value should be between 0.1 and 1.0.
- **Landmarks** : Add and remove model-target landmark pairs to be used for model 
    registration. Each entry is a model - target landmark pair. The model 
    landmark should be selected from the set of supported landmarks (see 
    Supported Landmarks section below). The target landmark should be the 
    exact name of the  corresponding landmark in the input landmark dictionary
    (e.g. marker name from a TRC file).
- **Marker Radius** : Radius of the markers used for motion capture input landmarks.
    This value is used to correct the input landmark positions to match the
    bone-surface model landmarks. If input landmarks are already on the
    bone surface, enter 0.0.
- **Skin Padding** : The soft-tissue thickness between skin surface markers and
    the underlying bone surface. This value is used to correct the input
    landmark positions to match the bone-surface model landmarks. If input
    landmarks are already on the bone surface, enter 0.0.
- **Knee Options** : Optionally turn on abduction/adduction angle adjustment at the
    knee. The _Abd. DOF_ option enables the abduction angle as a degree of 
    freedom in the model registration optimisation. Enabling the option tends
    to improve registration errors. The _Abd. Correction_ option will enable a
    correction of knee abduction to maintain the 5 mm tibio-femoral joint
    spacing for both the medial and lateral compartments of the knee (highly
    experimental, may cause optimisation to become unstable).
- **GUI** : Enable/disable the step GUI during workflow execution.

All options except "identifier" and "GUI" can be adjusted during workflow
execution in the step GUI if the GUI is enabled.


Step GUI
--------
- **Visibles box** : Show or hide the lower limb model and input landmarks in the 3D scene.
- **Landmarks tab** : Setup model-target landmarks for automatic registration.
    - Add and remove model-target landmark pairs to be used for model registration. 
        Each entry is a model - target landmark pair. The model landmark should be selected from the set of supported landmarks (see Supported Landmarks section below).
        The target landmark should be selected from the list of input landmark names.
    - **Marker Radius** : Radius of the markers used for motion capture input landmarks.
        This value is used to correct the input landmark positions to match the bone-surface model landmarks.
        If input landmarks are already on the bone surface, enter 0.0.
    - **Skin Padding** : The soft-tissue thickness between skin surface markers and the underlying bone surface.
        This value is used to correct the input landmark positions to match the bone-surface model landmarks.
        If input landmarks are already on the bone surface, enter 0.0.
- **Manual Registration tab** : Manually adjust model shape and orientation parameters.
    - **Shape Modes** : Adjust the weight of the first four principal components.
        The values are the standard deviations from the mean along each principal component.
    - **Pelvis Trans.** : Translation of the pelvis in the x, y, and z global axes. 
    - **Pelvis Rot.** : Rotation of the pelvis about the pelvis anatomic centre in the x, y, and z pelvis axes. 
    - **Hip, Knee Rot** : Hip and knee joint angles in their x, y, and z joint axes.
    - **Reset** : reset principal component weights and all rotations and translations to 0.
    - **Accept** : Finish execution of the step and output the currently configured model.
- **Auto Registration tab** : Configure and run automatic model registration to landmarks. 
    - **Registration Mode**: How bone model shapes are adjusted during registration.
        Only shape changes via the shape model is currently supported.
    - **PCs to Fit** : Number of principal components to adjust bone shape along 
        during registration.
    - **Mahalanobis Weight** : Weighting on the Mahalanobis distance penalty term
        during registration. Higher weights penalise more against shape far
        from the mean. Value should be between 0.1 and 1.0.
    - **Correct Knee Abd** : enable a correction of knee abduction to maintain the 5 mm tibio-femoral joint spacing for both the medial and lateral compartments of the knee (highly
        experimental).
    - **Fit Knee Abd** : enables the abduction angle as a degree of freedom in the model registration optimisation.
        Enabling the option tends to improve registration errors.
    - **Register** : Run model registration.
    - **Reset** : Reset principal component weights and all rotations and translations to 0.
    - **Abort** : Abort the workflow.
    - **Accept** : Finish execution of the step and output the currently configured model.
- **Screenshots tab** : Save a screenshot of the current 3-D scene to file.
    - **Pixels X** : Width in pixels of the output image.
    - **Pixels Y** : Height in pixels of the output image.
    - **Filename** : Path of the output image file. File format is defined by the suffix of the given filename.
    - **Save Screenshot** : Take screenshot and write to file.

Supported Landmarks
-------------------
- pelvis-LASIS : pelvis left anterior superior iliac spine
- pelvis-LPSIS : pelvis left posterior superior iliac spine
- pelvis-LHJC : pelvis left hip joint centre
- pelvis-LIS : pelvis left ischial spine 
- pelvis-LIT : pelvis left ischial tuberosity
- pelvis-LPS : pelvis left pubis symphysis
- pelvis-RASIS : pelvis right anterior superior iliac spine
- pelvis-RPSIS : pelvis right posterior superior iliac spine
- pelvis-RHJC : pelvis right hip joint centre
- pelvis-RIS : pelvis right ischial spine 
- pelvis-RIT : pelvis right ischial tuberosity
- pelvis-RPS : pelvis right pubis symphysis
- pelvis-Sacral : pelvis sacral
- femur-GT-l : femur left greater trochanter
- femur-HC-l : femur left head centre
- femur-LEC-l : femur left lateral epicondyle
- femur-MEC-l : femur left medial epicondyle
- femur-kneecentre-l : femur left knee centre
- femur-GT-r : femur right greater trochanter
- femur-HC-r : femur right head centre
- femur-LEC-r : femur right lateral epicondyle
- femur-MEC-r : femur right medial epicondyle
- femur-kneecentre-r : femur right knee centre
- tibiafibula-LC-l : tibia-fibula left tibia plateau most lateral point
- tibiafibula-MC-l : tibia-fibula left tibia plateau most medial point
- tibiafibula-LM-l : tibia-fibula left lateral malleolus
- tibiafibula-MM-l : tibia-fibula left medial malleolus
- tibiafibula-TT-l : tibia-fibula left tibial tuberosity
- tibiafibula-LC-r : tibia-fibula right tibia plateau most lateral point
- tibiafibula-LM-r : tibia-fibula right tibia plateau most medial point
- tibiafibula-MC-r : tibia-fibula right lateral malleolus
- tibiafibula-MM-r : tibia-fibula right medial malleolus
- tibiafibula-TT-r : tibia-fibula right tibial tuberosity

Todo List
---------
- Linear scaling as alternative to shape-model-based shape changes
