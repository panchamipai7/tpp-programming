# RPi-MCU Dispense Protocol

## Communication
RPi and MCU communicate using UART at 9600 baud.

## Command
DISPENSE <canister> <weight>

Example:
DISPENSE 2 30
This means dispense 30 g from canister 2.

## MCU Response
ACK
- Command received successfully.

WEIGHT <value>
- Final weight after dispensing.

Example:
WEIGHT 30.2

## Communication Flow
RPi -> DISPENSE 2 30
MCU -> ACK
MCU -> WEIGHT 30.2

## Timeout
The RPi waits for a response for 2 seconds.
If no response is received, the command is considered failed.
