"""
MAP Client Plugin Step
"""
import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.fieldworklowerlimb2sidegenerationstep.configuredialog import ConfigureDialog

from mapclientplugins.fieldworklowerlimb2sidegenerationstep import llstep
from mapclientplugins.fieldworklowerlimb2sidegenerationstep.lowerlimbgenerationdialog import LowerLimbGenerationDialog

DEFAULT_MODEL_LANDMARKS = (
    'pelvis-LASIS', 'pelvis-RASIS', 'pelvis-Sacral',
    'femur-MEC-l', 'femur-LEC-l',
    'femur-MEC-r', 'femur-LEC-r',
    'tibiafibula-MM-l', 'tibiafibula-LM-l',
    'tibiafibula-MM-r', 'tibiafibula-LM-r',
)


class FieldworkLowerLimb2SideGenerationStep(WorkflowStepMountPoint):
    """
    Step for customising the lower limb bones to motion capture markers.

    Inputs
    ------
    landmarks : dict
        Dictionary of marker names : marker coordinates

    Outputs
    -------
    fieldworkmodeldict : dict
        A dictionary of customised fieldwork models of lower limb bones.
        Dictionary keys are: "pelvis", "pelvis flat", 'hemipelvis-left",
        "hemipelvis-right", "sacrum", "femur-l", "femur-r", "tibiafibula-l",
        "tibiafibula-r", "tibia-l", "tibia-r", "fibula-l", 'fibula-r",
        "patella-l", "patella-r".
    LowerLimbAtlas : LowerLimbAtlas instance
    """

    def __init__(self, location):
        super(FieldworkLowerLimb2SideGenerationStep, self).__init__('Fieldwork Lower Limb (2 sides) Generation',
                                                                    location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Registration'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#landmarks'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodeldict'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#gias-lowerlimb'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#landmarks'))
        self._config = {
            'identifier': '', 'GUI': 'True', 'registration_mode': 'shapemodel',
            'pcs_to_fit': '1', 'mweight': '0.1', 'knee_corr': 'False', 'knee_dof': 'False',
            'marker_radius': '5.0', 'skin_pad': '5.0', 'landmarks': {}
        }
        for landmark in DEFAULT_MODEL_LANDMARKS:
            self._config['landmarks'][landmark] = ''

        self._data = llstep.LLStepData(self._config)

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        self._data.load_data()
        self._data.update_from_config()
        print('LL estimation configs:')
        print(self._data.config)
        if self._config['GUI'] == 'True':
            # Start gui
            widget = LowerLimbGenerationDialog(self._data, self._doneExecution)
            self._setCurrentWidget(widget)
        else:
            self._data.register()
            self._doneExecution()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        """
        self._data.inputLandmarks = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#landmarks

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        """
        if index == 1:
            print(('outputting {}'.format(list(self._data.output_model_dict.keys()))))
            return self._data.output_model_dict

        elif index == 2:
            return self._data.LL

        elif index == 3:
            # We may want to replace, or update the dictionary below to make
            # sure that the landmarks we are interested in are being included.
            return self._data.landmark_dict

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()
            self._data.config = self._config

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
