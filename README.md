# PWM Fan Controller with Verilog and Web UI

This project implements a PWM-based fan speed controller using Verilog HDL, integrated with a web interface for real-time control and simulation.

Features
- Control fan speed by entering duty cycle (%) and run time (seconds) from a simple web UI.
- Dynamic fan animation reflects the PWM duty cycle visually.
- Runs continuous background simulation to keep fan speed at default when idle.
- Automatically reverts to default duty cycle after specified time period.
- Simulation logs saved and accessible for review.
- Uses ModelSim for hardware simulation of the PWM module.
- Designed for easy deployment on FPGA hardware in the future.

How It Works
- User inputs desired duty cycle and time through the UI.
- Backend updates Verilog testbench with this input and runs ModelSim simulation in command line mode.
- Fan speed in UI animates according to current duty cycle (simulated or default).
- After time expires, simulation duty reverts to default (50%).
- Simulation logs provide detailed info about each run.

Technologies Used
- Verilog HDL for PWM design and testbench.
- ModelSim for HDL simulation.
- Python Flask for backend API and simulation control.
- HTML/CSS/JS for frontend UI.

Setup & Run
1. Clone this repo.
2. Install required Python packages.
3. Make sure ModelSim is installed and accessible in your system PATH.
4. Run `app.py` to start the web server.
5. Access the UI at `http://localhost:5000` and control the fan speed.


Notes
- This project can be extended for real FPGA implementation.
- The simulation demonstrates PWM behavior, which controls fan speed by adjusting the power ON time.



