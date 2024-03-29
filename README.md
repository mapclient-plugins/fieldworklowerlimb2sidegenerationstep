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

References
----------
Lower limb estimation from sparse landmarks using an articulated shape model.
Zhang et al. Journal of Biomechanics, Volume 49, Issue 16, 3875 - 3881
http://dx.doi.org/10.1016/j.jbiomech.2016.10.021

Requires
--------
- GIAS3: https://github.com/musculoskeletal/gias3
- MAP Client: https://github.com/MusculoskeletalAtlasProject/mapclient

Inputs
------
- **landmarks** [dict] : Dictionary of [landmark names]:[landmark coordinates]

Outputs
-------
- **fieldworkmodeldict** [dict] : A dictionary of customised fieldwork models of
lower limb bones. Dictionary keys are: pelvis, femur-l, femur-r, tibia-l,
tibia-r, fibula-l, fibula-r, patella-l, patella-r.
- **gias-lowerlimb** [GIAS3 LowerLimbAtlas instance]: The customised articulated lower
limb model.

Usage
-----
This step is intended to produce a set of lower limb bone meshes by registering a lower limb shape model to a sparse set of landmarks corresponding to lower limb bony anatomical landmarks. The model can also be manual posed and shape without running any registration.

This step has a workflow-runtime GUI in which the model can be viewed adjusted and registered. The GUI can also be disabled in which case the step will attempt to automatically registered the model to the configured landmarks.

### Landmarks
If the lowerlimb model is being fitted to a set of landmarks, there should be at least 1 input landmark per bone in the lowerlimb model. An ideal minimal set of landmarks should be the left and right anterior superior iliac spines on the pelvis, the midpoint of the left and right posterior superior iliac spines (Sacral), medial and lateral epicondyles for the left and right femur, medial and lateral malleolii for the left and right tibia and fibula. Additional landmarks, particularly on the proximal femur and proximal tibia, should improve bone shape prediction. If the pelvis-LASIS, pelvis-RASIS, and pelvis-Sacral landmarks are among the defined landmarks, the model can be registered fully automatically.

### Registration
In the configuration dialogue (before executing the workflow) or in the runtime GUI in the *Landmarks* tab, select the set of model landmarks to be fitted to their corresponding input landmarks. Before running registration by clicking the *Register* button, a number of registration parameters can be adjusted. See the Configurations and Step GUI sections for details on each parameter.

If the pelvis-LASIS, pelvis-RASIS, and pelvis-Sacral landmarks are among the defined landmarks, click the *Register* button to automatically register the model to the landmarks. If the three pelvis landmarks are not present, coarse manual registration of the model to the target landmarks is required before clicking *Register*.

Once registration is complete, the GUI will unlock and registration errors will be displayed. After registration, the model can be manually adjusted using controls in the _Manual Registration_ tab. To revert the model to its original state, click *Reset*. To output the current model, click *Accept*.

### Manual Registration
The _Manual Registration_ tab allows the model to be translated, rotated, posed, and deformed along its principal components. To produce a model completely manually, adjust the controls in the tab until satisfied, then click *Accept*.

To manually align the model before automatic registration, adjust pelvis translation and rotation to bring the model within ~5 cm of pelvis target landmarks. Joint angles can be adjusted by is usually not necessary if target joint angles are less than 20 degrees from the model. After manual adjustments, open the _Auto Registration_ tab to configure and run auto registration.

To manually adjust the model after auto registration, open the _Manual Registration_ tab after auto registration completes. Click _Accept_ to output the model after manual adjustments.

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
- **3D Scene** : Interactive viewer for the lower limb model and input markers.
    Green markers are the raw marker positions while red markers are those used
    for model fitting and adjusted for marker radius and soft-tissue thickness.
- **Visibles box** : Show or hide the lower limb model and input landmarks in
    the 3D scene.
- **Landmarks tab** : Setup model-target landmarks for automatic registration.
    - Add and remove model-target landmark pairs to be used for model registration. 
        Each entry is a model - target landmark pair. The model landmark should
        be selected from the set of supported landmarks (see Supported Landmarks
        section below).
        The target landmark should be selected from the list of input landmark names.
    - **Marker Radius** : Radius of the markers used for motion capture input landmarks.
        This value is used to correct the input landmark positions to match the
        bone-surface model landmarks.
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
        during registration. It is advisable to perform registration first with 1 PC to encourage pose and size matching, then increasing to  5 PCs to fine tune bone shape.
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
    - **Landmark Error** : Root-mean-squared distance between adjusted target
        landmarks and corresponding fitted model landmarks.
    - **Mahalanobis Distance** : The Mahalanobis distance of the fitted model. Higher values indicates a more unusual shape. Increasing the Mahalanobis Weight should reduce this number. The distance is calculated as sqrt(sum(z_i^2)) where z_i is the number of standard deviations from the mean of the fitted score of the i-th principal component.
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
