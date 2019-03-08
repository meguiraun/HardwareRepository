from HardwareRepository.BaseHardwareObjects import Device
import logging
import random
import gevent
import time

class TemperatureController(Device):

    def __init__(self, name):
        Device.__init__(self, name)
         logging.getLogger("HWR").info('Temperature Controller initialized.')

    def init(self):
        self._run()

    def _run(self):
        gevent.spawn(self._update_me)

    def _update_me(self):
        #TODO: periodically emit a new value

    def valueChanged(self, value):
        self.value = value
        self.emit('temperatureValueChanged', (value, ))
       
    def getState(self):
        return self.state

    def getStateDict(self):
        #TODO: return dict: state, temp, etc
        pass

    def setTemperature(self, value):
        #TODO: set temperature
        pass

    def getTemperature(self):
        #TODO: return 
        pass
