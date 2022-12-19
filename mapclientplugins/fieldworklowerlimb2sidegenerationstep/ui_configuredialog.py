# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(597, 591)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configGroupBox.sizePolicy().hasHeightForWidth())
        self.configGroupBox.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit_id = QLineEdit(self.configGroupBox)
        self.lineEdit_id.setObjectName(u"lineEdit_id")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_id)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label1)

        self.comboBox_regmode = QComboBox(self.configGroupBox)
        self.comboBox_regmode.setObjectName(u"comboBox_regmode")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_regmode)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.spinBox_pcsToFit = QSpinBox(self.configGroupBox)
        self.spinBox_pcsToFit.setObjectName(u"spinBox_pcsToFit")
        self.spinBox_pcsToFit.setMinimum(1)
        self.spinBox_pcsToFit.setMaximum(99)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox_pcsToFit)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.doubleSpinBox_mWeight = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBox_mWeight.setObjectName(u"doubleSpinBox_mWeight")
        self.doubleSpinBox_mWeight.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_mWeight)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidgetLandmarks = QTableWidget(self.configGroupBox)
        if (self.tableWidgetLandmarks.columnCount() < 2):
            self.tableWidgetLandmarks.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetLandmarks.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetLandmarks.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidgetLandmarks.setObjectName(u"tableWidgetLandmarks")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidgetLandmarks.sizePolicy().hasHeightForWidth())
        self.tableWidgetLandmarks.setSizePolicy(sizePolicy1)
        self.tableWidgetLandmarks.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidgetLandmarks.horizontalHeader().setMinimumSectionSize(200)
        self.tableWidgetLandmarks.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout.addWidget(self.tableWidgetLandmarks)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_addLandmark = QPushButton(self.configGroupBox)
        self.pushButton_addLandmark.setObjectName(u"pushButton_addLandmark")

        self.horizontalLayout_2.addWidget(self.pushButton_addLandmark)

        self.pushButton_removeLandmark = QPushButton(self.configGroupBox)
        self.pushButton_removeLandmark.setObjectName(u"pushButton_removeLandmark")

        self.horizontalLayout_2.addWidget(self.pushButton_removeLandmark)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.verticalLayout)

        self.label_12 = QLabel(self.configGroupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.doubleSpinBox_markerRadius = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBox_markerRadius.setObjectName(u"doubleSpinBox_markerRadius")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBox_markerRadius)

        self.label_13 = QLabel(self.configGroupBox)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.doubleSpinBox_skinPad = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBox_skinPad.setObjectName(u"doubleSpinBox_skinPad")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.doubleSpinBox_skinPad)

        self.label_10 = QLabel(self.configGroupBox)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_kneedof = QCheckBox(self.configGroupBox)
        self.checkBox_kneedof.setObjectName(u"checkBox_kneedof")

        self.horizontalLayout.addWidget(self.checkBox_kneedof)

        self.checkBox_kneecorr = QCheckBox(self.configGroupBox)
        self.checkBox_kneecorr.setObjectName(u"checkBox_kneecorr")

        self.horizontalLayout.addWidget(self.checkBox_kneecorr)


        self.formLayout.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_11 = QLabel(self.configGroupBox)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_11)

        self.checkBox_GUI = QCheckBox(self.configGroupBox)
        self.checkBox_GUI.setObjectName(u"checkBox_GUI")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.checkBox_GUI)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.lineEdit_id, self.comboBox_regmode)
        QWidget.setTabOrder(self.comboBox_regmode, self.spinBox_pcsToFit)
        QWidget.setTabOrder(self.spinBox_pcsToFit, self.doubleSpinBox_mWeight)
        QWidget.setTabOrder(self.doubleSpinBox_mWeight, self.tableWidgetLandmarks)
        QWidget.setTabOrder(self.tableWidgetLandmarks, self.pushButton_addLandmark)
        QWidget.setTabOrder(self.pushButton_addLandmark, self.pushButton_removeLandmark)
        QWidget.setTabOrder(self.pushButton_removeLandmark, self.doubleSpinBox_markerRadius)
        QWidget.setTabOrder(self.doubleSpinBox_markerRadius, self.doubleSpinBox_skinPad)
        QWidget.setTabOrder(self.doubleSpinBox_skinPad, self.checkBox_kneedof)
        QWidget.setTabOrder(self.checkBox_kneedof, self.checkBox_kneecorr)
        QWidget.setTabOrder(self.checkBox_kneecorr, self.checkBox_GUI)
        QWidget.setTabOrder(self.checkBox_GUI, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure 2-Sided Lower Limb Registration Step", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("Dialog", u"identifier:  ", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"Registration Mode:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"PCs to Fit:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Mahalanobis Weight:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Landmarks:", None))
        ___qtablewidgetitem = self.tableWidgetLandmarks.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Model Landmarks", None));
        ___qtablewidgetitem1 = self.tableWidgetLandmarks.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Target Landmarks", None));
        self.pushButton_addLandmark.setText(QCoreApplication.translate("Dialog", u"Add Landmark", None))
        self.pushButton_removeLandmark.setText(QCoreApplication.translate("Dialog", u"Remove Landmark", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Marker Radius:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Skin Padding:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Knee Options:", None))
        self.checkBox_kneedof.setText(QCoreApplication.translate("Dialog", u"Abd. DOF", None))
        self.checkBox_kneecorr.setText(QCoreApplication.translate("Dialog", u"Abd. Correction", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"GUI:", None))
        self.checkBox_GUI.setText("")
    # retranslateUi

