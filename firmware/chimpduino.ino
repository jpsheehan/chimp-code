#include "chimp_hw.h"
#include "chimp_demo.h"
#include "chimp_ctl.h"

void setup() {
  // put your setup code here, to run once:

  chimp_ctl_setup();
  chimp_hw_setup();
}

void loop() {
  // put your main code here, to run repeatedly:
//     chimp_demo_eyes_horizontal();
//     chimp_demo_eyelids();
//     chimp_demo_jaw();
//     chimp_demo_eyebrows();

   chimp_ctl_process();

}
