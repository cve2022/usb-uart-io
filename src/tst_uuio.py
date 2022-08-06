#! /usr/bin/env python3

from usb_uart_io import UsbUartIo
from usb_uart_io import IN1, IN2, IN3, IN4
from usb_uart_io import OUT1, OUT2, OUT3
import time

def main():
    uio = UsbUartIo()
    while True:
        uio.out(OUT1, uio.inp(IN1) or uio.inp(IN4))
        uio.out(OUT2, uio.inp(IN2) or uio.inp(IN4))
        uio.out(OUT3, uio.inp(IN3) or uio.inp(IN4))
        time.sleep(0.2)

if __name__ == "__main__":
    main()
