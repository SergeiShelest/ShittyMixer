from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import windowApp

from functools import partial

from customDial import Dial
from pulseManagement import pulseManagement

class ControlPanel(QtWidgets.QMainWindow, windowApp.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.volumeDial = {}
        self.volumeDialOutputs = {}

        self.pManagement = pulseManagement()

        self.pManagement.addSinkInput.connect(self.addDialIputs)
        self.pManagement.removeSinkInput.connect(self.removeDialIputs)

        self.pManagement.addSinkOutput.connect(self.addDialOutputs)
        self.pManagement.removeSinkOutput.connect(self.removeDialOutputs)

    def addDialIputs(self, sink):
        self.volumeDial[sink.index] = Dial(self.sinksInputLayout)
        self.volumeDial[sink.index].setTitle(sink.proplist["application.process.binary"])
        self.volumeDial[sink.index].setValue(int(round(sink.volume.values[0], 1)* 100))

        if "application.icon_name" in sink.proplist:
            self.volumeDial[sink.index].setIco(QtGui.QIcon.fromTheme(sink.proplist["application.icon_name"]).pixmap(48, 48))

        self.volumeDial[sink.index].dial.valueChanged.connect(partial(self.setVolumeDialIputs, sink))

    def removeDialIputs(self, sink):
        if self.volumeDial:
            self.volumeDial[sink.index].remove()
            del self.volumeDial[sink.index]

    def setVolumeDialIputs(self, sink, vol):
        self.pManagement.setVolSink(sink, vol)

    def addDialOutputs(self, sink):
        self.volumeDialOutputs[sink.index] = Dial(self.sinksOutputLayout)
        self.volumeDialOutputs[sink.index].setTitle(sink.proplist["application.process.binary"])
        self.volumeDialOutputs[sink.index].setValue(int(round(sink.volume.values[0], 1)* 100))

        if "application.icon_name" in sink.proplist:
            self.volumeDialOutputs[sink.index].setIco(QtGui.QIcon.fromTheme(sink.proplist["application.icon_name"]).pixmap(48, 48))

        self.volumeDialOutputs[sink.index].dial.valueChanged.connect(partial(self.setVolumeDialOutputs, sink))

    def removeDialOutputs(self, sink):
        self.volumeDialOutputs[sink.index].remove()
        del self.volumeDialOutputs[sink.index]

        if self.volumeDialOutputs:
            self.splitterOutputs[sink.index].deleteLater()

    def setVolumeDialOutputs(self, sink, vol):
        self.pManagement.setVolSink(sink, vol)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    app.exec_()
