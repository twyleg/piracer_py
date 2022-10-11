# PiRacer-Py

This package will provide you with a simple abstraction layer for the PiRacer development platform.
You will be able to control the powertrain and the steering as easy as possible.

I also provides an easy way to grab images from the camera (based on v4l2 and opencv)

## Install

Tested on the following Hardware:

* Raspberry Pi 4 Model B 4GB

Tested on the following distributions:

* Ubuntu Server 20.04.5 LTS (64-Bit)

### Add source (Ubuntu only)

If you run **Ubuntu**, add the following sources first:

    sudo -s
    echo "deb http://archive.raspberrypi.org/debian/ buster main" >> /etc/apt/sources.list
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7FA3303E
    apt update
    mount /dev/mmcblk0p1 /boot/
    exit 

### Install dependencies:

    sudo apt update
    sudo apt install \
        v4l-utils \
        i2c-tools \
        raspi-config \
        python3-dev \
        python3-venv \
        libopencv-dev

### Setup periphery 

Use the **raspi-config** tool to enable the following peripherals:

* i2c: Interface Options > I2C
* Camera: Interface Options > Camera

Afterwards, reboot:
    
    sudo reboot

### Install piracer-py package

    cd ~
    mkdir piracer_test/
    cd piracer_test/
    python3 -m venv venv
    source venv/bin/ativate

    pip install piracer-py

## Examples

The following examples will show the basic functionality of the piracer-py package.
Make sure the virtual environment from step **Install piracer-py package** is activated.

### Basic example

This basic example will test the power train and the steering.

Paste the following code into **basic_example.py**

    import time
    from piracer.vehicles import PiRacerPro

    if __name__ == '__main__':
    
        piracer = PiRacerPro()
        # piracer = PiRacerStandard()
    
        # Forward
        piracer.set_throttle_percent(0.2)
        time.sleep(2.0)
    
        # Brake
        piracer.set_throttle_percent(-1.0)
        time.sleep(0.5)
        piracer.set_throttle_percent(0.0)
        time.sleep(0.1)
    
        # Backward
        piracer.set_throttle_percent(-0.3)
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


Run it with:

    python basic_example.py

### Remote control example

The following example will let you control the PiRacer with the ShanWan Gamepad 
that is shipped with the PiRacer package. Make sure the dongle is connected to your Raspberry Pi.

Paste the following code into **rc_example.py**:

    from piracer.vehicles import PiRacerPro
    from piracer.gamepads import ShanWanGamepad

    if __name__ == '__main__':
    
        shanwan_gamepad = ShanWanGamepad()
        piracer = PiRacerPro()
        # piracer = PiRacerStandard()
    
        while True:
            gamepad_input = shanwan_gamepad.read_data()
    
            throttle = gamepad_input.analog_stick_right.y * 0.5
            steering = -gamepad_input.analog_stick_left.x
    
            print(f'throttle={throttle}, steering={steering}')
    
            piracer.set_throttle_percent(throttle)
            piracer.set_steering_percent(steering)

Run it with:

    python rc_example.py

### Grab images example

With the following example you can grab and save images from the Raspberry Pi camera.

Paste the following code into **camera_grab_example.py**:

    import cv2
    from piracer.cameras import Camera, MonochromeCamera
    
    if __name__ == '__main__':
        camera = MonochromeCamera()
    
        image = camera.read_image()
        cv2.imwrite('image.png', image)

Run it with:

    python camera_grab_example.py
