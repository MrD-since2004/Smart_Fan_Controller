# fan_controller.py

def control_fan(temp):
    """
    Decide fan speed (0-100%) based on temperature.
    Returns an integer percentage.
    """
    if temp is None:
        return 0           # No reading -> fan off
    if temp < 25:
        return 0           # Below 25°C -> fan off
    elif temp < 30:
        return 50          # Between 25°C and 29°C -> medium speed
    else:
        return 100         # 30°C or higher -> full speed
