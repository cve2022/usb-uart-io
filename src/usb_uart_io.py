#! /usr/bin/env python3

from serial import Serial

IN1, IN2, IN3, IN4 = range(4)
OUT1, OUT2, OUT3 = range(3)
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

    def out(self, id, state):
        if id == OUT1:
            self.dtr = state
        elif id == OUT2:
            self.rts = state
        elif id == OUT3:
            self.break_condition = state
        else:
            pass # do nothing

    def inp(self, id):
        if id == IN1:
            return self.cts
        elif id == IN2:
            return self.dsr
        elif id == IN3:
            return self.cd
        elif id == IN4:
            return self.ri
        else:
            return OFF
