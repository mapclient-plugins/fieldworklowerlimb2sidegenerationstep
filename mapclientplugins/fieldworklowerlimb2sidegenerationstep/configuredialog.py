from PySide2 import QtWidgets
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

        self.landmarkTable = LandmarkComboBoxTextTable(
            validModelLandmarks,
            self._ui.tableWidgetLandmarks,
        )

        self._makeConnections()

        for regmode in REG_MODES:
            self._ui.comboBox_regmode.addItem(regmode)

    def _makeConnections(self):
        self._ui.pushButton_addLandmark.clicked.connect(self.landmarkTable.addLandmark)
        self._ui.pushButton_removeLandmark.clicked.connect(self.landmarkTable.removeLandmark)

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # As it is, the configuration cannot be invalid.
        return True

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        config = {}
        config['registration_mode'] = self._ui.comboBox_regmode.currentText()
        config['pcs_to_fit'] = str(self._ui.spinBox_pcsToFit.value())
        config['mweight'] = str(self._ui.doubleSpinBox_mWeight.value())
        config['landmarks'] = self.landmarkTable.getLandmarkPairs()
        config['marker_radius'] = self._ui.doubleSpinBox_markerRadius.value()
        config['skin_pad'] = self._ui.doubleSpinBox_skinPad.value()
        if self._ui.checkBox_kneecorr.isChecked():
            config['knee_corr'] = 'True'
        else:
            config['knee_corr'] = 'False'
        if self._ui.checkBox_kneedof.isChecked():
            config['knee_dof'] = 'True'
        else:
            config['knee_dof'] = 'False'
        if self._ui.checkBox_GUI.isChecked():
            config['GUI'] = 'True'
        else:
            config['GUI'] = 'False'
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.
        """
        self._ui.comboBox_regmode.setCurrentIndex(
            REG_MODES.index(config['registration_mode'])
        )
        self._ui.spinBox_pcsToFit.setValue(int(config['pcs_to_fit']))
        self._ui.doubleSpinBox_mWeight.setValue(float(config['mweight']))

        for ml, il in sorted(config['landmarks'].items()):
            self.landmarkTable.addLandmark(ml, il)
        self._ui.doubleSpinBox_markerRadius.setValue(float(config['marker_radius']))
        self._ui.doubleSpinBox_skinPad.setValue(float(config['skin_pad']))
        if config['knee_corr'] == 'True':
            self._ui.checkBox_kneecorr.setChecked(bool(True))
        else:
            self._ui.checkBox_kneecorr.setChecked(bool(False))
        if config['knee_dof'] == 'True':
            self._ui.checkBox_kneedof.setChecked(bool(True))
        else:
            self._ui.checkBox_kneedof.setChecked(bool(False))
        if config['GUI'] == 'True':
            self._ui.checkBox_GUI.setChecked(bool(True))
        else:
            self._ui.checkBox_GUI.setChecked(bool(False))
