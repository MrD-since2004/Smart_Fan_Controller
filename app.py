from flask import Flask, render_template, request, redirect, jsonify
import threading
import time

app = Flask(__name__)

DEFAULT_DUTY = 50  # Default duty %
current_duty = DEFAULT_DUTY
lock = threading.Lock()

def simulation_thread(duty, sim_time_sec):
    global current_duty
    with lock:
        current_duty = duty
    print(f"Simulation started for duty {duty}% for {sim_time_sec} seconds.")
    
    # Here you can trigger your ModelSim simulation command, if needed
    
    time.sleep(sim_time_sec)
    
    with lock:
        current_duty = DEFAULT_DUTY
    print(f"Simulation ended. Duty reverted to default {DEFAULT_DUTY}%.")

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_duty
    if request.method == 'POST':
        duty = request.form.get('duty')
        sim_time = request.form.get('time')
        try:
            duty = int(duty)
            sim_time = int(sim_time)
            if duty < 0 or duty > 100 or sim_time <= 0:
                raise ValueError
        except Exception:
            return "Invalid input", 400
        
        # Start simulation thread
        threading.Thread(target=simulation_thread, args=(duty, sim_time), daemon=True).start()
        return redirect('/')
    
    with lock:
        duty_now = current_duty
    return render_template('index.html', default_duty=DEFAULT_DUTY, current_duty=duty_now)

@app.route('/get_status')
def get_status():
    with lock:
        duty_now = current_duty
    return jsonify({"duty": duty_now})

if __name__ == '__main__':
    app.run(debug=True)
