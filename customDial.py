from PyQt5 import QtGui, QtCore, QtWidgets

class Dial():
    def __init__(self, parent=None):
        self.parent = parent

        self.createWidget()

    def createWidget(self):
        self.fontTitle = QtGui.QFont()
        self.fontTitle.setPointSize(12)

        self.font = QtGui.QFont()
        self.font.setPointSize(16)

        self.titleIco = QtWidgets.QLabel()
        self.titleIco.setMaximumSize(QtCore.QSize(48, 48))
        self.titleIco.setPixmap(QtGui.QPixmap("/usr/share/icons/breeze-dark/devices/64/audio-card.svg"))
        self.titleIco.setScaledContents(True)

        self.titleTxt = QtWidgets.QLabel()
        self.titleTxt.setText("Title")
        self.titleTxt.setFont(self.fontTitle)
        self.titleTxt.setAlignment(QtCore.Qt.AlignCenter)

        self.titleBody = QtWidgets.QHBoxLayout()
        self.titleBody.setContentsMargins(5, 0, 5, 0)
        self.titleBody.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.titleBody.addWidget(self.titleIco)
        self.titleBody.addItem(QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.titleBody.addWidget(self.titleTxt)
        self.titleBody.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.dial = QtWidgets.QDial()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy)
        self.dial.setMinimumSize(QtCore.QSize(180, 180))
        self.dial.setMaximumSize(QtCore.QSize(240, 240))
        self.dial.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dial.setMaximum(100)

        self.dialBody = QtWidgets.QHBoxLayout()
        self.dialBody.setSpacing(0)
        self.dialBody.addWidget(self.dial)

        self.dialLabel = QtWidgets.QLabel()
        self.dialLabel.setText("0 %")
        self.dialLabel.setFont(self.font)
        self.dialLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.dial.valueChanged.connect(self.changeDialValue)

        self.body = QtWidgets.QVBoxLayout()
        self.body.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.body.setSpacing(0)
        self.body.addLayout(self.titleBody)
        self.body.addLayout(self.dialBody)
        self.body.addWidget(self.dialLabel)

        self.parent.addLayout(self.body)

    def changeDialValue(self, s):
        self.dialLabel.setText(str(s) + " %")

    def setValue(self, val):
        self.dial.setProperty("value", val)

    def setTitle(self, title):

        if len(title) > 7:
            title = title[0:6] + "..."

        self.titleTxt.setText(title)

    def setIco(self, pixmap):
        self.titleIco.setPixmap(pixmap)

    def remove(self):
        self.titleBody.deleteLater()
        self.dialBody.deleteLater()
        self.dialLabel.deleteLater()
        self.titleIco.deleteLater()
        self.titleTxt.deleteLater()
        self.dial.deleteLater()
        self.body.deleteLater()