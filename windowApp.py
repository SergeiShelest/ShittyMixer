from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.resize(379, 389)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon.fromTheme("multimedia-volume-control")
        MainWindow.setWindowIcon(icon)
        self.body = QtWidgets.QWidget(MainWindow)
        self.body.setObjectName("body")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.body)

        self.sinks = QtWidgets.QTabWidget(self.body)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.sinks.setFont(font)
        self.sinks.setTabPosition(QtWidgets.QTabWidget.West)
        self.sinksInput = QtWidgets.QWidget()

        self.sinksInputLayout = QtWidgets.QHBoxLayout(self.sinksInput)

        icon = QtGui.QIcon.fromTheme("audio-speakers-symbolic")
        self.sinks.addTab(self.sinksInput, icon, "")

        self.sinksOutput = QtWidgets.QWidget()

        self.sinksOutputLayout = QtWidgets.QHBoxLayout(self.sinksOutput)

        icon = QtGui.QIcon.fromTheme("audio-input-microphone-symbolic")
        self.sinks.addTab(self.sinksOutput, icon, "")

        self.horizontalLayout_41.addWidget(self.sinks)
        MainWindow.setCentralWidget(self.body)

        self.retranslateUi(MainWindow)
        self.sinks.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shitty mixer [ALPHA]"))
        self.sinks.setTabText(self.sinks.indexOf(self.sinksInput), _translate("MainWindow", "Outputs"))
        self.sinks.setTabText(self.sinks.indexOf(self.sinksOutput), _translate("MainWindow", "Inputs"))
