#include <Arduino.h>

#include "chimp_demo.h"
#include "chimp_hw.h"

void chimp_demo_eyes_horizontal(void)
{

  // LOOK LEFT
#if PRINT_DEBUG
  Serial.print("Looking left... ");
#endif
  
  chimp_hw_move_eyes_horizontal(HDIR_LEFT);
  delay(300);
  chimp_hw_move_eyes_horizontal(HDIR_NEUTRAL);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif

  delay(1000);

  // LOOK RIGHT
#if PRINT_DEBUG
  Serial.print("Looking right... ");
#endif

  chimp_hw_move_eyes_horizontal(HDIR_RIGHT);
  delay(300);
  chimp_hw_move_eyes_horizontal(HDIR_NEUTRAL);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif

  delay(1000);
}

void chimp_demo_eyes_vertical(void)
{

  // LOOK UP
  
#if PRINT_DEBUG
  Serial.print("Looking up... ");
#endif

  chimp_hw_move_eyes_vertical(VDIR_UP);
  delay(350);
  chimp_hw_move_eyes_vertical(VDIR_NEUTRAL);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif

  delay(1000);

  // LOOK DOWN
  
#if PRINT_DEBUG
  Serial.print("Looking down... ");
#endif

  chimp_hw_move_eyes_vertical(VDIR_DOWN);
  delay(350);
  chimp_hw_move_eyes_vertical(VDIR_NEUTRAL);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif

  delay(1000);
}

void chimp_demo_eyelids(void)
{

  // EYES CLOSE
#if PRINT_DEBUG
  Serial.print("Eyes closing... ");
#endif

  chimp_hw_move_eyelids(DIR_CLOSE);
  delay(400);
  chimp_hw_move_eyelids(DIR_NEUTRAL);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif
  delay(1000);

  // EYES OPEN
#if PRINT_DEBUG
  Serial.print("Eyes opening... ");
#endif

  chimp_hw_move_eyelids(DIR_OPEN);
  delay(400);
  chimp_hw_move_eyelids(DIR_NEUTRAL);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif

  delay(1000);
}

void chimp_demo_jaw(void)
{

  // JAW CLOSE
#if PRINT_DEBUG
  Serial.print("Jaw closing... ");
#endif

  chimp_hw_move_jaw(DIR_CLOSE);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif

  delay(500);

  // JAW OPEN
#if PRINT_DEBUG
  Serial.print("Jaw opening... ");
#endif

  chimp_hw_move_jaw(DIR_OPEN);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif

  delay(500);

  chimp_hw_move_jaw(DIR_NEUTRAL);
  
}

void chimp_demo_eyebrows(void)
{

  // EYEBROWS UP
#if PRINT_DEBUG
  Serial.print("Eyebrows going up... ");
#endif

  chimp_hw_move_eyebrows(VDIR_UP);
  delay(250);
  chimp_hw_move_eyebrows(VDIR_NEUTRAL);
  delay(1000);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif

  // EYEBROWS DOWN
#if PRINT_DEBUG
  Serial.print("Eyebrows going down... ");
#endif

  chimp_hw_move_eyebrows(VDIR_DOWN);
  delay(250);
  chimp_hw_move_eyebrows(VDIR_NEUTRAL);
  delay(1000);
  
#if PRINT_DEBUG
  Serial.println("Done!");
#endif
}
