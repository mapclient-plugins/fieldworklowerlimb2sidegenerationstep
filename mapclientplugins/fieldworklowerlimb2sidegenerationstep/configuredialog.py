from PySide6 import QtWidgets
from mapclientplugins.fieldworklowerlimb2sidegenerationstep.ui_configuredialog import Ui_Dialog
from mapclientplugins.fieldworklowerlimb2sidegenerationstep.llstep import validModelLandmarks
from mapclientplugins.fieldworklowerlimb2sidegenerationstep.landmarktablewidget import LandmarkComboBoxTextTable

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''

REG_MODES = ('shapemodel',)


# REG_MODES = ('shapemodel', 'uniformscaling', 'perbonescaling', 'manual')

class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self.landmarkTable = LandmarkComboBoxTextTable(
            validModelLandmarks,
            self._ui.tableWidgetLandmarks,
        )

        self._make_connections()

        for regmode in REG_MODES:
            self._ui.comboBox_regmode.addItem(regmode)

    def _make_connections(self):
        self._ui.lineEdit_id.textChanged.connect(self.validate)
        self._ui.pushButton_addLandmark.clicked.connect(self.landmarkTable.add_landmark)
        self._ui.pushButton_removeLandmark.clicked.connect(self.landmarkTable.remove_landmark)

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.StandardButton.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration', 'This configuration is invalid.  Unpredictable behaviour '
                                                   'may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.StandardButton(QtWidgets.QMessageBox.StandardButton.Yes |
                                                                                        QtWidgets.QMessageBox.StandardButton.No),
                                                   QtWidgets.QMessageBox.StandardButton.No)

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit_id.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit_id.text())
        if valid:
            self._ui.lineEdit_id.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit_id.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEdit_id.text()
        config = {
            'identifier': self._ui.lineEdit_id.text(),
            'registration_mode': self._ui.comboBox_regmode.currentText(),
            'pcs_to_fit': str(self._ui.spinBox_pcsToFit.value()),
            'mweight': str(self._ui.doubleSpinBox_mWeight.value()),
            'landmarks': self.landmarkTable.get_landmark_pairs(),
            'marker_radius': self._ui.doubleSpinBox_markerRadius.value(),
            'skin_pad': self._ui.doubleSpinBox_skinPad.value(),
            'knee_corr': 'True' if self._ui.checkBox_kneecorr.isChecked() else 'False',
            'knee_dof': 'True' if self._ui.checkBox_kneedof.isChecked() else 'False',
            'GUI': 'True' if self._ui.checkBox_GUI.isChecked() else 'False'
        }
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit_id.setText(config['identifier'])
        self._ui.comboBox_regmode.setCurrentIndex(REG_MODES.index(config['registration_mode']))
        self._ui.spinBox_pcsToFit.setValue(int(config['pcs_to_fit']))
        self._ui.doubleSpinBox_mWeight.setValue(float(config['mweight']))

        for ml, il in sorted(config['landmarks'].items()):
            self.landmarkTable.add_landmark(ml, il)

        self._ui.doubleSpinBox_markerRadius.setValue(float(config['marker_radius']))
        self._ui.doubleSpinBox_skinPad.setValue(float(config['skin_pad']))
        self._ui.checkBox_kneecorr.setChecked(config['knee_corr'] == 'True')
        self._ui.checkBox_kneedof.setChecked(config['knee_dof'] == 'True')
        self._ui.checkBox_GUI.setChecked(config['GUI'] == 'True')
