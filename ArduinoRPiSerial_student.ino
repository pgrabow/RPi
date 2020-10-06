// File: ArduinoRPiSerial_pot.ino
// Python files: ArduinoRPiSerial_student.py
// Date: 10/6/20
// Description: Transfers an array of a particular size between
//              the Arduino and the RPi
/* Assumptions:
      - the array passed between Python and Arduino is always of length 10
      - this code will ultimately show use of both sensor and motor data
*/
#include "SerialTransfer.h"

SerialTransfer myTransfer;

// Transfer constants and variables
const uint16_t ARRAY_SIZE = 10;
const uint16_t INT_SIZE = 4;
uint16_t varArray[ARRAY_SIZE] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

// ==================================================
void setup()
{
  Serial.begin(115200);
  myTransfer.begin(Serial);
}

// ==================================================
void loop()
{

  uint16_t returnSize = 0;
  uint16_t sendSize = 0;
  uint16_t sensorValue = 0;
  uint16_t voltage = 0;
  int index = 0;

  while ( true ) {
    if (myTransfer.available())
    {
      // Extract values from buffer
      // ------------------------------------
      receive_array(ARRAY_SIZE, varArray);

      // Insert 4 times the voltage into index 1
      index = 1;
      varArray[index] = get_voltage() * 4;

      transmit_array(ARRAY_SIZE, varArray);
      delay(500);
    }
  }
}

// ------------------------------------------------
void receive_array(const int size, int16_t tmpArray[]) {
  int16_t returnSize = 0;
  for (int i = 0; i < size; i++) {
    returnSize = myTransfer.rxObj(tmpArray[i], i * INT_SIZE);
  }
}

// ------------------------------------------------
void transmit_array(const int size, int16_t tmpArray[]) {
  int16_t sendSize = 0;
  for (int j = 0; j < size; j++) {
    sendSize = myTransfer.txObj(varArray[j], j * INT_SIZE);
  }
  myTransfer.sendData(INT_SIZE * sendSize);
}

// ------------------------------------------------
uint16_t get_voltage() {
  const int analogInPin = A0;
  const int analogOutPin = 9;

  // Your code goes here
}
