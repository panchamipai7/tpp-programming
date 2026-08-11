# Beverage Kiosk – Programming Track

## Overview

The Programming track is responsible for the control and orchestration of the automated beverage compounding kiosk.

## System Flow

Cup Transit → Powder Carousel → Liquid Fluidics → Lidding → Shaking → Collection Bay

## Our Responsibilities

- Implement the overall machine state machine
- Coordinate all subsystems
- Read and process sensor feedback
- Control motors, pumps and valves
- Handle communication between Raspberry Pi and real-time controller
- Implement fault detection and recovery
- Maintain correct sequencing and timing
- Log system events and errors

## Control Architecture

### Raspberry Pi 4
Responsible for:
- High-level logic
- User interface
- Application logic
- Cloud/app communication
- Data logging

### 32-bit Real-Time Controller
Responsible for:
- Real-time sensor reading
- Motor control
- Pump and valve control
- Deterministic timing
- Safety-critical machine operations

## Machine Sequence

1. Cup dispensing
2. Powder selection and dosing
3. Liquid dispensing
4. Lid placement and sealing
5. Shaking
6. Cup delivery

## Key Requirements

- Complete the beverage cycle in less than 75 seconds
- Maintain reliable subsystem coordination
- Detect failures during operation
- Safely stop or recover from faults
- Maintain reliable communication between controllers

## Daily Engineering Log

Each day's work should record:

- What was built
- What was tested
- What failed
- What is next

## Programming Workflow

Build → Test → Debug → Commit → Push
