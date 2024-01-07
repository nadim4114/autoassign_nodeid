/*
  Software serial multiple serial test

 Receives from the hardware serial, sends to software serial.
 Receives from software serial, sends to hardware serial.

 The circuit:
 * RX is digital pin 10 (connect to TX of other device)
 * TX is digital pin 11 (connect to RX of other device)

 Note:
 Not all pins on the Mega and Mega 2560 support change interrupts,
 so only the following can be used for RX:
 10, 11, 12, 13, 50, 51, 52, 53, 62, 63, 64, 65, 66, 67, 68, 69

 Not all pins on the Leonardo and Micro support change interrupts,
 so only the following can be used for RX:
 8, 9, 10, 11, 14 (MISO), 15 (SCK), 16 (MOSI).

 created back in the mists of time
 modified 25 May 2012
 by Tom Igoe
 based on Mikal Hart's example

 This example code is in the public domain.

 */
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  

  // Open serial communications and wait for port to open:
  Serial.begin(4800);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  
  }

  Serial.println("This is Coupler");

  // set the data rate for the SoftwareSerial port
  mySerial.begin(4800);
//  mySerial.println("Hello, world?");
}

void loop() { // run over and over

  int send_code = 48;
  bool iFl_Alt = 0;
/*
This code is for assgning node id.
If received code is any character/code i.e 'a' then assign the next character i.e 'b' as own nodeid and pass own nodeid i.e. 'b' to next 
node to proceed further
*/
//    mySerial.write(" ,This is coupler ");
    mySerial.write(send_code);
    //LED Toggle code
    if (iFl_Alt == 0) {
      digitalWrite(LED_BUILTIN, HIGH); // turn the LED on (HIGH is the voltage level)
      iFl_Alt = 1;

      Serial.write(" This is Coupler with Node /n");
      Serial.write(send_code);
    }
    else {
      digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
      iFl_Alt = 0;
    }
    // Wait for 5 seconds before sending next message
    delay(2000); 
 

               


/*    
    println(rec_code)
    if(rec_code =="a") {
      mynodeid = "'A' + 1";
    }
    if(rec_code =="b") {
      mynodeid = "c";
    }
    if(rec_code =="c") {
      mynodeid = "d";
    }
    if(rec_code =="d") {
      mynodeid = "e";
    }
    else{
      mynodeid = "n";
    } 
  */ 

  }


/*  
  if (Serial.available()) {
    mySerial.write(Serial.read());
  }
*/

