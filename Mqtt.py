# -*- coding: utf-8-*-
# vim: set expandtab:ts=4:sw=4:ft=python
import re

import paho.mqtt.publish as publish

NUMBERS = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
           "SEVEN", "EIGHT", "NINE", "TEN"]
DEVICES = ["DEVICE", "ROOM", "LIGHT", "SENSOR", "DOOR"]
PAYLOADS = ["ON", "OFF", "TRUE", "FALSE", "OPEN", "CLOSE", "STATUS"]

WORDS = ["MOSQUITTO"] + DEVICES + NUMBERS + PAYLOADS
PRIORITY = 4


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by sending a
        mosquitto publish event
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    words = text.split(' ')
    if words[0] not in DEVICES:
        return mic.say(words[0]+" not found in the list of devices")
    if words[1] not in NUMBERS:
        return mic.say(words[1]+" not found in the list of valid indexes")
    if words[2] not in PAYLOADS:
        return mic.say(words[2]+" is not found in the list of valid payloads")
    topic = '/'.join(['hal9000']+words[0:1])
    publish.single(topic, words[2],
                   hostname=profile['mqtt']['broker_hostname'])


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(mosquitto)\b', text, re.IGNORECASE))
