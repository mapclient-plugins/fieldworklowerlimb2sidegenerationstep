"""
Auto lower limb registration
"""
import os
import numpy as np
import copy

from gias3.musculoskeletal import mocap_landmark_preprocess
from gias3.musculoskeletal.bonemodels import lowerlimbatlasfit2side
from gias3.musculoskeletal.bonemodels import lowerlimbatlas


validModelLandmarks = (
    'femur-GT-l',
    'femur-GT-r',
    'femur-HC-l',
    'femur-HC-r',
    'femur-LEC-l',
    'femur-LEC-r',
    'femur-MEC-l',
    'femur-MEC-r',
    'femur-kneecentre-l',
    'femur-kneecentre-r',
    'pelvis-LASIS',
    'pelvis-LHJC',
    'pelvis-LIS',
    'pelvis-LIT',
    'pelvis-LPS',
    'pelvis-LPSIS',
    'pelvis-RASIS',
    'pelvis-RHJC',
    'pelvis-RIS',
    'pelvis-RIT',
    'pelvis-RPS',
    'pelvis-RPSIS',
    'pelvis-Sacral',
    'tibiafibula-LC-l',
    'tibiafibula-LC-r',
    'tibiafibula-LM-l',
    'tibiafibula-LM-r',
    'tibiafibula-MC-l',
    'tibiafibula-MC-r',
    'tibiafibula-MM-l',
    'tibiafibula-MM-r',
    'tibiafibula-TT-l',
    'tibiafibula-TT-r',
)

SELF_DIRECTORY = os.path.split(__file__)[0]

PELVIS_SUBMESHES = ('RH', 'LH', 'sac')
PELVIS_SUBMESH_ELEMS = {
    'RH': list(range(0, 73)),
    'LH': list(range(73, 146)),
    'sac': list(range(146, 260)),
}
PELVIS_BASISTYPES = {'tri10': 'simplex_L3_L3', 'quad44': 'quad_L3_L3'}

TIBFIB_SUBMESHES = ('tibia', 'fibula')
TIBFIB_SUBMESH_ELEMS = {
    'tibia': list(range(0, 46)),
    'fibula': list(range(46, 88)),
}
TIBFIB_BASISTYPES = {'tri10': 'simplex_L3_L3', 'quad44': 'quad_L3_L3'}


class LLStepData(object):
    _shapeModelFilenameRight = os.path.join(SELF_DIRECTORY, 'data/shape_models/LLP26_right_mirrored_from_left_rigid.pc')
    _boneModelFilenamesRight = {
        'pelvis': (
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/pelvis_combined_cubic_mean_rigid_LLP26.geof'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/pelvis_combined_cubic_flat.ens'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/pelvis_combined_cubic_flat.mesh'),
        ),
        'femur': (
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/femur_right_mirrored_from_left_mean_rigid_LLP26.geof'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/femur_right_quartic_flat.ens'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/femur_right_quartic_flat.mesh'),
        ),
        'patella': (
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/patella_right_mirrored_from_left_mean_rigid_LLP26.geof'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/patella_11_right.ens'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/patella_11_right.mesh'),
        ),
        'tibiafibula': (
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/tibia_fibula_cubic_right_mirrored_from_left_mean_rigid_LLP26.geof'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/tibia_fibula_right_cubic_flat.ens'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/tibia_fibula_right_cubic_flat.mesh'),
        ),
    }
    _shapeModelFilenameLeft = os.path.join(SELF_DIRECTORY, 'data/shape_models/LLP26_rigid.pc')
    _boneModelFilenamesLeft = {
        'pelvis': (
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/pelvis_combined_cubic_mean_rigid_LLP26.geof'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/pelvis_combined_cubic_flat.ens'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/pelvis_combined_cubic_flat.mesh'),
        ),
        'femur': (
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/femur_left_mean_rigid_LLP26.geof'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/femur_left_quartic_flat.ens'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/femur_left_quartic_flat.mesh'),
        ),
        'patella': (
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/patella_left_mean_rigid_LLP26.geof'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/patella_11_left.ens'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/patella_11_left.mesh'),
        ),
        'tibiafibula': (
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/tibia_fibula_cubic_left_mean_rigid_LLP26.geof'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/tibia_fibula_left_cubic_flat.ens'),
            os.path.join(SELF_DIRECTORY, 'data/atlas_meshes/tibia_fibula_left_cubic_flat.mesh'),
        ),
    }
    _validRegistrationModes = ('shapemodel',)
    minArgs = {
        'method': 'BFGS',
        'jac': False,
        'bounds': None, 'tol': 1e-6,
        'options': {'eps': 1e-5},
    }

    def __init__(self, config):
        """
        example config
        config['identifier'] = ''
        config['GUI'] = 'True'
        config['registration_mode'] = 'shapemodel'
        config['pcs_to_fit'] = '1'
        config['mweight'] = '0.1'
        config['knee_corr'] = 'False'
        config['knee_dof'] = 'False'
        config['marker_radius'] = '5.0'
        config['skin_pad'] = '5.0'
        config['landmarks'] = {
            'pelvis-LASIS': 'L.ASIS',
            'pelvis-RASIS': 'R.ASIS',
            ...
            }

        """
        self.config = config
        self.inputLandmarks = None  # a dict of target landmark names : coordinates
        self.LL = lowerlimbatlas.LowerLimbAtlas('lowerlimb')
        self.landmark_dict = None

        self.landmarkErrors = None
        self.landmarkRMSE = None
        self.fitMDist = None

    def load_data(self):
        self.LL.ll_l.bone_files = self._boneModelFilenamesLeft
        self.LL.ll_l.combined_pcs_filename = self._shapeModelFilenameLeft
        self.LL.ll_r.bone_files = self._boneModelFilenamesRight
        self.LL.ll_r.combined_pcs_filename = self._shapeModelFilenameRight
        self.LL.load_bones()

    def reset_ll(self):
        self.LL.update_all_models(*self.LL._neutral_params)
        self.landmarkErrors = None
        self.landmarkRMSE = None

    def update_from_config(self):
        self.n_shape_modes = self.config['pcs_to_fit']
        if self.knee_corr:
            self.LL.enable_knee_adduction_correction()
        else:
            self.LL.disable_knee_adduction_correction()
        if self.knee_dof:
            self.LL.enable_knee_adduction_dof()
        else:
            self.LL.disable_knee_adduction_dof()

    def _preprocess_landmarks(self):
        """
        given a dictionary of landmark names and coordinates, translate landmarks
        according to marker_radius and skin_pad.

        Landmark names in the dictionary name should have fieldwork landmark names
        """

        def _process(body, body_landmarks):
            skipBody = False
            targetCoords = []
            targetNames = []
            newLandmarks = {}

            # get raw coordinates
            for n in body_landmarks:
                targetName = self.config['landmarks'].get(n)
                targetCoords.append(self.inputLandmarks.get(targetName))
                targetNames.append(targetName)

                # preprocess
            preprocessor = mocap_landmark_preprocess.preprocessors[body]
            try:
                newTargetCoords = preprocessor(
                    self.marker_radius, self.skin_pad, *targetCoords
                )
            except mocap_landmark_preprocess.InsufficientLandmarksError:
                print(('Insufficient landmarks for preprocessing {}'.format(body)))
                skipBody = True

            # save updated coordinates
            if not skipBody:
                for ni, n in enumerate(body_landmarks):
                    if newTargetCoords[ni] is not None:
                        newLandmarks[targetNames[ni]] = newTargetCoords[ni]
            else:
                # keep original coordinates if preprocessing failed
                for ni, n in enumerate(body_landmarks):
                    newLandmarks[targetNames[ni]] = targetCoords[ni]

            return newLandmarks

        preprocdLandmarks = {}

        # fill with original coordinates
        for nInput in list(self.config['landmarks'].values()):
            nInputCoords = self.inputLandmarks.get(nInput)
            print(('{}: {}'.format(nInput, nInputCoords)))
            preprocdLandmarks[nInput] = nInputCoords

        # pelvis
        pelvisLandmarks = (
            'pelvis-LASIS', 'pelvis-RASIS', 'pelvis-LPSIS', 'pelvis-RPSIS',
            'pelvis-Sacral'
        )
        preprocdLandmarks.update(_process('pelvis', pelvisLandmarks))

        # femur-l
        femurLLandmarks = (
            'femur-LEC-l', 'femur-MEC-l'
        )
        preprocdLandmarks.update(_process('femur', femurLLandmarks))

        # femur-r
        femurRLandmarks = (
            'femur-LEC-r', 'femur-MEC-r'
        )
        preprocdLandmarks.update(_process('femur', femurRLandmarks))

        # tibiafibula-l
        tibiafibulaLLandmarks = (
            'tibiafibula-LM-l', 'tibiafibula-MM-l'
        )
        preprocdLandmarks.update(_process('tibiafibula', tibiafibulaLLandmarks))

        # tibiafibula-r
        tibiafibulaRLandmarks = (
            'tibiafibula-LM-r', 'tibiafibula-MM-r'
        )
        preprocdLandmarks.update(_process('tibiafibula', tibiafibulaRLandmarks))

        return preprocdLandmarks

    @property
    def output_model_dict(self):
        _outputModelDict = dict([(m[0], m[1].gf) for m in list(self.LL.models.items())])

        # add pelvis submeshes
        lh_gf, sac_gf, rh_gf = self._split_pelvis_gfs()
        _outputModelDict['hemipelvis-left'] = lh_gf
        _outputModelDict['sacrum'] = sac_gf
        _outputModelDict['hemipelvis-right'] = rh_gf

        # add seperate tibia and fibula
        tibiaGFL, fibulaGFL, tibiaGFR, fibulaGFR = self._split_tibia_fibula_gfs()
        _outputModelDict['tibia-l'] = tibiaGFL
        _outputModelDict['fibula-l'] = fibulaGFL
        _outputModelDict['tibia-r'] = tibiaGFR
        _outputModelDict['fibula-r'] = fibulaGFR

        return _outputModelDict

    def _split_tibia_fibula_gfs(self):
        tibfibL = self.LL.models['tibiafibula-l'].gf
        tibL = tibfibL.makeGFFromElements(
            'tibia-l',
            TIBFIB_SUBMESH_ELEMS['tibia'],
            TIBFIB_BASISTYPES,
        )
        fibL = tibfibL.makeGFFromElements(
            'fibula-l',
            TIBFIB_SUBMESH_ELEMS['fibula'],
            TIBFIB_BASISTYPES,
        )

        tibfibR = self.LL.models['tibiafibula-r'].gf
        tibR = tibfibR.makeGFFromElements(
            'tibia-r',
            TIBFIB_SUBMESH_ELEMS['tibia'],
            TIBFIB_BASISTYPES,
        )
        fibR = tibfibR.makeGFFromElements(
            'fibula-r',
            TIBFIB_SUBMESH_ELEMS['fibula'],
            TIBFIB_BASISTYPES,
        )

        return tibL, fibL, tibR, fibR

    def _split_pelvis_gfs(self):
        """ Given a flattened pelvis model, create left hemi, sacrum,
        and right hemi meshes
        """
        gf = self.LL.models['pelvis'].gf
        lhgf = gf.makeGFFromElements(
            'hemipelvis-left',
            PELVIS_SUBMESH_ELEMS['LH'],
            PELVIS_BASISTYPES
        )
        sacgf = gf.makeGFFromElements(
            'sacrum',
            PELVIS_SUBMESH_ELEMS['sac'],
            PELVIS_BASISTYPES
        )
        rhgf = gf.makeGFFromElements(
            'hemipelvis-right',
            PELVIS_SUBMESH_ELEMS['RH'],
            PELVIS_BASISTYPES
        )
        return lhgf, sacgf, rhgf

    @property
    def valid_registration_modes(self):
        return self._validRegistrationModes

    @property
    def registration_mode(self):
        return self.config['registration_mode']

    @registration_mode.setter
    def registration_mode(self, value):
        if value in self.valid_registration_modes:
            self.config['registration_mode'] = value
        else:
            raise ValueError('Invalid registration mode. Given {}, must be one of {}'.format(value, self.valid_registration_modes))

    @property
    def landmark_names(self):
        return sorted(self.config['landmarks'].keys())

    @property
    def target_landmark_names(self):
        return [self.config['landmarks'][ln] for ln in self.landmark_names]

    @property
    def target_landmarks(self):
        preprocd = self._preprocess_landmarks()
        print('preprocd')
        print(preprocd)
        self.landmark_dict = preprocd

        _targetLandmarks = []
        for n in self.target_landmark_names:
            if (n is None) or (len(n) == 0):
                pass
            else:
                _targetLandmarks.append(preprocd[n])
        return np.array(_targetLandmarks)

    @property
    def m_weight(self):
        return float(self.config['mweight'])

    @m_weight.setter
    def m_weight(self, value):
        self.config['mweight'] = str(value)

    @property
    def marker_radius(self):
        return float(self.config['marker_radius'])

    @marker_radius.setter
    def marker_radius(self, value):
        self.config['marker_radius'] = str(value)

    @property
    def skin_pad(self):
        return float(self.config['skin_pad'])

    @skin_pad.setter
    def skin_pad(self, value):
        self.config['skin_pad'] = str(value)

    @property
    def n_shape_modes(self):
        return int(self.config['pcs_to_fit'])

    @n_shape_modes.setter
    def n_shape_modes(self, n):
        self.config['pcs_to_fit'] = str(n)
        self.LL.shape_modes = np.arange(int(n), dtype=int)

    @property
    def knee_corr(self):
        return self.config['knee_corr'] == 'True'

    @knee_corr.setter
    def knee_corr(self, value):
        if value:
            self.config['knee_corr'] = 'True'
            self.LL.enable_knee_adduction_correction()
        else:
            self.config['knee_corr'] = 'False'
            self.LL.disable_knee_adduction_correction()

    @property
    def knee_dof(self):
        return self.config['knee_dof'] == 'True'

    @knee_dof.setter
    def knee_dof(self, value):
        if value:
            self.config['knee_dof'] = 'True'
            self.LL.enable_knee_adduction_dof()
        else:
            self.config['knee_dof'] = 'False'
            self.LL.disable_knee_adduction_dof()

    def register(self, callback_signal=None):
        self.update_from_config()
        mode = self.config['registration_mode']

        if self.target_landmarks is None:
            raise RuntimeError('Target Landmarks not set')

        if callback_signal is not None:
            def callback(_output):
                callback_signal.emit(_output)
        else:
            callback = None

        if mode == 'shapemodel':
            if self.LL.shape_modes is None:
                raise RuntimeError('Number of pcs to fit not defined')
            else:
                print(('shape models {}'.format(self.LL.shape_modes)))
            if self.m_weight is None:
                raise RuntimeError('Mahalanobis penalty weight not defined')
            output = _register_shape_model(self, callback)
        else:
            raise ValueError('Invalid registration mode: {}'.format(mode))
        return output


def _register_shape_model(lldata, callback=None):
    # if lladata.LL.shape_model_x has not changed from the default,
    # use None for x0 so that it is automatically calculated
    x0Temp = lldata.LL.shape_model_x
    if np.all(x0Temp == 0.0):
        x0 = None
    else:
        x0 = x0Temp
    print(x0)

    # do the fit
    print((lldata.LL.shape_modes, lldata.m_weight))
    xFitted, optLandmarkDist, optLandmarkRMSE, fitInfo = lowerlimbatlasfit2side.fit(
        lldata.LL,
        lldata.target_landmarks,
        lldata.landmark_names,
        lldata.LL.shape_modes,
        lldata.m_weight,
        x0=x0,
        minimise_args=lldata.minArgs,
        callback=callback,
    )
    lldata.landmarkRMSE = optLandmarkRMSE
    lldata.landmarkErrors = optLandmarkDist
    lldata.fitMDist = fitInfo['mahalanobis_distance']
    lldata.LL.shape_model_x = xFitted[-1]
    print(('new X:' + str(lldata.LL.shape_model_x)))
    return xFitted, optLandmarkDist, optLandmarkRMSE, fitInfo
