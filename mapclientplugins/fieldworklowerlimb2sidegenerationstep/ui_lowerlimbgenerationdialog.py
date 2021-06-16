# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lowerlimbgenerationdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from gias2.mappluginutils.mayaviviewer.mayaviscenewidget import MayaviSceneWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(1177, 726)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widgetMain = QWidget(Dialog)
        self.widgetMain.setObjectName("widgetMain")
        self.widgetMain.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.widgetMain)
        self.gridLayout.setObjectName("gridLayout")
        self.MayaviScene = MayaviSceneWidget(self.widgetMain)
        self.MayaviScene.setObjectName("MayaviScene")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)

        self.widget = QWidget(self.widgetMain)
        self.widget.setObjectName("widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(450, 0))
        self.widget.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName("tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 150))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(300)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.toolBox = QToolBox(self.widget)
        self.toolBox.setObjectName("toolBox")
        self.toolBox.setMinimumSize(QSize(0, 0))
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.page_2.setGeometry(QRect(0, 0, 428, 379))
        self.formLayout_3 = QFormLayout(self.page_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.tableWidgetLandmarks = QTableWidget(self.page_2)
        if (self.tableWidgetLandmarks.columnCount() < 2):
            self.tableWidgetLandmarks.setColumnCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetLandmarks.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetLandmarks.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        self.tableWidgetLandmarks.setObjectName("tableWidgetLandmarks")
        self.tableWidgetLandmarks.setMinimumSize(QSize(0, 200))
        self.tableWidgetLandmarks.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetLandmarks.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetLandmarks.horizontalHeader().setDefaultSectionSize(150)

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.tableWidgetLandmarks)

        self.label_23 = QLabel(self.page_2)
        self.label_23.setObjectName("label_23")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_23)

        self.doubleSpinBox_markerRadius = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_markerRadius.setObjectName("doubleSpinBox_markerRadius")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.doubleSpinBox_markerRadius)

        self.label_24 = QLabel(self.page_2)
        self.label_24.setObjectName("label_24")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_24)

        self.doubleSpinBox_skinPad = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_skinPad.setObjectName("doubleSpinBox_skinPad")

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.doubleSpinBox_skinPad)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_addLandmark = QPushButton(self.page_2)
        self.pushButton_addLandmark.setObjectName("pushButton_addLandmark")

        self.horizontalLayout.addWidget(self.pushButton_addLandmark)

        self.pushButton_removeLandmark = QPushButton(self.page_2)
        self.pushButton_removeLandmark.setObjectName("pushButton_removeLandmark")

        self.horizontalLayout.addWidget(self.pushButton_removeLandmark)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.toolBox.addItem(self.page_2, "Landmarks")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.page.setGeometry(QRect(0, 0, 428, 379))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.formLayout_5.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setHorizontalSpacing(2)
        self.label_14 = QLabel(self.page)
        self.label_14.setObjectName("label_14")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.label_18 = QLabel(self.page)
        self.label_18.setObjectName("label_18")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.page)
        self.label_19.setObjectName("label_19")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.doubleSpinBox_ptx = QDoubleSpinBox(self.page)
        self.doubleSpinBox_ptx.setObjectName("doubleSpinBox_ptx")
        self.doubleSpinBox_ptx.setMinimum(-10000.000000000000000)
        self.doubleSpinBox_ptx.setMaximum(10000.000000000000000)

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_ptx)

        self.doubleSpinBox_pty = QDoubleSpinBox(self.page)
        self.doubleSpinBox_pty.setObjectName("doubleSpinBox_pty")
        self.doubleSpinBox_pty.setMinimum(-10000.000000000000000)
        self.doubleSpinBox_pty.setMaximum(10000.000000000000000)

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_pty)

        self.doubleSpinBox_ptz = QDoubleSpinBox(self.page)
        self.doubleSpinBox_ptz.setObjectName("doubleSpinBox_ptz")
        self.doubleSpinBox_ptz.setMinimum(-10000.000000000000000)
        self.doubleSpinBox_ptz.setMaximum(10000.000000000000000)

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_ptz)


        self.formLayout_5.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_11)

        self.label_20 = QLabel(self.page)
        self.label_20.setObjectName("label_20")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_20)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.doubleSpinBox_prx = QDoubleSpinBox(self.page)
        self.doubleSpinBox_prx.setObjectName("doubleSpinBox_prx")
        self.doubleSpinBox_prx.setMinimum(-360.000000000000000)
        self.doubleSpinBox_prx.setMaximum(360.000000000000000)

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_prx)

        self.doubleSpinBox_pry = QDoubleSpinBox(self.page)
        self.doubleSpinBox_pry.setObjectName("doubleSpinBox_pry")
        self.doubleSpinBox_pry.setMinimum(-360.000000000000000)
        self.doubleSpinBox_pry.setMaximum(360.000000000000000)

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_pry)

        self.doubleSpinBox_prz = QDoubleSpinBox(self.page)
        self.doubleSpinBox_prz.setObjectName("doubleSpinBox_prz")
        self.doubleSpinBox_prz.setMinimum(-360.000000000000000)
        self.doubleSpinBox_prz.setMaximum(360.000000000000000)

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_prz)


        self.formLayout_5.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_12)

        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName("label_21")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_21)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.doubleSpinBox_hiplx = QDoubleSpinBox(self.page)
        self.doubleSpinBox_hiplx.setObjectName("doubleSpinBox_hiplx")
        self.doubleSpinBox_hiplx.setMinimum(-360.000000000000000)
        self.doubleSpinBox_hiplx.setMaximum(360.000000000000000)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_hiplx)

        self.doubleSpinBox_hiply = QDoubleSpinBox(self.page)
        self.doubleSpinBox_hiply.setObjectName("doubleSpinBox_hiply")
        self.doubleSpinBox_hiply.setMinimum(-360.000000000000000)
        self.doubleSpinBox_hiply.setMaximum(360.000000000000000)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_hiply)

        self.doubleSpinBox_hiplz = QDoubleSpinBox(self.page)
        self.doubleSpinBox_hiplz.setObjectName("doubleSpinBox_hiplz")
        self.doubleSpinBox_hiplz.setMinimum(-360.000000000000000)
        self.doubleSpinBox_hiplz.setMaximum(360.000000000000000)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_hiplz)


        self.formLayout_5.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_13)

        self.label_22 = QLabel(self.page)
        self.label_22.setObjectName("label_22")

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.label_22)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.doubleSpinBox_kneelx = QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneelx.setObjectName("doubleSpinBox_kneelx")
        self.doubleSpinBox_kneelx.setMinimum(-180.000000000000000)
        self.doubleSpinBox_kneelx.setMaximum(180.000000000000000)

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_kneelx)

        self.doubleSpinBox_kneely = QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneely.setObjectName("doubleSpinBox_kneely")
        self.doubleSpinBox_kneely.setMinimum(-180.000000000000000)
        self.doubleSpinBox_kneely.setMaximum(180.000000000000000)

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_kneely)

        self.doubleSpinBox_kneelz = QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneelz.setObjectName("doubleSpinBox_kneelz")
        self.doubleSpinBox_kneelz.setMinimum(-180.000000000000000)
        self.doubleSpinBox_kneelz.setMaximum(180.000000000000000)

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_kneelz)


        self.formLayout_5.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_14)

        self.doubleSpinBox_scaling = QDoubleSpinBox(self.page)
        self.doubleSpinBox_scaling.setObjectName("doubleSpinBox_scaling")
        self.doubleSpinBox_scaling.setEnabled(False)
        self.doubleSpinBox_scaling.setMinimum(-5.000000000000000)
        self.doubleSpinBox_scaling.setMaximum(5.000000000000000)
        self.doubleSpinBox_scaling.setSingleStep(0.100000000000000)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_scaling)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBox_pc1 = QDoubleSpinBox(self.page)
        self.doubleSpinBox_pc1.setObjectName("doubleSpinBox_pc1")
        self.doubleSpinBox_pc1.setMinimum(-99.000000000000000)
        self.doubleSpinBox_pc1.setMaximum(99.000000000000000)
        self.doubleSpinBox_pc1.setSingleStep(0.100000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_pc1, 1, 1, 1, 1)

        self.doubleSpinBox_pc4 = QDoubleSpinBox(self.page)
        self.doubleSpinBox_pc4.setObjectName("doubleSpinBox_pc4")
        self.doubleSpinBox_pc4.setMinimum(-99.000000000000000)
        self.doubleSpinBox_pc4.setMaximum(99.000000000000000)
        self.doubleSpinBox_pc4.setSingleStep(0.100000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_pc4, 2, 3, 1, 1)

        self.doubleSpinBox_pc3 = QDoubleSpinBox(self.page)
        self.doubleSpinBox_pc3.setObjectName("doubleSpinBox_pc3")
        self.doubleSpinBox_pc3.setMinimum(-99.000000000000000)
        self.doubleSpinBox_pc3.setMaximum(99.000000000000000)
        self.doubleSpinBox_pc3.setSingleStep(0.100000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_pc3, 2, 1, 1, 1)

        self.doubleSpinBox_pc2 = QDoubleSpinBox(self.page)
        self.doubleSpinBox_pc2.setObjectName("doubleSpinBox_pc2")
        self.doubleSpinBox_pc2.setMinimum(-99.000000000000000)
        self.doubleSpinBox_pc2.setMaximum(99.000000000000000)
        self.doubleSpinBox_pc2.setSingleStep(0.100000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_pc2, 1, 3, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 2, 1, 1)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 2, 2, 1, 1)


        self.formLayout_5.setLayout(1, QFormLayout.FieldRole, self.gridLayout_3)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName("label_5")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName("label_7")

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.doubleSpinBox_hiprx = QDoubleSpinBox(self.page)
        self.doubleSpinBox_hiprx.setObjectName("doubleSpinBox_hiprx")
        self.doubleSpinBox_hiprx.setMinimum(-360.000000000000000)
        self.doubleSpinBox_hiprx.setMaximum(360.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_hiprx)

        self.doubleSpinBox_hipry = QDoubleSpinBox(self.page)
        self.doubleSpinBox_hipry.setObjectName("doubleSpinBox_hipry")
        self.doubleSpinBox_hipry.setMinimum(-360.000000000000000)
        self.doubleSpinBox_hipry.setMaximum(360.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_hipry)

        self.doubleSpinBox_hiprz = QDoubleSpinBox(self.page)
        self.doubleSpinBox_hiprz.setObjectName("doubleSpinBox_hiprz")
        self.doubleSpinBox_hiprz.setMinimum(-360.000000000000000)
        self.doubleSpinBox_hiprz.setMaximum(360.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_hiprz)


        self.formLayout_5.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.doubleSpinBox_kneerx = QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneerx.setObjectName("doubleSpinBox_kneerx")
        self.doubleSpinBox_kneerx.setMinimum(-180.000000000000000)
        self.doubleSpinBox_kneerx.setMaximum(180.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_kneerx)

        self.doubleSpinBox_kneery = QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneery.setObjectName("doubleSpinBox_kneery")
        self.doubleSpinBox_kneery.setMinimum(-180.000000000000000)
        self.doubleSpinBox_kneery.setMaximum(180.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_kneery)

        self.doubleSpinBox_kneerz = QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneerz.setObjectName("doubleSpinBox_kneerz")
        self.doubleSpinBox_kneerz.setMinimum(-180.000000000000000)
        self.doubleSpinBox_kneerz.setMaximum(180.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_kneerz)


        self.formLayout_5.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.formLayout_5)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_manual_reset = QPushButton(self.page)
        self.pushButton_manual_reset.setObjectName("pushButton_manual_reset")

        self.horizontalLayout_15.addWidget(self.pushButton_manual_reset)

        self.pushButton_manual_accept = QPushButton(self.page)
        self.pushButton_manual_accept.setObjectName("pushButton_manual_accept")

        self.horizontalLayout_15.addWidget(self.pushButton_manual_accept)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.toolBox.addItem(self.page, "Manual Registration")
        self.page_reg = QWidget()
        self.page_reg.setObjectName("page_reg")
        self.page_reg.setGeometry(QRect(0, 0, 428, 379))
        self.verticalLayout_2 = QVBoxLayout(self.page_reg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QLabel(self.page_reg)
        self.label_13.setObjectName("label_13")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.label_11 = QLabel(self.page_reg)
        self.label_11.setObjectName("label_11")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.spinBox_pcsToFit = QSpinBox(self.page_reg)
        self.spinBox_pcsToFit.setObjectName("spinBox_pcsToFit")
        self.spinBox_pcsToFit.setMinimum(1)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.spinBox_pcsToFit)

        self.label_12 = QLabel(self.page_reg)
        self.label_12.setObjectName("label_12")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.spinBox_mWeight = QDoubleSpinBox(self.page_reg)
        self.spinBox_mWeight.setObjectName("spinBox_mWeight")
        self.spinBox_mWeight.setSingleStep(0.100000000000000)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.spinBox_mWeight)

        self.label_6 = QLabel(self.page_reg)
        self.label_6.setObjectName("label_6")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.checkBox_kneecorr = QCheckBox(self.page_reg)
        self.checkBox_kneecorr.setObjectName("checkBox_kneecorr")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.checkBox_kneecorr)

        self.label_10 = QLabel(self.page_reg)
        self.label_10.setObjectName("label_10")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.checkBox_kneedof = QCheckBox(self.page_reg)
        self.checkBox_kneedof.setObjectName("checkBox_kneedof")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.checkBox_kneedof)

        self.comboBox_regmode = QComboBox(self.page_reg)
        self.comboBox_regmode.setObjectName("comboBox_regmode")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.comboBox_regmode)


        self.verticalLayout_2.addLayout(self.formLayout_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_auto_reg = QPushButton(self.page_reg)
        self.pushButton_auto_reg.setObjectName("pushButton_auto_reg")

        self.gridLayout_2.addWidget(self.pushButton_auto_reg, 0, 0, 1, 1)

        self.pushButton_auto_abort = QPushButton(self.page_reg)
        self.pushButton_auto_abort.setObjectName("pushButton_auto_abort")

        self.gridLayout_2.addWidget(self.pushButton_auto_abort, 1, 0, 1, 1)

        self.pushButton_auto_reset = QPushButton(self.page_reg)
        self.pushButton_auto_reset.setObjectName("pushButton_auto_reset")

        self.gridLayout_2.addWidget(self.pushButton_auto_reset, 0, 1, 1, 1)

        self.pushButton_auto_accept = QPushButton(self.page_reg)
        self.pushButton_auto_accept.setObjectName("pushButton_auto_accept")

        self.gridLayout_2.addWidget(self.pushButton_auto_accept, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.errorGroup = QGroupBox(self.page_reg)
        self.errorGroup.setObjectName("errorGroup")
        self.formLayout_2 = QFormLayout(self.errorGroup)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.landmarkErrorLabel = QLabel(self.errorGroup)
        self.landmarkErrorLabel.setObjectName("landmarkErrorLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.landmarkErrorLabel)

        self.lineEdit_landmarkError = QLineEdit(self.errorGroup)
        self.lineEdit_landmarkError.setObjectName("lineEdit_landmarkError")
        self.lineEdit_landmarkError.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_landmarkError.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_landmarkError)

        self.mDistLabel = QLabel(self.errorGroup)
        self.mDistLabel.setObjectName("mDistLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.mDistLabel)

        self.lineEdit_mDist = QLineEdit(self.errorGroup)
        self.lineEdit_mDist.setObjectName("lineEdit_mDist")
        self.lineEdit_mDist.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_mDist.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_mDist)


        self.verticalLayout_2.addWidget(self.errorGroup)

        self.toolBox.addItem(self.page_reg, "Auto Registration")
        self.Screenshot = QWidget()
        self.Screenshot.setObjectName("Screenshot")
        self.Screenshot.setGeometry(QRect(0, 0, 428, 379))
        self.formLayout = QFormLayout(self.Screenshot)
        self.formLayout.setObjectName("formLayout")
        self.pixelsXLabel = QLabel(self.Screenshot)
        self.pixelsXLabel.setObjectName("pixelsXLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pixelsXLabel)

        self.screenshotPixelXLineEdit = QLineEdit(self.Screenshot)
        self.screenshotPixelXLineEdit.setObjectName("screenshotPixelXLineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.screenshotPixelXLineEdit)

        self.pixelsYLabel = QLabel(self.Screenshot)
        self.pixelsYLabel.setObjectName("pixelsYLabel")
        sizePolicy3.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pixelsYLabel)

        self.screenshotPixelYLineEdit = QLineEdit(self.Screenshot)
        self.screenshotPixelYLineEdit.setObjectName("screenshotPixelYLineEdit")
        sizePolicy4.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.screenshotPixelYLineEdit)

        self.screenshotFilenameLabel = QLabel(self.Screenshot)
        self.screenshotFilenameLabel.setObjectName("screenshotFilenameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.screenshotFilenameLabel)

        self.screenshotFilenameLineEdit = QLineEdit(self.Screenshot)
        self.screenshotFilenameLineEdit.setObjectName("screenshotFilenameLineEdit")
        sizePolicy4.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.screenshotFilenameLineEdit)

        self.screenshotSaveButton = QPushButton(self.Screenshot)
        self.screenshotSaveButton.setObjectName("screenshotSaveButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy5)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.screenshotSaveButton)

        self.toolBox.addItem(self.Screenshot, "Screenshots")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widgetMain)

        QWidget.setTabOrder(self.tableWidget, self.tableWidgetLandmarks)
        QWidget.setTabOrder(self.tableWidgetLandmarks, self.pushButton_addLandmark)
        QWidget.setTabOrder(self.pushButton_addLandmark, self.pushButton_removeLandmark)
        QWidget.setTabOrder(self.pushButton_removeLandmark, self.doubleSpinBox_markerRadius)
        QWidget.setTabOrder(self.doubleSpinBox_markerRadius, self.doubleSpinBox_skinPad)
        QWidget.setTabOrder(self.doubleSpinBox_skinPad, self.doubleSpinBox_pc1)
        QWidget.setTabOrder(self.doubleSpinBox_pc1, self.doubleSpinBox_pc2)
        QWidget.setTabOrder(self.doubleSpinBox_pc2, self.doubleSpinBox_pc3)
        QWidget.setTabOrder(self.doubleSpinBox_pc3, self.doubleSpinBox_pc4)
        QWidget.setTabOrder(self.doubleSpinBox_pc4, self.doubleSpinBox_scaling)
        QWidget.setTabOrder(self.doubleSpinBox_scaling, self.doubleSpinBox_ptx)
        QWidget.setTabOrder(self.doubleSpinBox_ptx, self.doubleSpinBox_pty)
        QWidget.setTabOrder(self.doubleSpinBox_pty, self.doubleSpinBox_ptz)
        QWidget.setTabOrder(self.doubleSpinBox_ptz, self.doubleSpinBox_prx)
        QWidget.setTabOrder(self.doubleSpinBox_prx, self.doubleSpinBox_pry)
        QWidget.setTabOrder(self.doubleSpinBox_pry, self.doubleSpinBox_prz)
        QWidget.setTabOrder(self.doubleSpinBox_prz, self.doubleSpinBox_hiplx)
        QWidget.setTabOrder(self.doubleSpinBox_hiplx, self.doubleSpinBox_hiply)
        QWidget.setTabOrder(self.doubleSpinBox_hiply, self.doubleSpinBox_hiplz)
        QWidget.setTabOrder(self.doubleSpinBox_hiplz, self.doubleSpinBox_hiprx)
        QWidget.setTabOrder(self.doubleSpinBox_hiprx, self.doubleSpinBox_hipry)
        QWidget.setTabOrder(self.doubleSpinBox_hipry, self.doubleSpinBox_hiprz)
        QWidget.setTabOrder(self.doubleSpinBox_hiprz, self.doubleSpinBox_kneelx)
        QWidget.setTabOrder(self.doubleSpinBox_kneelx, self.doubleSpinBox_kneely)
        QWidget.setTabOrder(self.doubleSpinBox_kneely, self.doubleSpinBox_kneelz)
        QWidget.setTabOrder(self.doubleSpinBox_kneelz, self.doubleSpinBox_kneerx)
        QWidget.setTabOrder(self.doubleSpinBox_kneerx, self.doubleSpinBox_kneery)
        QWidget.setTabOrder(self.doubleSpinBox_kneery, self.doubleSpinBox_kneerz)
        QWidget.setTabOrder(self.doubleSpinBox_kneerz, self.pushButton_manual_reset)
        QWidget.setTabOrder(self.pushButton_manual_reset, self.pushButton_manual_accept)
        QWidget.setTabOrder(self.pushButton_manual_accept, self.comboBox_regmode)
        QWidget.setTabOrder(self.comboBox_regmode, self.spinBox_pcsToFit)
        QWidget.setTabOrder(self.spinBox_pcsToFit, self.spinBox_mWeight)
        QWidget.setTabOrder(self.spinBox_mWeight, self.checkBox_kneecorr)
        QWidget.setTabOrder(self.checkBox_kneecorr, self.checkBox_kneedof)
        QWidget.setTabOrder(self.checkBox_kneedof, self.pushButton_auto_reg)
        QWidget.setTabOrder(self.pushButton_auto_reg, self.pushButton_auto_reset)
        QWidget.setTabOrder(self.pushButton_auto_reset, self.pushButton_auto_abort)
        QWidget.setTabOrder(self.pushButton_auto_abort, self.pushButton_auto_accept)
        QWidget.setTabOrder(self.pushButton_auto_accept, self.lineEdit_landmarkError)
        QWidget.setTabOrder(self.lineEdit_landmarkError, self.lineEdit_mDist)
        QWidget.setTabOrder(self.lineEdit_mDist, self.screenshotPixelXLineEdit)
        QWidget.setTabOrder(self.screenshotPixelXLineEdit, self.screenshotPixelYLineEdit)
        QWidget.setTabOrder(self.screenshotPixelYLineEdit, self.screenshotFilenameLineEdit)
        QWidget.setTabOrder(self.screenshotFilenameLineEdit, self.screenshotSaveButton)

        self.retranslateUi(Dialog)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "2-Sided Lower Limb Registration", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", "Visible", None));
        ___qtablewidgetitem1 = self.tableWidgetLandmarks.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", "Model Landmarks", None));
        ___qtablewidgetitem2 = self.tableWidgetLandmarks.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", "MoCap Landmarks", None));
        self.label_23.setText(QCoreApplication.translate("Dialog", "Marker Radius", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", "Skin Padding", None))
        self.pushButton_addLandmark.setText(QCoreApplication.translate("Dialog", "Add Landmark", None))
        self.pushButton_removeLandmark.setText(QCoreApplication.translate("Dialog", "Remove Landmarks", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Dialog", "Landmarks", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", "Shape Modes:", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", "Scaling:", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", "Pelvis Trans.", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", "Pelvis Rot.", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", "Hip Rot. Left", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", "Knee Rot. Left", None))
        self.label.setText(QCoreApplication.translate("Dialog", "1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", "2", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "3", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", "4", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", "Hip Rot. Right", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", "Knee Rot. Right", None))
        self.pushButton_manual_reset.setText(QCoreApplication.translate("Dialog", "Reset", None))
        self.pushButton_manual_accept.setText(QCoreApplication.translate("Dialog", "Accept", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Dialog", "Manual Registration", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", "Registration Mode:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", "PCs to Fit:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", "Mahalanobis Weight:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", "Correct Knee Abd.:", None))
        self.checkBox_kneecorr.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", "Fit Knee Abd.:", None))
        self.checkBox_kneedof.setText("")
        self.pushButton_auto_reg.setText(QCoreApplication.translate("Dialog", "Register", None))
        self.pushButton_auto_abort.setText(QCoreApplication.translate("Dialog", "Abort", None))
        self.pushButton_auto_reset.setText(QCoreApplication.translate("Dialog", "Reset", None))
        self.pushButton_auto_accept.setText(QCoreApplication.translate("Dialog", "Accept", None))
        self.errorGroup.setTitle(QCoreApplication.translate("Dialog", "Registration Results", None))
        self.landmarkErrorLabel.setText(QCoreApplication.translate("Dialog", "Landmark Error (mm RMS):", None))
#if QT_CONFIG(whatsthis)
        self.mDistLabel.setWhatsThis(QCoreApplication.translate("Dialog", "Percentage of landmarks that have converged to their texture match.", None))
#endif // QT_CONFIG(whatsthis)
        self.mDistLabel.setText(QCoreApplication.translate("Dialog", "Mahalanobis Distance:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_reg), QCoreApplication.translate("Dialog", "Auto Registration", None))
        self.pixelsXLabel.setText(QCoreApplication.translate("Dialog", "Pixels X:", None))
        self.screenshotPixelXLineEdit.setText(QCoreApplication.translate("Dialog", "800", None))
        self.pixelsYLabel.setText(QCoreApplication.translate("Dialog", "Pixels Y:", None))
        self.screenshotPixelYLineEdit.setText(QCoreApplication.translate("Dialog", "600", None))
        self.screenshotFilenameLabel.setText(QCoreApplication.translate("Dialog", "Filename:", None))
        self.screenshotFilenameLineEdit.setText(QCoreApplication.translate("Dialog", "screenshot.png", None))
        self.screenshotSaveButton.setText(QCoreApplication.translate("Dialog", "Save Screenshot", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Screenshot), QCoreApplication.translate("Dialog", "Screenshots", None))
    # retranslateUi

