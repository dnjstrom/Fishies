// This program listens to a button and on press sends
// data continuously to the serial port for a set duration.

// Pins
int buttonPin = 7;
int pumpPin = 5;

// Input
int reading;

// Delay
long time = 0;
long debounce = 1000; //3000
int signalInterval = 20; //40
int duration = 25000;

void setup() {
  pinMode(buttonPin, INPUT);
  digitalWrite(buttonPin, HIGH); // Turn on internal resistor
  
  pinMode(pumpPin, OUTPUT);
  digitalWrite(pumpPin, LOW);  // start by turning the pump off
  
  Serial.begin(9600);
}

void loop() {
  reading = digitalRead(buttonPin);
  
  if (reading == LOW && millis() > time + debounce) {
    time = millis();
    
    digitalWrite(pumpPin, HIGH);  // turn the pump on
    
    //send signals to the visualization
    while (millis() < time + duration) {
      Serial.println('DEC');
      delay(signalInterval);
    }
    
    digitalWrite(pumpPin, LOW);  // turn the pump off
  }
}