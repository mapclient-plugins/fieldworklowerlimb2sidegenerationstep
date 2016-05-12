'''
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
'''

from PySide.QtGui import QDialog, QFileDialog, QDialogButtonBox,\
                         QAbstractItemView, QTableWidgetItem, QComboBox   

class LandmarkComboBoxTable(object):

    def __init__(self, modelLandmarks, inputLandmarks, tableWidget, landmarkPairs=None):
        """
        A table for editing model landmark - input landmark pairs. Each are picked from
        comboboxes.

        Inputs
        ------
        modelLandmarks : list
            a list of valid model landmark names
        inputLandmarks : list
            a list of input landmark names
        tableWidget : QTableWidgetItem
            The tableWidget to use
        landmarkPairs : dict (optional)
            Existing landmark pairs to initialise the table with
        """
         
        self.modelLandmarks = modelLandmarks
        self.inputLandmarks = inputLandmarks
        self.table = tableWidget
        self._rowCount = 0
        self._comboBoxes = [] # (model, input)

        if landmarkPairs is not None:
            for m, i in landmarkPairs.items():
                self.addLandmark(m, i)

    def _initTableWidget(self):
        self._ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

    def addLandmark(self, modelLandmark=None, inputLandmark=None):
        """
        Add a new row to the table. Create new combo boxes for the new row.
        If modelLandmark and or inputLandmark are provided, those landmark
        names will be preselected.
        """
        self.table.setRowCount(self._rowCount+1)
        combMode = self._addComboBox(self._rowCount, 0, self.modelLandmarks, modelLandmark)
        combInput = self._addComboBox(self._rowCount, 1, self.inputLandmarks, inputLandmark)
        self._comboBoxes.append((combMode, combInput))
        self._rowCount += 1
        print('row added {}'.format(self._rowCount))

    def removeLandmark(self, selectedRow=None):
        """
        Delete the specified or if not specified, the currently selected
        row from the table
        """
        if selectedRow is None:
            selectedRow = self.table.currentRow()
        self.table.removeRow(selectedRow)
        self._comboBoxes.remove(self._comboBoxes[selectedRow])
        self._rowCount -= 1

    def clearTable(self):
        """
        Delete all rows
        """
        while self._rowCount>0:
            self.removeLandmark(0)

    def getLandmarkPairs(self):
        """
        Return a dictionary mapping selected model landmarks to selected 
        input landmarks
        """
        d = {}
        for mComb, iComb in self._comboBoxes:
            d[str(mComb.currentText())] = str(iComb.currentText())
        return d

    def enable(self):
        for mComb, iComb in self._comboBoxes:
            mComb.setEnabled(True)
            iComb.setEnabled(True)

    def disable(self):
        for mComb, iComb in self._comboBoxes:
            mComb.setEnabled(False)
            iComb.setEnabled(False)


    def _addComboBox(self, row, col, items, currentItem=None):
        comb = QComboBox()
        for it in items:
            comb.addItem(it)
        self.table.setCellWidget(row, col, comb)

        if (currentItem is not None) and (currentItem!=''):
            if currentItem in items:
                comb.setCurrentIndex(items.index(currentItem))
            else:
                print('invalid item: {}'.format(currentItem))

        return comb

class LandmarkComboBoxTextTable(object):

    def __init__(self, modelLandmarks, tableWidget, landmarkPairs=None):
        """
        A table for editing model landmark - input landmark pairs. Model landmarks are
        picked from comboboxes, input landmarks are text entries.

        Inputs
        ------
        modelLandmarks : list
            a list of valid model landmark names
        inputLandmarks : list
            a list of input landmark names
        tableWidget : QTableWidgetItem
            The tableWidget to use
        landmarkPairs : dict (optional)
            Existing landmark pairs to initialise the table with
        """
         
        self.modelLandmarks = modelLandmarks
        self.table = tableWidget
        self._rowCount = 0
        self._rowElems = [] # (model, input)

        if landmarkPairs is not None:
            for m, i in landmarkPairs.items():
                self.addLandmark(m, i)

    def _initTableWidget(self):
        self._ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

    def addLandmark(self, modelLandmark=None, inputLandmark=None):
        """
        Add a new row to the table. Create new combo boxes for the new row.
        If modelLandmark and or inputLandmark are provided, those landmark
        names will be preselected.
        """
        self.table.setRowCount(self._rowCount+1)
        combMode = self._addComboBox(self._rowCount, 0, self.modelLandmarks, modelLandmark)
        elemInput = self._addTableItem(self._rowCount, 1, inputLandmark)
        self._rowElems.append((combMode, elemInput))
        self._rowCount += 1
        print('row added {}'.format(self._rowCount))

    def removeLandmark(self, selectedRow=None):
        """
        Delete the specified or if not specified, the currently selected
        row from the table
        """
        if selectedRow is None:
            selectedRow = self.table.currentRow()
        self.table.removeRow(selectedRow)
        self._rowElems.remove(self._rowElems[selectedRow])
        self._rowCount -= 1

    def clearTable(self):
        """
        Delete all rows
        """
        while self._rowCount>0:
            self.removeLandmark(0)

    def getLandmarkPairs(self):
        """
        Return a dictionary mapping selected model landmarks to selected 
        input landmarks
        """
        d = {}
        for mElem, iElem in self._rowElems:
            d[str(mElem.currentText())] = str(iElem.text())
        return d

    def enable(self):
        for mElem, iElem in self._rowElems:
            mElem.setEnabled(True)
            iElem.setEnabled(True)

    def disable(self):
        for mElem, iElem in self._rowElems:
            mElem.setEnabled(False)
            iElem.setEnabled(False)

    def _addComboBox(self, row, col, items, currentItem=None):
        comb = QComboBox()
        for it in items:
            comb.addItem(it)
        self.table.setCellWidget(row, col, comb)

        if (currentItem is not None) and (currentItem!=''):
            if currentItem in items:
                comb.setCurrentIndex(items.index(currentItem))
            else:
                print('invalid item: {}'.format(currentItem))

        return comb

    def _addTableItem(self, row, col, text=None):
        tableItem = QTableWidgetItem()
        if text is not None:
            tableItem.setText(text)

        self.table.setItem(row, col, tableItem)
        return tableItem