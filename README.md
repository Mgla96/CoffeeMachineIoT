# FrenchPressIoT

<p align="center">
<img src="static/images/OLEDScreen.png" width="50%" alt="gif">
</p>

### About
This is an automated IoT Coffee Machine I am building that is controlled by a Raspberry Pi. When it is activated through a Siri Voice command such as "make coffee", it gathers Twitter activity from the past 24 hours from people tagging my account using the hashtags #darkroast, #mediumroast, or #lightroast and makes coffee with the roast of coffee bean that is voted on the most in the past 24 hours.
<br>
<br>
Siri is implemented through SiriControl an open source framework created by Sanjeet Chatterjee.


#### Mechanics
##### Coffee Bean Dispenser
Each servo controls an individual coffee bean dispenser. 

* GPIO-4 is Dark Roast
* GPIO-5 is Medium Roast
* GPIO-17 is Light Roast

##### Coffee Mixer
* GPIO-21 is the Mixer 

##### Hot Water Pourer
* GPIO-18 is the Hot Water Pouring Mechanism (25kg - servo)

##### Servo Linear Actuator to Start Kettle Boil
* GPIO-?