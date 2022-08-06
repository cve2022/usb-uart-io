# usb-uart-io

A simple example of the use of Python to control and monitor external devices from a PC through a USB-UART converter with C-MOS/TTL inputs/outputs.

Constituted by a class that abstracts the USB-UART converter inputs and outputs to generic I/Os and an simple test script that monitors inputs and controls the relays according to the states of the corresponding inputs.

Inputs and outputs are based on negative logic, i.e., active in zero low logic/voltage level.

Tested with adapters based on FT232RL and CP2101N.

There are two short videos showing the code in action with two different USB-Serial converters, [CP2102N](https://youtu.be/8ubaLk3z_3o) and [FT232RL](https://youtu.be/_RM3ibkgs64), that show the code in action.
