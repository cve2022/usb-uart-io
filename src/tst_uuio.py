#! /usr/bin/env python3

from usb_uart_io import UsbUartIo
import time

def main():
    uio = UsbUartIo()
    while True:
        uio.out1(uio.inp1() or uio.inp4())
        uio.out2(uio.inp2() or uio.inp4())
        uio.out3(uio.inp3() or uio.inp4())
        time.sleep(0.2)

if __name__ == "__main__":
    main()
