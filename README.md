# raspberry-pi-i2c-clock
Clock running on Raspberry PI with 16x2 LCD I2C interface 

## Enable I2C Interface on raspberry pi
```
sudo raspi-config
Interfacing Option -> I2C -> Enable
```

## Install following python modules
```
sudo apt-get install python-pip
pip install ics
pip install requests
pip install RPLCD
pip install smbus
```

## Connections
|Raspberry PI | I2C LCD |
|---|---|
|5v|VCC|
|GND|GND|
|SDA|SDA|
|SCL|SCL|

## Checkout code using git clone

## Setup cron job
Run cronjob every two minutes

0/2 * * * * <basepath>/raspberry-pi-i2c-clock/clockmonitor.sh
