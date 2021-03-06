# Jasper-Module-MQTT

Jasper MQTT Module for my [HAL9000 Raspberry PI Instructable](http://www.instructables.com/id/RaspberryPI-HAL9000/)

When triggered it publishes a simple MQTT event using the following topic:
```
hal9000/*device*/*index* 
```
Available devices:
  * device
  * room
  * light
  * sensor
  * door

Available indexes:
  * one
  * two
  * three
  * ...
  * ten

Available topic messages:
  * on
  * off
  * true
  * false
  * open
  * close


## Steps to install MQTT Module

* Install the python Mosquitto package:
```
sudo pip install paho-mqtt
```
* run the following commands in order:
```
git clone https://github.com/ArtBIT/jasper-module-mqtt.git
cp jasper-module-mqtt/Mqtt.py <path to jasper/client/modules>
#i.e. cp jasper-module-mqtt/Mqtt.py /usr/local/lib/jasper/client/modules/
```
* Edit `~/.jasper/profile.yml` and add the follwing at the bottom:
```
mqtt:
  hostname: 'your.mqtt.broker.hostname.or.ip'
  port: 1883
  protocol: 'MQTTv31' # Note: this should be either MQTTv31 or MQTTv311, I had problems with Ubuntu broker and MQTTv311
```
* Restart the Pi:
```
sudo reboot
```
## Congrats, JASPER MQTT Module is now installed and ready for use.
Here are some examples:
```
YOU: Light one off
JASPER: *publishes an mqtt event* topic:hal9000/light/one message:off
YOU: Door two close
JASPER: *publishes an mqtt event* topic:hal9000/door/two message:close
```

