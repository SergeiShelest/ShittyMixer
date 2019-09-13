from pulsectl import Pulse, PulseVolumeInfo
from pulseSinksMonitoringThread import SinksMonitoring


class pulseManagement():
    def __init__(self):
        self.pulse = Pulse('volume-mixer')

        self.SinksMonitoringThread = SinksMonitoring()

        self.addSinkInput = self.SinksMonitoringThread.addSinkInput
        self.removeSinkInput = self.SinksMonitoringThread.removeSinkInput
        self.changeVolumeInput = self.SinksMonitoringThread.changeVolumeInput

        self.addSinkOutput = self.SinksMonitoringThread.addSinkOutput
        self.removeSinkOutput = self.SinksMonitoringThread.removeSinkOutput
        self.changeVolumeOutput = self.SinksMonitoringThread.changeVolumeOutput

        self.SinksMonitoringThread.start()

    def setVolSink(self, sink, vol):
        self.pulse.volume_set(sink, PulseVolumeInfo(vol / 100, len(sink.volume.values)))
