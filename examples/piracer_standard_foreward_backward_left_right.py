import time
from piracer.vehicles import PiRacerStandard


if __name__ == '__main__':

    piracer = PiRacerStandard()

    # time.sleep(1.0)

    # Forward
    piracer.set_throttle_percent(0.9)
    time.sleep(2.0)

    # Backward
    piracer.set_throttle_percent(-0.9)
    time.sleep(2.0)

    # Stop
    piracer.set_throttle_percent(0.0)

    # Steering left
    piracer.set_steering_percent(1.0)
    time.sleep(1.0)

    # Steering right
    piracer.set_steering_percent(-1.0)
    time.sleep(1.0)

    # Steering neutral
    piracer.set_steering_percent(0.0)
