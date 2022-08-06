FROM  piandarduinoguy/raspbian-bullseye-python3-pip
WORKDIR /hardware-security-controller
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt
COPY src .
RUN mkdir "/hardware-security-controller/logs" \
    && ln -sf /dev/stdout /hardware-security-controller/logs/hardware-security-controller.log
RUN raspi-config nonint do_i2c 0 # enable i2c interface
CMD ["python3", "./main.py"]