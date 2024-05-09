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


  // Open serial communications and wait for port to open:
  Serial.begin(4800);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  Serial.println("This is DI module");

  // set the data rate for the SoftwareSerial port
  mySerial.begin(4800);
//  mySerial.println("Hello, world?");
}

void loop() { // run over and over

  int mynodeid = "$";
  int rec_code = "0";

/*
This code is for assgning node id.
If received code is any character/code i.e 'a' then assign the next character i.e 'b' as own nodeid and pass own nodeid i.e. 'b' to next 
node to proceed further
*/


  if (mySerial.available()) {
    rec_code = mySerial.read();

    if(rec_code == 57) { //57 is ascii code of 9
      mynodeid = 48; //48 is ascii code of zero 0
    }
    else {
      mynodeid = rec_code + 1;
    }


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
    Serial.write(" ,received code at DI module is ");
    Serial.write(rec_code);
    delay(5000);   
    Serial.write(" ,allocated nodeid to DI module is "); 
    Serial.write(mynodeid);

    mySerial.write(mynodeid);


  }


/*  
  if (Serial.available()) {
    mySerial.write(Serial.read());
  }
*/
}
