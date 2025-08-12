import time
import threading

DEFAULT_DUTY = 50
current_duty = DEFAULT_DUTY
lock = threading.Lock()

def run_simulation(duty, sim_time_sec):
    global current_duty
    with lock:
        current_duty = duty
    print(f"Simulation started for duty {duty}% for {sim_time_sec} seconds.")

    # Here you would trigger your ModelSim CLI command to simulate Verilog code

    time.sleep(sim_time_sec)

    with lock:
        current_duty = DEFAULT_DUTY
    print(f"Simulation ended. Duty reverted to default {DEFAULT_DUTY}%.")
