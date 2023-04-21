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

from PySide6.QtWidgets import QAbstractItemView, QTableWidgetItem, QComboBox


class LandmarkComboBoxTable(object):

    def __init__(self, model_landmarks, input_landmarks, table_widget, landmark_pairs=None):
        """
        A table for editing model landmark - input landmark pairs. Each are picked from
        comboboxes.

        Inputs
        ------
        model_landmarks : list
            a list of valid model landmark names
        input_landmarks : list
            a list of input landmark names
        table_widget : QTableWidgetItem
            The tableWidget to use
        landmark_pairs : dict (optional)
            Existing landmark pairs to initialise the table with
        """

        self.modelLandmarks = model_landmarks
        self.inputLandmarks = input_landmarks
        self.table = table_widget
        self._rowCount = 0
        self._comboBoxes = []  # (model, input)

        if landmark_pairs is not None:
            for m, i in list(landmark_pairs.items()):
                self.add_landmark(m, i)

    def add_landmark(self, model_landmark=None, input_landmark=None):
        """
        Add a new row to the table. Create new combo boxes for the new row.
        If model_landmark and or input_landmark are provided, those landmark
        names will be preselected.
        """
        self.table.setRowCount(self._rowCount + 1)
        combMode = self._add_combo_box(self._rowCount, 0, self.modelLandmarks, model_landmark)
        combInput = self._add_combo_box(self._rowCount, 1, self.inputLandmarks, input_landmark)
        self._comboBoxes.append((combMode, combInput))
        self._rowCount += 1
        # print(('row added {}'.format(self._rowCount)))

    def remove_landmark(self, selected_row=None):
        """
        Delete the specified or if not specified, the currently selected
        row from the table
        """
        if selected_row is None:
            selected_row = self.table.currentRow()
        self.table.removeRow(selected_row)
        self._comboBoxes.remove(self._comboBoxes[selected_row])
        self._rowCount -= 1

    def clear_table(self):
        """
        Delete all rows
        """
        while self._rowCount > 0:
            self.remove_landmark(0)

    def get_landmark_pairs(self):
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

    def _add_combo_box(self, row, col, items, current_item=None):
        comb = QComboBox()
        for it in items:
            comb.addItem(it)
        self.table.setCellWidget(row, col, comb)

        if (current_item is not None) and (current_item != ''):
            if current_item in items:
                comb.setCurrentIndex(items.index(current_item))
            else:
                print(('invalid item: {}'.format(current_item)))

        return comb


class LandmarkComboBoxTextTable(object):

    def __init__(self, model_landmarks, table_widget, landmark_pairs=None):
        """
        A table for editing model landmark - input landmark pairs. Model landmarks are
        picked from comboboxes, input landmarks are text entries.

        Inputs
        ------
        model_landmarks : list
            a list of valid model landmark names
        table_widget : QTableWidgetItem
            The tableWidget to use
        landmark_pairs : dict (optional)
            Existing landmark pairs to initialise the table with
        """

        self.modelLandmarks = model_landmarks
        self.table = table_widget
        self._rowCount = 0
        self._rowElems = []  # (model, input)

        if landmark_pairs is not None:
            for m, i in list(landmark_pairs.items()):
                self.add_landmark(m, i)

    def add_landmark(self, model_landmark=None, input_landmark=None):
        """
        Add a new row to the table. Create new combo boxes for the new row.
        If model_landmark and or input_landmark are provided, those landmark
        names will be preselected.
        """
        self.table.setRowCount(self._rowCount + 1)
        combMode = self._add_combo_box(self._rowCount, 0, self.modelLandmarks, model_landmark)
        elemInput = self._add_table_item(self._rowCount, 1, input_landmark)
        self._rowElems.append((combMode, elemInput))
        self._rowCount += 1
        # print(('row added {}'.format(self._rowCount)))

    def remove_landmark(self, selected_row=None):
        """
        Delete the specified or if not specified, the currently selected
        row from the table
        """
        if selected_row is None:
            selected_row = self.table.currentRow()
        self.table.removeRow(selected_row)
        self._rowElems.remove(self._rowElems[selected_row])
        self._rowCount -= 1

    def clear_table(self):
        """
        Delete all rows
        """
        while self._rowCount > 0:
            self.remove_landmark(0)

    def get_landmark_pairs(self):
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

    def _add_combo_box(self, row, col, items, current_item=None):
        comb = QComboBox()
        for it in items:
            comb.addItem(it)
        self.table.setCellWidget(row, col, comb)

        if (current_item is not None) and (current_item != ''):
            if current_item in items:
                comb.setCurrentIndex(items.index(current_item))
            else:
                print(('invalid item: {}'.format(current_item)))

        return comb

    def _add_table_item(self, row, col, text=None):
        tableItem = QTableWidgetItem()
        if text is not None:
            tableItem.setText(text)

        self.table.setItem(row, col, tableItem)
        return tableItem
