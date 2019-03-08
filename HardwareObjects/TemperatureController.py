from HardwareRepository.BaseHardwareObjects import Device
import logging
import random
import gevent
import time

class TemperatureController(Device):

    def __init__(self, name):
        Device.__init__(self, name)
        self.state = 'READY'
        self.temperature = 4.534
        self.powered = True
        logging.getLogger("HWR").info('Temperature Controller initialized.')

    def init(self):
        self._run()

    def _run(self):
        gevent.spawn(self._update_me)

    def _update_me(self):
        self.t0 = time.time()

        while True:
            gevent.sleep(5)
            elapsed = time.time() - self.t0
            temp = self.getTemperature()
            self.valueChanged(temp)

    def valueChanged(self, value):
        self.value = value
        self.emit('temperatureValueChanged', (value, ))
       
    def getState(self):
        return self.state

    def getStateDict(self):
        state = {
            'state': self.state,
            'value': self.getTemperature(),
            'powered': self.powered
        }
        return state

    def setTemperature(self, value):
        self.temperature = value
        self.valueChanged(temperature)

    def getTemperature(self):
        return self.temperature + random.random()

    def powerOn(self):
        self.powered = True
        self.state = 'READY'

    def powerOff(self):
        self.powered = False
        self.state = 'DISABLED'
