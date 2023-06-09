# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 60, 720, 530))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 50, 131, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LineButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineButton.sizePolicy().hasHeightForWidth())
        self.LineButton.setSizePolicy(sizePolicy)
        self.LineButton.setMinimumSize(QtCore.QSize(30, 30))
        self.LineButton.setMaximumSize(QtCore.QSize(30, 30))
        self.LineButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("project/icons/layer-shape-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LineButton.setIcon(icon)
        self.LineButton.setCheckable(True)
        self.LineButton.setObjectName("LineButton")
        self.gridLayout.addWidget(self.LineButton, 2, 0, 1, 1)
        self.CircleButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CircleButton.sizePolicy().hasHeightForWidth())
        self.CircleButton.setSizePolicy(sizePolicy)
        self.CircleButton.setMinimumSize(QtCore.QSize(30, 30))
        self.CircleButton.setMaximumSize(QtCore.QSize(30, 30))
        self.CircleButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("project/icons/layer-shape-ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CircleButton.setIcon(icon1)
        self.CircleButton.setCheckable(True)
        self.CircleButton.setObjectName("CircleButton")
        self.gridLayout.addWidget(self.CircleButton, 3, 0, 1, 1)
        self.ColorButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ColorButton.setObjectName("ColorButton")
        self.gridLayout.addWidget(self.ColorButton, 6, 0, 1, 1)
        self.BrushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrushButton.sizePolicy().hasHeightForWidth())
        self.BrushButton.setSizePolicy(sizePolicy)
        self.BrushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.BrushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.BrushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("project/icons/paint-brush.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BrushButton.setIcon(icon2)
        self.BrushButton.setCheckable(True)
        self.BrushButton.setObjectName("BrushButton")
        self.gridLayout.addWidget(self.BrushButton, 1, 0, 1, 1)
        self.PenButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PenButton.sizePolicy().hasHeightForWidth())
        self.PenButton.setSizePolicy(sizePolicy)
        self.PenButton.setMinimumSize(QtCore.QSize(30, 30))
        self.PenButton.setMaximumSize(QtCore.QSize(30, 30))
        self.PenButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("project/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PenButton.setIcon(icon3)
        self.PenButton.setCheckable(True)
        self.PenButton.setObjectName("PenButton")
        self.gridLayout.addWidget(self.PenButton, 0, 0, 1, 1)
        self.EraseButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EraseButton.sizePolicy().hasHeightForWidth())
        self.EraseButton.setSizePolicy(sizePolicy)
        self.EraseButton.setMinimumSize(QtCore.QSize(30, 30))
        self.EraseButton.setMaximumSize(QtCore.QSize(30, 30))
        self.EraseButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("paint/icons/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EraseButton.setIcon(icon4)
        self.EraseButton.setCheckable(True)
        self.EraseButton.setObjectName("EraseButton")
        self.gridLayout.addWidget(self.EraseButton, 4, 0, 1, 1)
        self.CopyButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CopyButton.sizePolicy().hasHeightForWidth())
        self.CopyButton.setSizePolicy(sizePolicy)
        self.CopyButton.setMinimumSize(QtCore.QSize(30, 30))
        self.CopyButton.setMaximumSize(QtCore.QSize(30, 30))
        self.CopyButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("paint/icons/selection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CopyButton.setIcon(icon5)
        self.CopyButton.setCheckable(True)
        self.CopyButton.setObjectName("CopyButton")
        self.gridLayout.addWidget(self.CopyButton, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 660, 31, 28))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 700, 31, 28))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 740, 31, 28))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(100, 660, 841, 22))
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(100, 700, 841, 22))
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setProperty("value", 100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(100, 740, 841, 22))
        self.spinBox_3.setMaximum(100)
        self.spinBox_3.setProperty("value", 100)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(950, 660, 21, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(950, 700, 21, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(950, 740, 21, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(970, 700, 81, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 620, 71, 16))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 26))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("paint/icons/document-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon6)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("paint/icons/blue-folder-open-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon7)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("paint/icons/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon8)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionrotate_by_90 = QtWidgets.QAction(MainWindow)
        self.actionrotate_by_90.setObjectName("actionrotate_by_90")
        self.actionrotate_by_180 = QtWidgets.QAction(MainWindow)
        self.actionrotate_by_180.setObjectName("actionrotate_by_180")
        self.actionrotate_by_270 = QtWidgets.QAction(MainWindow)
        self.actionrotate_by_270.setObjectName("actionrotate_by_270")
        self.actionInvert_Colors = QtWidgets.QAction(MainWindow)
        self.actionInvert_Colors.setObjectName("actionInvert_Colors")
        self.actionFlip_Horizontal_2 = QtWidgets.QAction(MainWindow)
        self.actionFlip_Horizontal_2.setObjectName("actionFlip_Horizontal_2")
        self.actionFlip_Vertical_2 = QtWidgets.QAction(MainWindow)
        self.actionFlip_Vertical_2.setObjectName("actionFlip_Vertical_2")
        self.actionClear_Image = QtWidgets.QAction(MainWindow)
        self.actionClear_Image.setObjectName("actionClear_Image")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionrotate_by_90)
        self.menuEdit.addAction(self.actionrotate_by_180)
        self.menuEdit.addAction(self.actionrotate_by_270)
        self.menuEdit.addAction(self.actionInvert_Colors)
        self.menuEdit.addAction(self.actionFlip_Horizontal_2)
        self.menuEdit.addAction(self.actionFlip_Vertical_2)
        self.menuEdit.addAction(self.actionClear_Image)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "paint"))
        self.ColorButton.setText(_translate("MainWindow", "Выбрать цвет"))
        self.label_2.setText(_translate("MainWindow", "%"))
        self.label_3.setText(_translate("MainWindow", "%"))
        self.label_4.setText(_translate("MainWindow", "%"))
        self.pushButton_5.setText(_translate("MainWindow", "Применить"))
        self.label_5.setText(_translate("MainWindow", "Затемнение"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionrotate_by_90.setText(_translate("MainWindow", "rotate by 90"))
        self.actionrotate_by_180.setText(_translate("MainWindow", "rotate by 180"))
        self.actionrotate_by_270.setText(_translate("MainWindow", "rotate by 270"))
        self.actionInvert_Colors.setText(_translate("MainWindow", "Invert Colors"))
        self.actionFlip_Horizontal_2.setText(_translate("MainWindow", "Flip Horizontal"))
        self.actionFlip_Vertical_2.setText(_translate("MainWindow", "Flip Vertical"))
        self.actionClear_Image.setText(_translate("MainWindow", "Clear Image"))
