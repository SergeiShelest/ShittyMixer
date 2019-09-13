from pulsectl import Pulse, PulseSinkInputInfo, PulseSourceOutputInfo
from PyQt5 import QtCore


class SinksMonitoring(QtCore.QThread):

    addSinkInput = QtCore.pyqtSignal(PulseSinkInputInfo)
    removeSinkInput = QtCore.pyqtSignal(PulseSinkInputInfo)
    changeVolumeInput = QtCore.pyqtSignal(PulseSinkInputInfo)

    addSinkOutput = QtCore.pyqtSignal(PulseSourceOutputInfo)
    removeSinkOutput = QtCore.pyqtSignal(PulseSourceOutputInfo)
    changeVolumeOutput = QtCore.pyqtSignal(PulseSourceOutputInfo)

    def __init__(self):
        QtCore.QThread.__init__(self)

        self.pulse = Pulse('volume-mixer-monitor')

        self.__sinksInput = {}
        self.__sinksOutput = {}

    def run(self):
        while True:
            sinksInputNow = self.pulse.sink_input_list()
            removeSinksInput = self.__sinksInput.copy()

            for sinkNow in sinksInputNow:
                id = sinkNow.index

                if id not in self.__sinksInput:
                    self.__sinksInput[id] = sinkNow
                    self.addSinkInput.emit(sinkNow)
                else:
                    if sinkNow.volume.values != self.__sinksInput[id].volume.values:
                        self.__sinksInput[id] = sinkNow
                        self.changeVolumeInput.emit(sinkNow)

                    del removeSinksInput[id]

            for key, sink, in removeSinksInput.items():
                self.removeSinkInput.emit(sink)
                del self.__sinksInput[key]



            sinksOutputNow = self.pulse.source_output_list()
            removeSinksOutput = self.__sinksOutput.copy()

            for sinkNow in sinksOutputNow:
                id = sinkNow.index

                if id not in self.__sinksOutput:
                    self.__sinksOutput[id] = sinkNow
                    self.addSinkOutput.emit(sinkNow)
                else:
                    if sinkNow.volume.values != self.__sinksOutput[id].volume.values:
                        self.__sinksOutput[id] = sinkNow
                        self.changeVolumeOutput.emit(sinkNow)

                    del removeSinksOutput[id]

            for key, sink, in removeSinksOutput.items():
                self.removeSinkOutput.emit(sink)
                del self.__sinksOutput[key]

            self.msleep(10)

    def __del__(self):
        print("Pulse close")
        self.pulse.close()
