# Beverage Control

## Architecture
The Raspberry Pi handles high-level control, Flask API and communication with the MCU
The MCU handles real-time motor, pump and sensor control

Pi -> UART -> MCU

## API

### Start Cycle
POST /start
Starts a new beverage cycle

### Check Status
GET /status
Returns the current machine status
Example:
{
  "status": "RUNNING"
}

## Protocol
The Raspberry Pi communicates with the MCU using UART
Example command:
DISPENSE 2 30
The MCU replies with:
ACK
and then:
WEIGHT 30.2

## Known Limitations
Only basic START and STATUS endpoints are implemented
The API currently supports one cycle at a time
Status updates are simple and not real-time
Error handling and automatic recovery are still basic
The API has only been tested on the local network
