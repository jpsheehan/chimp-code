#include <Arduino.h>

#include "chimp_demo.h"
#include "chimp_hw.h"

void chimp_demo_eyes_horizontal(void)
{
  // LOOK LEFT  
  chimp_hw_move_eyes_horizontal(HDIR_LEFT);
  delay(300);
  chimp_hw_move_eyes_horizontal(HDIR_NEUTRAL);
  delay(1000);

  // LOOK RIGHT
  chimp_hw_move_eyes_horizontal(HDIR_RIGHT);
  delay(300);
  chimp_hw_move_eyes_horizontal(HDIR_NEUTRAL);
  delay(1000);
}

void chimp_demo_eyes_vertical(void)
{
  // LOOK UP
  chimp_hw_move_eyes_vertical(VDIR_UP);
  delay(350);
  chimp_hw_move_eyes_vertical(VDIR_NEUTRAL);
  delay(1000);

  // LOOK DOWN
  chimp_hw_move_eyes_vertical(VDIR_DOWN);
  delay(350);
  chimp_hw_move_eyes_vertical(VDIR_NEUTRAL);
  delay(1000);
}

void chimp_demo_eyelids(void)
{

  // EYES CLOSE
  chimp_hw_move_eyelids(DIR_CLOSE);
  delay(400);
  chimp_hw_move_eyelids(DIR_NEUTRAL);
  delay(1000);

  // EYES OPEN
  chimp_hw_move_eyelids(DIR_OPEN);
  delay(400);
  chimp_hw_move_eyelids(DIR_NEUTRAL);
  delay(1000);
}

void chimp_demo_jaw(void)
{

  // JAW CLOSE
  chimp_hw_move_jaw(DIR_CLOSE);
  delay(500);

  // JAW OPEN
  chimp_hw_move_jaw(DIR_OPEN);
  delay(500);

  // JAW NEUTRAL
  chimp_hw_move_jaw(DIR_NEUTRAL);
  delay(500);
}

void chimp_demo_eyebrows(void)
{

  // EYEBROWS UP
  chimp_hw_move_eyebrows(VDIR_UP);
  delay(250);
  chimp_hw_move_eyebrows(VDIR_NEUTRAL);
  delay(1000);

  // EYEBROWS DOWN
  chimp_hw_move_eyebrows(VDIR_DOWN);
  delay(250);
  chimp_hw_move_eyebrows(VDIR_NEUTRAL);
  delay(1000);
}
