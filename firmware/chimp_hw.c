#include <Arduino.h>

#include "chimp_hw.h"
#include "chimp_pin.h"

void chimp_hw_setup(void)
{
  pinMode(CHIMP_PIN_EYE_U, OUTPUT);
  pinMode(CHIMP_PIN_EYE_D, OUTPUT);

  pinMode(CHIMP_PIN_EYE_L, OUTPUT);
  pinMode(CHIMP_PIN_EYE_R, OUTPUT);

  pinMode(CHIMP_PIN_EYELID_O, OUTPUT);
  pinMode(CHIMP_PIN_EYELID_C, OUTPUT);

  pinMode(CHIMP_PIN_JAW_O, OUTPUT);
  pinMode(CHIMP_PIN_JAW_C, OUTPUT);

  pinMode(CHIMP_PIN_EYEBROW_U, OUTPUT);
  pinMode(CHIMP_PIN_EYEBROW_D, OUTPUT);

  pinMode(CHIMP_PIN_HEAD_L, OUTPUT);
  pinMode(CHIMP_PIN_HEAD_R, OUTPUT);

  pinMode(CHIMP_PIN_UNKNOWN_A, OUTPUT);
  pinMode(CHIMP_PIN_UNKNOWN_B, OUTPUT);

  pinMode(CHIMP_PIN_UNKNOWN_C, OUTPUT);
  pinMode(CHIMP_PIN_UNKNOWN_D, OUTPUT);

  delay(500);

  chimp_hw_reset_all();
}

void chimp_hw_reset_all(void)
{
  // make all motors return to neutral
  chimp_hw_move_eyes_vertical(VDIR_NEUTRAL);
  chimp_hw_move_eyes_horizontal(HDIR_NEUTRAL);
  chimp_hw_move_eyelids(DIR_NEUTRAL);
  chimp_hw_move_eyebrows(VDIR_NEUTRAL);
  chimp_hw_move_jaw(DIR_NEUTRAL);
  chimp_hw_move_upper_lip(VDIR_NEUTRAL);
  chimp_hw_move_head_horizontal(HDIR_NEUTRAL);
  chimp_hw_move_head_vertical(VDIR_NEUTRAL);

  // until we figure out what the other hbridges do, set these low
  digitalWrite(CHIMP_PIN_UNKNOWN_A, LOW);
  digitalWrite(CHIMP_PIN_UNKNOWN_B, LOW);
  digitalWrite(CHIMP_PIN_UNKNOWN_C, LOW);
  digitalWrite(CHIMP_PIN_UNKNOWN_D, LOW);
}

void chimp_hw_move_eyes_vertical(vdir_t dir)
{
  switch (dir)
  {
    case VDIR_NEUTRAL:
      digitalWrite(CHIMP_PIN_EYE_U, LOW);
      digitalWrite(CHIMP_PIN_EYE_D, LOW);
      break;
    case VDIR_UP:
      digitalWrite(CHIMP_PIN_EYE_D, LOW);
      digitalWrite(CHIMP_PIN_EYE_U, HIGH);
      break;
    case VDIR_DOWN:
      digitalWrite(CHIMP_PIN_EYE_U, LOW);
      digitalWrite(CHIMP_PIN_EYE_D, HIGH);
      break;
  }
}

void chimp_hw_move_eyes_horizontal(hdir_t dir)
{
  switch (dir)
  {
    case HDIR_NEUTRAL:
      digitalWrite(CHIMP_PIN_EYE_L, LOW);
      digitalWrite(CHIMP_PIN_EYE_R, LOW);
      break;
    case HDIR_LEFT:
      digitalWrite(CHIMP_PIN_EYE_R, LOW);
      digitalWrite(CHIMP_PIN_EYE_L, HIGH);
      break;
    case HDIR_RIGHT:
      digitalWrite(CHIMP_PIN_EYE_L, LOW);
      digitalWrite(CHIMP_PIN_EYE_R, HIGH);
      break;
  }
}

void chimp_hw_move_eyelids(dir_t dir)
{
  switch (dir)
  {
    case DIR_NEUTRAL:
      digitalWrite(CHIMP_PIN_EYELID_O, LOW);
      digitalWrite(CHIMP_PIN_EYELID_C, LOW);
      break;
    case DIR_OPEN:
      digitalWrite(CHIMP_PIN_EYELID_C, LOW);
      digitalWrite(CHIMP_PIN_EYELID_O, HIGH);
      break;
    case DIR_CLOSE:
      digitalWrite(CHIMP_PIN_EYELID_O, LOW);
      digitalWrite(CHIMP_PIN_EYELID_C, HIGH);
      break;
  }
}

void chimp_hw_move_jaw(dir_t dir)
{
  switch (dir)
  {
    case DIR_NEUTRAL:
      digitalWrite(CHIMP_PIN_JAW_O, LOW);
      digitalWrite(CHIMP_PIN_JAW_C, LOW);
      break;
    case DIR_OPEN:
      digitalWrite(CHIMP_PIN_JAW_C, LOW);
      digitalWrite(CHIMP_PIN_JAW_O, HIGH);
      break;
    case DIR_CLOSE:
      digitalWrite(CHIMP_PIN_JAW_O, LOW);
      digitalWrite(CHIMP_PIN_JAW_C, HIGH);
      break;
  }
}

void chimp_hw_move_eyebrows(vdir_t dir)
{
  switch (dir)
  {
    case VDIR_NEUTRAL:
      digitalWrite(CHIMP_PIN_EYEBROW_U, LOW);
      digitalWrite(CHIMP_PIN_EYEBROW_D, LOW);
      break;
    case VDIR_UP:
      digitalWrite(CHIMP_PIN_EYEBROW_D, LOW);
      digitalWrite(CHIMP_PIN_EYEBROW_U, HIGH);
      break;
    case VDIR_DOWN:
      digitalWrite(CHIMP_PIN_EYEBROW_U, LOW);
      digitalWrite(CHIMP_PIN_EYEBROW_D, HIGH);
      break;
  }
}

void chimp_hw_move_head_horizontal(hdir_t dir)
{
  switch (dir)
  {
    case HDIR_NEUTRAL:
      digitalWrite(CHIMP_PIN_HEAD_L, LOW);
      digitalWrite(CHIMP_PIN_HEAD_R, LOW);
      break;
    case HDIR_LEFT:
      digitalWrite(CHIMP_PIN_HEAD_R, LOW);
      digitalWrite(CHIMP_PIN_HEAD_L, HIGH);
      break;
    case HDIR_RIGHT:
      digitalWrite(CHIMP_PIN_HEAD_L, LOW);
      digitalWrite(CHIMP_PIN_HEAD_R, HIGH);
      break;
  }
}

void chimp_hw_move_head_vertical(vdir_t dir)
{
  //  switch (dir)
  //  {
  //    case VDIR_NEUTRAL:
  //      digitalWrite(CHIMP_PIN_HEAD_U, LOW);
  //      digitalWrite(CHIMP_PIN_HEAD_D, LOW);
  //      break;
  //    case VDIR_UP:
  //      digitalWrite(CHIMP_PIN_HEAD_D, LOW);
  //      digitalWrite(CHIMP_PIN_HEAD_U, HIGH);
  //      break;
  //    case VDIR_DOWN:
  //      digitalWrite(CHIMP_PIN_HEAD_U, LOW);
  //      digitalWrite(CHIMP_PIN_HEAD_D, HIGH);
  //      break;
  //  }
}

void chimp_hw_move_upper_lip(vdir_t dir)
{
  //  switch (dir)
  //  {
  //    case VDIR_NEUTRAL:
  //      digitalWrite(CHIMP_PIN_LIP_U, LOW);
  //      digitalWrite(CHIMP_PIN_LIP_D, LOW);
  //      break;
  //    case VDIR_UP:
  //      digitalWrite(CHIMP_PIN_LIP_D, LOW);
  //      digitalWrite(CHIMP_PIN_LIP_U, HIGH);
  //      break;
  //    case VDIR_DOWN:
  //      digitalWrite(CHIMP_PIN_LIP_U, LOW);
  //      digitalWrite(CHIMP_PIN_LIP_D, HIGH);
  //      break;
  //  }
}
