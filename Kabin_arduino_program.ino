// created by KkingGz 


#include "frames.h"                      // import frames.h file
#include "Arduino_LED_Matrix.h"          // this library is only for R4



int relay2 = 2;                          // set up relay module
int relay3 = 3;
int relay4 = 4;

          
        
byte val;                                 // take commands value 
ArduinoLEDMatrix matrix;                  // Create an instance of the ArduinoLEDMatrix class

void setup() {
  Serial.begin(9600);                     // Initialize serial communication at a baud rate of 9600
  pinMode(relay2, OUTPUT);                // set up relay module
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  digitalWrite(relay2, LOW);              // set up all relay channels to LOW
  digitalWrite(relay3, LOW);
  digitalWrite(relay4, LOW);           
  matrix.begin();                         // Initialize the LED matrix **only for R4**
}

void loop() {
  while(Serial.available() > 0){          // create the loop for taking val
    val = Serial.read();                  // read val from python
    if(val == 'O'){
      matrix.loadFrame(turnOnLight);      //recieve val O from python to LightON **only for R4**
    }
    if(val == 'F'){
      matrix.loadFrame(turnOffLight);     //recieve val F from python to LightOFF **only for R4**
    }
    if(val == 'H'){
      matrix.loadFrame(happy);            //recieve val H from python to make R4 smile **only for R4**
    }
    if(val == 'A'){
      digitalWrite(relay2, HIGH);         //recieve val A from python to set relay2 HIGH 
      matrix.loadFrame(heart);
    }
    if(val == 'a'){
      digitalWrite(relay2, LOW);          //recieve val a from python to set relay2 LOW
      matrix.loadFrame(turnOffLight);
    }
    if(val == 'B'){
      digitalWrite(relay3, HIGH);         //recieve val B from python to set relay3 HIGH 
      matrix.loadFrame(heart);
    }
    if(val == 'b'){
      digitalWrite(relay3, LOW);          //recieve val b from python to set relay3 LOW 
      matrix.loadFrame(turnOffLight);
    }
    if(val == 'C'){
      digitalWrite(relay4, HIGH);         //recieve val C from python to set relay4 HIGH
      matrix.loadFrame(heart);
    }
    if(val == 'c'){
      digitalWrite(relay4, LOW);          //recieve val c from python to set relay4 LOW 
      matrix.loadFrame(turnOffLight);
    }
    if(val == 'R'){
      digitalWrite(relay2, LOW);          //recieve val R from python to set all back to setup state
      digitalWrite(relay3, LOW);
      digitalWrite(relay4, LOW);
      matrix.loadFrame(turnOffLight);
    }
  }
}