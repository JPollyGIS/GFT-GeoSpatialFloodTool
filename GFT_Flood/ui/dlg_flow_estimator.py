# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_flow_estimator.ui'
#
# Created: Fri Sep 23 13:00:41 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DrainageChannelFlowEstimatorDialogBase(object):
    def setupUi(self, DrainageChannelFlowEstimatorDialogBase):
        DrainageChannelFlowEstimatorDialogBase.setObjectName(_fromUtf8("DrainageChannelFlowEstimatorDialogBase"))
        DrainageChannelFlowEstimatorDialogBase.resize(616, 644)
        DrainageChannelFlowEstimatorDialogBase.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DrainageChannelFlowEstimatorDialogBase)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_3 = QtGui.QWidget(DrainageChannelFlowEstimatorDialogBase)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 250))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.vLayout = QtGui.QVBoxLayout()
        self.vLayout.setObjectName(_fromUtf8("vLayout"))
        self.horizontalLayout_4.addLayout(self.vLayout)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.tabWidget_2 = QtGui.QTabWidget(DrainageChannelFlowEstimatorDialogBase)
        self.tabWidget_2.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 373))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox_2)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 164))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabTrap = QtGui.QWidget()
        self.tabTrap.setObjectName(_fromUtf8("tabTrap"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabTrap)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rightSS = QtGui.QDoubleSpinBox(self.tabTrap)
        self.rightSS.setMinimum(0.01)
        self.rightSS.setSingleStep(0.25)
        self.rightSS.setProperty("value", 2.0)
        self.rightSS.setObjectName(_fromUtf8("rightSS"))
        self.gridLayout_2.addWidget(self.rightSS, 1, 4, 1, 1)
        self.leftSS = QtGui.QDoubleSpinBox(self.tabTrap)
        self.leftSS.setMinimum(0.01)
        self.leftSS.setSingleStep(0.25)
        self.leftSS.setProperty("value", 2.0)
        self.leftSS.setObjectName(_fromUtf8("leftSS"))
        self.gridLayout_2.addWidget(self.leftSS, 1, 1, 1, 1)
        self.botWidth = QtGui.QDoubleSpinBox(self.tabTrap)
        self.botWidth.setMinimum(0.01)
        self.botWidth.setMaximum(999.0)
        self.botWidth.setProperty("value", 5.0)
        self.botWidth.setObjectName(_fromUtf8("botWidth"))
        self.gridLayout_2.addWidget(self.botWidth, 0, 4, 1, 1)
        self.depth = QtGui.QDoubleSpinBox(self.tabTrap)
        self.depth.setMinimum(0.01)
        self.depth.setSingleStep(0.5)
        self.depth.setProperty("value", 5.0)
        self.depth.setObjectName(_fromUtf8("depth"))
        self.gridLayout_2.addWidget(self.depth, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.tabTrap)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.tabTrap)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tabTrap)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.tabTrap)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabTrap, _fromUtf8(""))
        self.tabSample = QtGui.QWidget()
        self.tabSample.setObjectName(_fromUtf8("tabSample"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabSample)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_9 = QtGui.QLabel(self.tabSample)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.cbWSE = QtGui.QDoubleSpinBox(self.tabSample)
        self.cbWSE.setMaximum(999999.0)
        self.cbWSE.setSingleStep(0.1)
        self.cbWSE.setObjectName(_fromUtf8("cbWSE"))
        self.horizontalLayout_2.addWidget(self.cbWSE)
        self.label_8 = QtGui.QLabel(self.tabSample)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.cbDEM = QtGui.QComboBox(self.tabSample)
        self.cbDEM.setObjectName(_fromUtf8("cbDEM"))
        self.horizontalLayout_2.addWidget(self.cbDEM)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.tabSample)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.btnSampleLine = QtGui.QToolButton(self.tabSample)
        self.btnSampleLine.setObjectName(_fromUtf8("btnSampleLine"))
        self.horizontalLayout.addWidget(self.btnSampleLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_11 = QtGui.QLabel(self.tabSample)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        self.btnSampleSlope = QtGui.QToolButton(self.tabSample)
        self.btnSampleSlope.setObjectName(_fromUtf8("btnSampleSlope"))
        self.horizontalLayout_3.addWidget(self.btnSampleSlope)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tabSample, _fromUtf8(""))
        self.tabUD = QtGui.QWidget()
        self.tabUD.setObjectName(_fromUtf8("tabUD"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabUD)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_14 = QtGui.QLabel(self.tabUD)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_7.addWidget(self.label_14)
        self.cbUDwse = QtGui.QDoubleSpinBox(self.tabUD)
        self.cbUDwse.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cbUDwse.setMaximum(999999.99)
        self.cbUDwse.setSingleStep(0.1)
        self.cbUDwse.setObjectName(_fromUtf8("cbUDwse"))
        self.horizontalLayout_7.addWidget(self.cbUDwse)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_13 = QtGui.QLabel(self.tabUD)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_6.addWidget(self.label_13)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.inputFile = QtGui.QLineEdit(self.tabUD)
        self.inputFile.setObjectName(_fromUtf8("inputFile"))
        self.horizontalLayout_6.addWidget(self.inputFile)
        self.btnLoadTXT = QtGui.QToolButton(self.tabUD)
        self.btnLoadTXT.setObjectName(_fromUtf8("btnLoadTXT"))
        self.horizontalLayout_6.addWidget(self.btnLoadTXT)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tabUD, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.widget_2 = QtGui.QWidget(self.groupBox_2)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 14))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_10 = QtGui.QLabel(self.widget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(self.widget_2)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.widget)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.ft = QtGui.QRadioButton(self.widget)
        self.ft.setChecked(True)
        self.ft.setObjectName(_fromUtf8("ft"))
        self.gridLayout_6.addWidget(self.ft, 0, 0, 1, 1)
        self.m = QtGui.QRadioButton(self.widget)
        self.m.setObjectName(_fromUtf8("m"))
        self.gridLayout_6.addWidget(self.m, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget_2)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 4, 1, 1)
        self.n = QtGui.QDoubleSpinBox(self.widget_2)
        self.n.setDecimals(3)
        self.n.setMinimum(0.001)
        self.n.setSingleStep(0.005)
        self.n.setProperty("value", 0.04)
        self.n.setObjectName(_fromUtf8("n"))
        self.gridLayout_3.addWidget(self.n, 0, 5, 1, 1)
        self.slope = QtGui.QDoubleSpinBox(self.widget_2)
        self.slope.setDecimals(5)
        self.slope.setMinimum(0.0)
        self.slope.setSingleStep(1e-05)
        self.slope.setProperty("value", 0.0005)
        self.slope.setObjectName(_fromUtf8("slope"))
        self.gridLayout_3.addWidget(self.slope, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_12 = QtGui.QLabel(DrainageChannelFlowEstimatorDialogBase)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_5.addWidget(self.label_12)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.outputDir = QtGui.QLineEdit(DrainageChannelFlowEstimatorDialogBase)
        self.outputDir.setObjectName(_fromUtf8("outputDir"))
        self.horizontalLayout_5.addWidget(self.outputDir)
        self.btnBrowse = QtGui.QToolButton(DrainageChannelFlowEstimatorDialogBase)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.horizontalLayout_5.addWidget(self.btnBrowse)
        self.buttonBox = QtGui.QDialogButtonBox(DrainageChannelFlowEstimatorDialogBase)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(DrainageChannelFlowEstimatorDialogBase)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DrainageChannelFlowEstimatorDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DrainageChannelFlowEstimatorDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(DrainageChannelFlowEstimatorDialogBase)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.tabWidget, self.depth)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.depth, self.botWidth)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.botWidth, self.leftSS)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.leftSS, self.rightSS)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.rightSS, self.ft)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.ft, self.m)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.m, self.slope)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.slope, self.n)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.n, self.cbWSE)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.cbWSE, self.cbDEM)
        DrainageChannelFlowEstimatorDialogBase.setTabOrder(self.cbDEM, self.btnSampleSlope)

    def retranslateUi(self, DrainageChannelFlowEstimatorDialogBase):
        DrainageChannelFlowEstimatorDialogBase.setWindowTitle(_translate("DrainageChannelFlowEstimatorDialogBase", "Drainage Channel Flow Estimator", None))
        self.groupBox_2.setTitle(_translate("DrainageChannelFlowEstimatorDialogBase", "Inputs", None))
        self.label.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Bottom Width", None))
        self.label_3.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Water Depth", None))
        self.label_4.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Right Side Slope (width/height ratio)", None))
        self.label_2.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Left Side Slope (width/height ratio)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTrap), _translate("DrainageChannelFlowEstimatorDialogBase", "Trapezoidal Channel", None))
        self.label_9.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Water Surface Elevation", None))
        self.label_8.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "DEM", None))
        self.label_7.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Draw Cross Section (looking downstream from left to right)", None))
        self.btnSampleLine.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Draw Cross Section", None))
        self.label_11.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Use DEM to estimate slope", None))
        self.btnSampleSlope.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Estimate slope from DEM", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSample), _translate("DrainageChannelFlowEstimatorDialogBase", "Channel from DEM", None))
        self.label_14.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Water Surface Elevation", None))
        self.label_13.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Text File of Station and Elevation Values (space or tab delimited, no header)", None))
        self.btnLoadTXT.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUD), _translate("DrainageChannelFlowEstimatorDialogBase", "User Defined Channel", None))
        self.label_10.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Units", None))
        self.ft.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "ft", None))
        self.m.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "m", None))
        self.label_6.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Manning\'s Roughness Coefficent", None))
        self.label_5.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Slope of Channel", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("DrainageChannelFlowEstimatorDialogBase", "Program", None))
        self.textBrowser.setHtml(_translate("DrainageChannelFlowEstimatorDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Flow Estimator - A Uniform, Steady Open Channel Flow Calculator for QGIS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Description</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This plugin calculates flow and velocity using the Manning equation for uniform, steady flow.  <span style=\" font-weight:600;\">If you\'ve never heard of the Manning equation or taken a course in open channel hydraulics you won\'t understand what this tool is doing</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you are familar with open channel hydraulics and want a quick refresher check out this information from the Univeristy of Delaware:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http://udel.edu/~inamdar/EGTE215/Open_channel.pdf</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A great reference for Mannings n values can be found from the USGS here:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http://pubs.usgs.gov/wsp/2339/report.pdf</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">User Defined Cross Section</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The user defined cross section option allows the use of a tab or space delimited text file without a header.  The first column should contain the station values and the following column should contain elevation values.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Final Considerations</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Make sure the steady, uniform flow assumption is valid!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When sampling a DEM cross-section be sure to make the cross-section perpendicular to flow at a location that is representative of the stream or drainage channel.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When sampling DEM cross-sections and slopes, make sure the DEM is in the same CRS as the project CRS (but you knew that already right!).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("DrainageChannelFlowEstimatorDialogBase", "Documentation", None))
        self.label_12.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "Output Directory", None))
        self.btnBrowse.setText(_translate("DrainageChannelFlowEstimatorDialogBase", "...", None))

