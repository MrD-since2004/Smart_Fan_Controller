const fan = document.getElementById('fan');
const simForm = document.getElementById('simForm');

// Map duty cycle (0-100%) to animation speed (seconds per rotation)
// Higher duty = faster rotation (shorter duration)
function dutyToSpeed(duty) {
  // Clamp duty
  duty = Math.min(Math.max(duty, 0), 100);
  // Map 0% duty to slow 6s rotation, 100% to fast 0.5s rotation
  return 6 - (duty / 100) * 5.5;
}

// Update fan speed animation based on duty
function updateFanSpeed(duty) {
  const speed = dutyToSpeed(duty);
  fan.style.animationDuration = speed + "s";
}

// Poll backend every second for current duty
async function pollDuty() {
  try {
    const res = await fetch('/get_status');
    const data = await res.json();
    updateFanSpeed(data.current_duty);
  } catch (e) {
    console.error("Error fetching duty:", e);
  }
}

setInterval(pollDuty, 1000);
pollDuty(); // initial call

// Optional: prevent form multiple submits or add UI feedback
