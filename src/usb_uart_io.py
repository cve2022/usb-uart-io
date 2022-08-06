#! /usr/bin/env python3

from serial import Serial

ON, OFF = True, False

class UsbUartIo(Serial):
    def __init__(self, port='/dev/ttyUSB0'):
        super().__init__(port)
        self.dtr = False
        self.rts = False

    def __del__(self):
        self.break_condition = False
        self.dtr = False
        self.rts = False
        super().__del__()

    def out1(self, state):
        self.dtr = state

    def out2(self, state):
        self.rts = state

    def out3(self, state):
        self.break_condition = state

    def inp1(self):
        return self.cts

    def inp2(self):
        return self.dsr

    def inp3(self):
        return self.cd

    def inp4(self):
        return self.ri
