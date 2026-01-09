# Command-Line Stopwatch

## Overview
This project is a Python-based command-line stopwatch application that allows users to start, stop, reset, and monitor elapsed time in real time. It demonstrates object-oriented programming and basic event-driven control using standard Python libraries.

The stopwatch updates the elapsed time every second while running and responds to user commands via the terminal.

## How It Works
The stopwatch is implemented as a `StopWatch` class that manages start time, elapsed time, and running state.  
The program listens for user input commands and updates the stopwatch accordingly.

While the stopwatch is running, it:
- Continuously displays elapsed time every second
- Non-blockingly checks for user input to allow stopping or resetting

## Tech Stack
- Language: Python  
- Libraries:
  - `time` – high-resolution timing
  - `sys`, `select` – non-blocking input handling

## Features
- Start, stop, and reset functionality
- Real-time elapsed time display
- Accurate timing using `time.perf_counter()`
- Non-blocking input handling
- Object-oriented design

## How to Run
1. Ensure Python is installed on your system  
2. Save the script as `stopwatch.py`  
3. Run the program:
   ```bash
   python stopwatch.py
