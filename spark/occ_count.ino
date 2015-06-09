// Include the library for communicating with our ultrasonic sesnor.
#include "HC_SR04/HC_SR04.h"

/* This code uses two ultrasonic range finders (HC-SR04's) to determine the direction
   of movement by the device.  It then publishes the change in occupancy count to the
   particle cloud via webhooks which will alert our web app of the change.
 
 
        The circuit:
            * VCC connection of the sensor attached to Vin of spark
                WARNING:  Make sure you are powering from a 5V source capable of
                suppling at least 330mA of current.  A typical phone charger or
                computer USB should meet these requirements.
            * GND connection of the sensor attached to GND of spark
            // These must all be on pins capable of handling 5v, but ECHO can still only
            // measure up to 3.3v on spark, so use voltage divider here at the
            // expense of some resolution.  Brings 5v down to 2.5v.
            * TRIG connection of sensor0 attached to D0 
            * TRIG connection of sensor1 attached to D1
            * ECHO connection of sensor0 attached to D3
            * ECHO connection of sensor1 attached to D4
 */

// Pins used by the ultrasonic sensors, must be capable of handling 5V.
// Pin D2 is not.
const int trigPin[] = {D0,D1};
const int echoPin[] = {D3,D4};

// Variable to store the change in occupancy count since last synced with the cloud.
int occ_change = 0;
// Variables to store the duration of the pin, and the resulting distance in cm.
double cm[2];

/*
The default usable rangefinder is 10cm to 250cm. Outside of that range -1 is returned as the distance.
You can change this range by supplying two extra parameters to the constructor of minCM and maxCM, like this:
HC_SR04 rangefinder = HC_SR04(trigPin, echoPin, 5.0, 300.0);
This constructor also handles pinMode setup ect.
*/
HC_SR04 rangefinder0 = HC_SR04(trigPin[0], echoPin[0],5.0,300.0);



void setup() {
    Spark.variable("cm", &cm[0], DOUBLE);
}

void loop() {
   cm[0] = rangefinder0.getDistanceCM();
   delay(100);
}