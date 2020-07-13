#include "chimp_hw.h"
#include "chimp_demo.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
  chimp_hw_setup();
}

void loop() {
  // put your main code here, to run repeatedly:
  // chimp_demo_eyes_horizontal();
}
