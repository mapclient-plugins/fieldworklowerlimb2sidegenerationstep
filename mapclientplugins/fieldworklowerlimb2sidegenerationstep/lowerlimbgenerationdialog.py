"""
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland

This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
"""
import os

from PySide2 import QtGui
from PySide2.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem, QDoubleSpinBox, QLabel, QWidget
from PySide2.QtGui import QIntValidator
from PySide2.QtCore import Qt
from PySide2.QtCore import QThread, Signal

from mapclientplugins.fieldworklowerlimb2sidegenerationstep.ui_lowerlimbgenerationdialog import Ui_Dialog

from gias3.mapclientpluginutilities.viewers import MayaviViewerObjectsContainer, MayaviViewerLandmark, \
    MayaviViewerFieldworkModel, colours
from mapclientplugins.fieldworklowerlimb2sidegenerationstep.landmarktablewidget import LandmarkComboBoxTable
from mapclientplugins.fieldworklowerlimb2sidegenerationstep.llstep import validModelLandmarks

import numpy as np

import math

os.environ['ETS_TOOLKIT'] = 'qt'


class _ExecThread(QThread):
    update = Signal(tuple)
    callback = Signal(tuple)

    def __init__(self, func):
        QThread.__init__(self)
        self.func = func

    def run(self):
        # NOT USING CALLBACK since (probably due to threading) not all 
        # bone models update in synchrony
        # output = self.func(self.callback)
        output = self.func()
        self.update.emit(output)


class LowerLimbGenerationDialog(QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """
    defaultColor = colours['bone']
    objectTableHeaderColumns = {'Visible': 0}
    backgroundColour = (0.0, 0.0, 0.0)
    _modelRenderArgs = {}
    _modelDisc = [8, 8]
    _landmarkRenderArgs = {'mode': 'sphere', 'scale_factor': 20.0, 'color': (0, 1, 0)}
    _landmarkAdjRenderArgs = {'mode': 'sphere', 'scale_factor': 15.0, 'color': (1, 0, 0)}

    def __init__(self, data, done_execution, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._scene = self._ui.MayaviScene.visualisation.scene
        self._scene.background = self.backgroundColour

        self.data = data
        self.data.regCallback = self._regCallback
        self.done_execution = done_execution
        self._lockManualRegUpdate = False

        self.selectedObjectName = None

        self._worker = _ExecThread(self.data.register)
        self._worker.update.connect(self._regUpdate)
        self._worker.callback.connect(self._regCallback)

        self.doubleSpinBox_pcs = []
        self.labels = []

        # FIX FROM HERE #
        self._initViewerObjects()
        self._setupGui()
        self._makeConnections()
        self._initialiseObjectTable()
        self._updateConfigs()
        self._refresh()

    def _initViewerObjects(self):
        self._objects = MayaviViewerObjectsContainer()
        for mn, m in list(self.data.LL.models.items()):
            self._objects.addObject(mn,
                                    MayaviViewerFieldworkModel(mn,
                                                               m.gf,
                                                               self._modelDisc,
                                                               render_args=self._modelRenderArgs
                                                               )
                                    )
        # 'none' is first elem in self._landmarkNames, so skip that
        for ln, lcoords in sorted(self.data.inputLandmarks.items()):
            print(('{} {}'.format(ln, lcoords)))
            self._objects.addObject(ln, MayaviViewerLandmark(ln,
                                                             lcoords,
                                                             render_args=self._landmarkRenderArgs
                                                             )
                                    )
        for li, lcoords in enumerate(self.data.targetLandmarks):
            ln = self.data.targetLandmarkNames[li] + '_adjusted'
            print(('{} {} {}'.format(li, ln, lcoords)))
            self._objects.addObject(ln, MayaviViewerLandmark(ln,
                                                             lcoords,
                                                             render_args=self._landmarkAdjRenderArgs
                                                             )
                                    )

    def _setupGui(self):
        # screenshot page
        self._ui.screenshotPixelXLineEdit.setValidator(QIntValidator())
        self._ui.screenshotPixelYLineEdit.setValidator(QIntValidator())

        # landmarks page
        valid_input_landmarks = sorted(self.data.inputLandmarks.keys())
        self.landmarkTable = LandmarkComboBoxTable(
            validModelLandmarks,
            valid_input_landmarks,
            self._ui.tableWidgetLandmarks,
        )

        # auto reg page
        self._ui.spinBox_pcsToFit.setMaximum(self.data.LL.SHAPEMODESMAX)
        for regmode in self.data.validRegistrationModes:
            self._ui.comboBox_regmode.addItem(regmode)

        # disable manual scaling adjustment, just use the shape model
        self._ui.doubleSpinBox_scaling.setEnabled(False)

    def _updateConfigs(self):
        # landmarks page
        self.landmarkTable.clearTable()
        for ml, il in sorted(self.data.config['landmarks'].items()):
            self.landmarkTable.addLandmark(ml, il)

        self._ui.doubleSpinBox_markerRadius.setValue(self.data.markerRadius)
        self._ui.doubleSpinBox_skinPad.setValue(self.data.skinPad)

        # manual reg page
        # This block could definitely be done better
        weights = self.data.LL.shape_mode_weights
        for index, weight in enumerate(weights):
            # Only update the spinBoxes that currently exist
            if index >= len(self.doubleSpinBox_pcs):
                break
            self.doubleSpinBox_pcs[index].setValue(weight)

        # self._ui.doubleSpinBox_scaling.setValue(self.data.T.uniformScaling)
        self._ui.doubleSpinBox_ptx.setValue(self.data.LL.pelvis_rigid[0])
        self._ui.doubleSpinBox_pty.setValue(self.data.LL.pelvis_rigid[1])
        self._ui.doubleSpinBox_ptz.setValue(self.data.LL.pelvis_rigid[2])
        self._ui.doubleSpinBox_prx.setValue(np.rad2deg(self.data.LL.pelvis_rigid[3]))
        self._ui.doubleSpinBox_pry.setValue(np.rad2deg(self.data.LL.pelvis_rigid[4]))
        self._ui.doubleSpinBox_prz.setValue(np.rad2deg(self.data.LL.pelvis_rigid[5]))

        self._ui.doubleSpinBox_hiplx.setValue(np.rad2deg(self.data.LL.hip_rot_l[0]))
        self._ui.doubleSpinBox_hiply.setValue(np.rad2deg(self.data.LL.hip_rot_l[1]))
        self._ui.doubleSpinBox_hiplz.setValue(np.rad2deg(self.data.LL.hip_rot_l[2]))
        self._ui.doubleSpinBox_hiprx.setValue(np.rad2deg(self.data.LL.hip_rot_r[0]))
        self._ui.doubleSpinBox_hipry.setValue(np.rad2deg(self.data.LL.hip_rot_r[1]))
        self._ui.doubleSpinBox_hiprz.setValue(np.rad2deg(self.data.LL.hip_rot_r[2]))

        rot_l = self.data.LL.knee_rot_l
        rot_r = self.data.LL.knee_rot_r
        axis = ['x', 'y', 'z']
        for index, rot_l_dim in enumerate(rot_l):
            getattr(self._ui, f'doubleSpinBox_kneel{axis[index]}').setValue(np.rad2deg(rot_l_dim))
        for index, rot_r_dim in enumerate(rot_r):
            getattr(self._ui, f'doubleSpinBox_kneer{axis[index]}').setValue(np.rad2deg(rot_r_dim))

        # auto reg page
        self._ui.comboBox_regmode.setCurrentIndex(
            self.data.validRegistrationModes.index(
                self.data.registrationMode,
            )
        )
        self._ui.spinBox_pcsToFit.setValue(self.data.nShapeModes)
        self._ui.spinBox_mWeight.setValue(self.data.mWeight)
        self._ui.checkBox_kneecorr.setChecked(bool(self.data.kneeCorr))
        self._ui.checkBox_kneedof.setChecked(bool(self.data.kneeDOF))

    def _updateNShapeModes(self):
        self.data.nShapeModes = self._ui.spinBox_pcsToFit.value()

    def _saveConfigs(self):
        # landmarks page
        self.data.config['landmarks'] = self.landmarkTable.getLandmarkPairs()
        self.data.markerRadius = self._ui.doubleSpinBox_markerRadius.value()
        self.data.skinPad = self._ui.doubleSpinBox_skinPad.value()

        # manual reg page
        self._saveLLParams()

        # auto reg page
        self.data.registrationMode = str(self._ui.comboBox_regmode.currentText())
        self.data.nShapeModes = self._ui.spinBox_pcsToFit.value()
        self.data.mWeight = self._ui.spinBox_mWeight.value()
        self.data.kneeCorr = self._ui.checkBox_kneecorr.isChecked()
        self.data.kneeDOF = self._ui.checkBox_kneedof.isChecked()
        self._ui.checkBox_kneecorr.setChecked(bool(self.data.kneeCorr))
        self._ui.checkBox_kneedof.setChecked(bool(self.data.kneeDOF))

    def _saveLLParams(self):
        shape_mode_weights = np.array(self.data.LL.shape_mode_weights)
        for index in range(len(shape_mode_weights)):
            shape_mode_weights[index] = self.doubleSpinBox_pcs[index].value()

        pelvis_rigid = [
            self._ui.doubleSpinBox_ptx.value(),
            self._ui.doubleSpinBox_pty.value(),
            self._ui.doubleSpinBox_ptz.value(),
            np.deg2rad(self._ui.doubleSpinBox_prx.value()),
            np.deg2rad(self._ui.doubleSpinBox_pry.value()),
            np.deg2rad(self._ui.doubleSpinBox_prz.value()),
        ]

        hip_rot_l = [
            np.deg2rad(self._ui.doubleSpinBox_hiplx.value()),
            np.deg2rad(self._ui.doubleSpinBox_hiply.value()),
            np.deg2rad(self._ui.doubleSpinBox_hiplz.value()),
        ]

        hip_rot_r = [
            np.deg2rad(self._ui.doubleSpinBox_hiprx.value()),
            np.deg2rad(self._ui.doubleSpinBox_hipry.value()),
            np.deg2rad(self._ui.doubleSpinBox_hiprz.value()),
        ]

        if self.data.kneeDOF:
            knee_rot_l = [
                np.deg2rad(self._ui.doubleSpinBox_kneelx.value()),
                np.deg2rad(self._ui.doubleSpinBox_kneelz.value()),
            ]
            knee_rot_r = [
                np.deg2rad(self._ui.doubleSpinBox_kneerx.value()),
                np.deg2rad(self._ui.doubleSpinBox_kneerz.value()),
            ]
        else:
            knee_rot_l = [np.deg2rad(self._ui.doubleSpinBox_kneelx.value()), ]
            knee_rot_r = [np.deg2rad(self._ui.doubleSpinBox_kneerx.value()), ]

        self.data.LL.update_all_models(
            shape_mode_weights[self.data.LL.shape_modes],
            self.data.LL.shape_modes,
            pelvis_rigid,
            hip_rot_l,
            hip_rot_r,
            knee_rot_l,
            knee_rot_r,
        )

    def _makeConnections(self):
        self._ui.tableWidget.itemClicked.connect(self._tableItemClicked)
        self._ui.tableWidget.itemChanged.connect(self._visibleBoxChanged)
        self._ui.screenshotSaveButton.clicked.connect(self._saveScreenShot)

        # landmarks
        # self.landmarktablewidget.table.itemClicked.connect(self._saveConfigs)
        self.landmarkTable.table.itemChanged.connect(self._saveConfigs)
        self._ui.pushButton_addLandmark.clicked.connect(self.landmarkTable.addLandmark)
        self._ui.pushButton_removeLandmark.clicked.connect(self.landmarkTable.removeLandmark)
        # self._ui.doubleSpinBox_scaling.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_ptx.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_pty.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_ptz.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_prx.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_pry.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_prz.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_hiplx.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_hiply.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_hiplz.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_hiprx.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_hipry.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_hiprz.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_kneelx.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_kneely.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_kneelz.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_kneerx.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_kneery.valueChanged.connect(self._manualRegUpdate)
        self._ui.doubleSpinBox_kneerz.valueChanged.connect(self._manualRegUpdate)
        self._ui.pushButton_manual_reset.clicked.connect(self._reset)
        self._ui.pushButton_manual_accept.clicked.connect(self._accept)

        # auto reg
        self._ui.checkBox_kneecorr.stateChanged.connect(self._autoRegChanged)
        self._ui.checkBox_kneedof.stateChanged.connect(self._autoRegChanged)
        self._ui.pushButton_auto_reset.clicked.connect(self._reset)
        self._ui.pushButton_auto_accept.clicked.connect(self._accept)
        self._ui.pushButton_auto_abort.clicked.connect(self._abort)
        self._ui.pushButton_auto_reg.clicked.connect(self._autoReg)
        self._ui.spinBox_pcsToFit.valueChanged.connect(self._pcsToFitChanged)

    def _pcsToFitChanged(self):
        # delta represents a change in the number of PCs. (+) means we need to increase, (-) means we need to decrease
        delta = self._ui.spinBox_pcsToFit.value() - int(self._ui.gridLayout_3.count() / 2)

        # If delta is negative, delete the specified number of widgets from the layout
        if delta < 0:
            for _ in range(abs(delta)):
                self.doubleSpinBox_pcs.pop().setParent(None)
                self.labels.pop().setParent(None)

                # ??:
                self._updateNShapeModes()
                # ??:
                self._manualRegUpdate()

        # If delta is positive, add the specified number of widgets to the layout
        elif delta > 0:
            # Get the position of the last cell
            cell_row = math.ceil(self._ui.gridLayout_3.count() / 4)
            cell_column = 3 if ((self._ui.gridLayout_3.count() % 4) == 0) else 1

            for it in range(abs(delta)):
                if cell_column == 3:
                    cell_row += 1
                    cell_column = 1
                else:
                    cell_column = 3

                widget = QDoubleSpinBox(self._ui.page)
                widget.setObjectName("doubleSpinBox_pc" + str(self._ui.gridLayout_3.count() + 1))
                widget.setMinimum(-99.000000000000000)
                widget.setMaximum(99.000000000000000)
                widget.setSingleStep(0.100000000000000)
                self._ui.gridLayout_3.addWidget(widget, cell_row, cell_column, 1, 1)

                widget.valueChanged.connect(self._manualRegUpdate)
                self._updateNShapeModes()

                label = QLabel(self._ui.page)
                label.setObjectName("label_" + str(self._ui.gridLayout_3.count() + 1))
                label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
                label.setText(str(int((self._ui.gridLayout_3.count() + 1) / 2)))
                self._ui.gridLayout_3.addWidget(label, cell_row, cell_column - 1, 1, 1)

                self.doubleSpinBox_pcs.append(widget)
                self.labels.append(label)

    def _initialiseObjectTable(self):
        self._ui.tableWidget.setRowCount(self._objects.getNumberOfObjects())
        self._ui.tableWidget.verticalHeader().setVisible(False)
        self._ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        # 'none' is first elem in self._landmarkNames, so skip that
        row = 0
        # Add input landmarks
        for li, ln in enumerate(sorted(self.data.inputLandmarks.keys())):
            self._addObjectToTable(row, ln, self._objects.getObject(ln), checked=True)
            row += 1

        # Add adjusted landmarks
        for ln in self.data.targetLandmarkNames:
            ln = ln + '_adjusted'
            self._addObjectToTable(row, ln, self._objects.getObject(ln), checked=True)
            row += 1

        # Add bone models
        for mn in list(self.data.LL.models.keys()):
            self._addObjectToTable(row, mn, self._objects.getObject(mn), checked=True)
            row += 1

        # self._modelRow = r
        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['Visible'])

    def _addObjectToTable(self, row, name, obj, checked=True):
        type_name = obj.typeName
        print(('adding to table: %s (%s)' % (name, type_name)))
        table_item = QTableWidgetItem(name)
        if checked:
            table_item.setCheckState(Qt.Checked)
        else:
            table_item.setCheckState(Qt.Unchecked)

        self._ui.tableWidget.setItem(row, self.objectTableHeaderColumns['Visible'], table_item)

    # It seems all this method does is print which item has been clicked, which is already done in _visibleBoxChanged
    def _tableItemClicked(self):
        pass
        # selected_row = self._ui.tableWidget.currentRow()
        #
        # self.selectedObjectName = self._ui.tableWidget.item(
        #     selected_row,
        #     self.objectTableHeaderColumns['Visible']
        # ).text()
        #
        # print(selected_row)
        # print(self.selectedObjectName)

    def _visibleBoxChanged(self, table_item):
        # Checked changed item is actually the checkbox
        if table_item.column() == self.objectTableHeaderColumns['Visible']:
            # Get visible status
            name = table_item.text()
            visible = table_item.checkState() == QtGui.Qt.CheckState.Checked

            # Toggle visibility
            obj = self._objects.getObject(name)
            if obj.sceneObject:
                obj.setVisibility(visible)
            else:
                obj.draw(self._scene)

    def _getSelectedObjectName(self):
        return self.selectedObjectName

    def _getSelectedScalarName(self):
        return 'none'

    def _drawObjects(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).draw(self._scene)

    def _updateSceneModels(self):
        for mn in self.data.LL.models:
            mesh_obj = self._objects.getObject(mn)
            mesh_obj.updateGeometry(None, self._scene)

    def _manualRegUpdate(self):
        if not self._lockManualRegUpdate:
            self._saveConfigs()
            # self.data.updateLLModel() # LL is auto updated in _saveConfigs
            self._updateSceneModels()

    def _autoRegChanged(self):
        self.data.kneeCorr = self._ui.checkBox_kneecorr.isChecked()
        self.data.kneeDOF = self._ui.checkBox_kneedof.isChecked()

    def _regLockUI(self):
        self.landmarkTable.disable()
        self._ui.doubleSpinBox_markerRadius.setEnabled(False)
        self._ui.doubleSpinBox_skinPad.setEnabled(False)
        for index in range(len(self.doubleSpinBox_pcs)):
            self.doubleSpinBox_pcs[index].setEnabled(False)
        self._ui.doubleSpinBox_ptx.setEnabled(False)
        self._ui.doubleSpinBox_pty.setEnabled(False)
        self._ui.doubleSpinBox_ptz.setEnabled(False)
        self._ui.doubleSpinBox_prx.setEnabled(False)
        self._ui.doubleSpinBox_pry.setEnabled(False)
        self._ui.doubleSpinBox_prz.setEnabled(False)
        self._ui.doubleSpinBox_hiplx.setEnabled(False)
        self._ui.doubleSpinBox_hiply.setEnabled(False)
        self._ui.doubleSpinBox_hiplz.setEnabled(False)
        self._ui.doubleSpinBox_hiprx.setEnabled(False)
        self._ui.doubleSpinBox_hipry.setEnabled(False)
        self._ui.doubleSpinBox_hiprz.setEnabled(False)
        self._ui.doubleSpinBox_kneelx.setEnabled(False)
        self._ui.doubleSpinBox_kneely.setEnabled(False)
        self._ui.doubleSpinBox_kneelz.setEnabled(False)
        self._ui.doubleSpinBox_kneerx.setEnabled(False)
        self._ui.doubleSpinBox_kneery.setEnabled(False)
        self._ui.doubleSpinBox_kneerz.setEnabled(False)
        self._ui.pushButton_manual_accept.setEnabled(False)
        self._ui.pushButton_manual_reset.setEnabled(False)

        self._ui.comboBox_regmode.setEnabled(False)
        self._ui.spinBox_pcsToFit.setEnabled(False)
        self._ui.spinBox_mWeight.setEnabled(False)
        self._ui.checkBox_kneecorr.setEnabled(False)
        self._ui.checkBox_kneedof.setEnabled(False)
        self._ui.pushButton_auto_accept.setEnabled(False)
        self._ui.pushButton_auto_reset.setEnabled(False)
        self._ui.pushButton_auto_abort.setEnabled(False)
        self._ui.pushButton_auto_reg.setEnabled(False)

    def _regUnlockUI(self):
        self.landmarkTable.enable()
        self._ui.doubleSpinBox_markerRadius.setEnabled(True)
        self._ui.doubleSpinBox_skinPad.setEnabled(True)
        for index in range(len(self.doubleSpinBox_pcs)):
            self.doubleSpinBox_pcs[index].setEnabled(True)
        self._ui.doubleSpinBox_ptx.setEnabled(True)
        self._ui.doubleSpinBox_pty.setEnabled(True)
        self._ui.doubleSpinBox_ptz.setEnabled(True)
        self._ui.doubleSpinBox_prx.setEnabled(True)
        self._ui.doubleSpinBox_pry.setEnabled(True)
        self._ui.doubleSpinBox_prz.setEnabled(True)
        self._ui.doubleSpinBox_hiplx.setEnabled(True)
        self._ui.doubleSpinBox_hiprx.setEnabled(True)
        self._ui.doubleSpinBox_hiply.setEnabled(True)
        self._ui.doubleSpinBox_hipry.setEnabled(True)
        self._ui.doubleSpinBox_hiplz.setEnabled(True)
        self._ui.doubleSpinBox_hiprz.setEnabled(True)
        self._ui.doubleSpinBox_kneelx.setEnabled(True)
        self._ui.doubleSpinBox_kneerx.setEnabled(True)
        self._ui.doubleSpinBox_kneely.setEnabled(True)
        self._ui.doubleSpinBox_kneery.setEnabled(True)
        self._ui.doubleSpinBox_kneelz.setEnabled(True)
        self._ui.doubleSpinBox_kneerz.setEnabled(True)
        self._ui.pushButton_manual_accept.setEnabled(True)
        self._ui.pushButton_manual_reset.setEnabled(True)

        self._ui.comboBox_regmode.setEnabled(True)
        self._ui.spinBox_pcsToFit.setEnabled(True)
        self._ui.spinBox_mWeight.setEnabled(True)
        self._ui.checkBox_kneecorr.setEnabled(True)
        self._ui.checkBox_kneedof.setEnabled(True)
        self._ui.pushButton_auto_accept.setEnabled(True)
        self._ui.pushButton_auto_reset.setEnabled(True)
        self._ui.pushButton_auto_abort.setEnabled(True)
        self._ui.pushButton_auto_reg.setEnabled(True)

    def _regUpdate(self, output):
        # update models in scene
        self._updateSceneModels()

        # update error field
        self._ui.lineEdit_landmarkError.setText('{:5.2f}'.format(self.data.landmarkRMSE))
        self._ui.lineEdit_mDist.setText('{:5.2f}'.format(self.data.fitMDist))

        # unlock reg ui
        self._regUnlockUI()

        # update configs
        self._lockManualRegUpdate = True
        self._updateConfigs()
        self._lockManualRegUpdate = False

    def _regCallback(self, output):
        self._updateSceneModels()

    def _autoReg(self):
        # self._saveConfigs()
        # Auto-reg doesn't work if any of the shape values are non-zero
        self.data.LL.shape_mode_weights = np.zeros(self._ui.spinBox_pcsToFit.value(), dtype=float)
        self._worker.start()
        self._regLockUI()

    def _reset(self):
        self.data.resetLL()
        self._lockManualRegUpdate = True
        self._updateConfigs()
        self._lockManualRegUpdate = False
        self._updateSceneModels()

        # clear error fields
        self._ui.lineEdit_landmarkError.clear()
        self._ui.lineEdit_mDist.clear()

    def _accept(self):
        self._saveConfigs()
        self._close()
        self.done_execution()

    def _abort(self):
        self._reset()
        self._close()

    def _close(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).remove()

        self._objects._objects = {}

    def _refresh(self):
        for r in range(self._ui.tableWidget.rowCount()):
            table_item = self._ui.tableWidget.item(r, self.objectTableHeaderColumns['Visible'])
            if table_item is None:
                continue

            name = table_item.text()
            visible = table_item.checkState() == QtGui.Qt.CheckState.Checked
            obj = self._objects.getObject(name)
            if obj.sceneObject:
                obj.setVisibility(visible)
            else:
                obj.draw(self._scene)

    def _saveScreenShot(self):
        filename = self._ui.screenshotFilenameLineEdit.text()
        width = int(self._ui.screenshotPixelXLineEdit.text())
        height = int(self._ui.screenshotPixelYLineEdit.text())
        self._scene.mlab.savefig(filename, size=(width, height))

    # ================================================================#
    # @on_trait_change('scene.activated')
    # def testPlot(self):
    #     # This function is called when the view is opened. We don't
    #     # populate the scene when the view is not yet open, as some
    #     # VTK features require a GLContext.
    #     print('trait_changed')

    #     # We can do normal mlab calls on the embedded scene.
    #     self._scene.mlab.test_points3d()

    # def _saveImage_fired( self ):
    #     self.scene.mlab.savefig( str(self.saveImageFilename), size=( int(self.saveImageWidth), \
    #     int(self.saveImageLength) ) )
