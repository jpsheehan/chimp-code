#include "chimp_hw.h"
#include "chimp_demo.h"

/*
   Received Packet:

   [0] - COMMAND ID
   [1] - DIRECTION or 0x00
*/

/**
   Transmitted Packet:

   [0] - COMMAND ID
   [1] - STATUS
   [2] - DIRECTION or 0x00
*/

#define CHIMP_CTL_BAUDRATE  115200

#define CHIMP_CTL_BUFFER_SIZE 10

#define CHIMP_CTL_RX_PACKET_SIZE 2
#define CHIMP_CTL_TX_PACKET_SIZE 3

#define CHIMP_CTL_DIR_NONE    0x00
#define CHIMP_CTL_DIR_NEUTRAL 0x00
#define CHIMP_CTL_DIR_LEFT    0x01
#define CHIMP_CTL_DIR_RIGHT   0x02
#define CHIMP_CTL_DIR_UP      0x01
#define CHIMP_CTL_DIR_DOWN    0x02
#define CHIMP_CTL_DIR_OPEN    0x01
#define CHIMP_CTL_DIR_CLOSE   0x02

#define CHIMP_CTL_CMD_PING            0x00

#define CHIMP_CTL_CMD_MOVE_EYES_H     0x10
#define CHIMP_CTL_CMD_MOVE_EYES_V     0x11
#define CHIMP_CTL_CMD_MOVE_EYELIDS    0x12
#define CHIMP_CTL_CMD_MOVE_EYEBROWS   0x13
#define CHIMP_CTL_CMD_MOVE_JAW        0x14
#define CHIMP_CTL_CMD_MOVE_UPPER_LIP  0x15
#define CHIMP_CTL_CMD_MOVE_HEAD_H     0x16
#define CHIMP_CTL_CMD_MOVE_HEAD_V     0x17

#define CHIMP_CTL_CMD_ALL_NEUTRAL     0x20

typedef enum {
  CHIMP_CTL_STATUS_OK = 0x00,
  CHIMP_CTL_STATUS_INVALID_COMMAND = 0x01,
  CHIMP_CTL_STATUS_INVALID_DIRECTION = 0x02,
} chimp_ctl_err_t;

void chimp_ctl_setup()
{
  Serial.begin(CHIMP_CTL_BAUDRATE);
}

void chimp_ctl_build_packet(byte *buffer, chimp_ctl_err_t status, int direction)
{
  // buffer[0] stays the same
  buffer[1] = (byte)status;
  buffer[2] = (byte)direction;
}

void chimp_ctl_process_packet_move_eyes_horizontal(byte *buffer)
{
  hdir_t dir;

  switch (buffer[1])
  {
    case CHIMP_CTL_DIR_NEUTRAL:
      dir = HDIR_NEUTRAL;
      break;
    case CHIMP_CTL_DIR_LEFT:
      dir = HDIR_LEFT;
      break;
    case CHIMP_CTL_DIR_RIGHT:
      dir = HDIR_RIGHT;
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_DIRECTION, buffer[1]);
      return;
  }

  chimp_hw_move_eyes_horizontal(dir);
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, dir);
}

void chimp_ctl_process_packet_move_eyes_vertical(byte *buffer)
{
  vdir_t dir;

  switch (buffer[1])
  {
    case CHIMP_CTL_DIR_NEUTRAL:
      dir = VDIR_NEUTRAL;
      break;
    case CHIMP_CTL_DIR_UP:
      dir = VDIR_UP;
      break;
    case CHIMP_CTL_DIR_DOWN:
      dir = VDIR_DOWN;
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_DIRECTION, buffer[1]);
      return;
  }

  chimp_hw_move_eyes_vertical(dir);
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, dir);
}

void chimp_ctl_process_packet_move_eyelids(byte *buffer)
{
  dir_t dir;

  switch (buffer[1])
  {
    case CHIMP_CTL_DIR_NEUTRAL:
      dir = DIR_NEUTRAL;
      break;
    case CHIMP_CTL_DIR_OPEN:
      dir = DIR_OPEN;
      break;
    case CHIMP_CTL_DIR_CLOSE:
      dir = DIR_CLOSE;
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_DIRECTION, buffer[1]);
      return;
  }
  
  chimp_hw_move_eyelids(dir);
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, dir);
}

void chimp_ctl_process_packet_move_eyebrows(byte *buffer)
{
  vdir_t dir;

  switch (buffer[1])
  {
    case CHIMP_CTL_DIR_NEUTRAL:
      dir = VDIR_NEUTRAL;
      break;
    case CHIMP_CTL_DIR_UP:
      dir = VDIR_UP;
      break;
    case CHIMP_CTL_DIR_DOWN:
      dir = VDIR_DOWN;
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_DIRECTION, buffer[1]);
      return;
  }
  
  chimp_hw_move_eyebrows(dir);
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, dir);
}

void chimp_ctl_process_packet_move_jaw(byte *buffer)
{
  dir_t dir;

  switch (buffer[1])
  {
    case CHIMP_CTL_DIR_NEUTRAL:
      dir = DIR_NEUTRAL;
      break;
    case CHIMP_CTL_DIR_OPEN:
      dir = DIR_OPEN;
      break;
    case CHIMP_CTL_DIR_CLOSE:
      dir = DIR_CLOSE;
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_DIRECTION, buffer[1]);
      return;
  }
  
  chimp_hw_move_jaw(dir);
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, dir);
}

void chimp_ctl_process_packet_move_upper_lip(byte *buffer)
{
  vdir_t dir;

  switch (buffer[1])
  {
    case CHIMP_CTL_DIR_NEUTRAL:
      dir = VDIR_NEUTRAL;
      break;
    case CHIMP_CTL_DIR_UP:
      dir = VDIR_UP;
      break;
    case CHIMP_CTL_DIR_DOWN:
      dir = VDIR_DOWN;
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_DIRECTION, buffer[1]);
      return;
  }
  
  chimp_hw_move_upper_lip(dir);
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, dir);
}

void chimp_ctl_process_packet_move_head_horizontal(byte *buffer)
{
  hdir_t dir;

  switch (buffer[1])
  {
    case CHIMP_CTL_DIR_NEUTRAL:
      dir = HDIR_NEUTRAL;
      break;
    case CHIMP_CTL_DIR_LEFT:
      dir = HDIR_LEFT;
      break;
    case CHIMP_CTL_DIR_RIGHT:
      dir = HDIR_RIGHT;
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_DIRECTION, buffer[1]);
      return;
  }
  
  chimp_hw_move_head_horizontal(dir);
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, dir);
}

void chimp_ctl_process_packet_move_head_vertical(byte *buffer)
{
  vdir_t dir;

  switch (buffer[1])
  {
    case CHIMP_CTL_DIR_NEUTRAL:
      dir = VDIR_NEUTRAL;
      break;
    case CHIMP_CTL_DIR_UP:
      dir = VDIR_UP;
      break;
    case CHIMP_CTL_DIR_DOWN:
      dir = VDIR_DOWN;
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_DIRECTION, buffer[1]);
      return;
  }
  
  chimp_hw_move_head_vertical(dir);
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, dir);
}

void chimp_ctl_process_packet_ping(byte *buffer)
{
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, CHIMP_CTL_DIR_NONE);
}

void chimp_ctl_process_packet_all_neutral(byte *buffer)
{
  chimp_hw_reset_all();
  chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_OK, CHIMP_CTL_DIR_NONE);
}

void chimp_ctl_process_packet(byte *buffer)
{
  // TODO: some sort of CRC check?

  switch (buffer[0])
  {
    case CHIMP_CTL_CMD_PING:
      chimp_ctl_process_packet_ping(buffer);
      break;
    case CHIMP_CTL_CMD_MOVE_EYES_H:
      chimp_ctl_process_packet_move_eyes_horizontal(buffer);
      break;
    case CHIMP_CTL_CMD_MOVE_EYES_V:
      chimp_ctl_process_packet_move_eyes_vertical(buffer);
      break;
    case CHIMP_CTL_CMD_MOVE_EYELIDS:
      chimp_ctl_process_packet_move_eyelids(buffer);
      break;
    case CHIMP_CTL_CMD_MOVE_EYEBROWS:
      chimp_ctl_process_packet_move_eyebrows(buffer);
      break;
    case CHIMP_CTL_CMD_MOVE_JAW:
      chimp_ctl_process_packet_move_jaw(buffer);
      break;
    case CHIMP_CTL_CMD_MOVE_UPPER_LIP:
      chimp_ctl_process_packet_move_upper_lip(buffer);
      break;
    case CHIMP_CTL_CMD_MOVE_HEAD_H:
      chimp_ctl_process_packet_move_head_horizontal(buffer);
      break;
    case CHIMP_CTL_CMD_MOVE_HEAD_V:
      chimp_ctl_process_packet_move_head_vertical(buffer);
      break;
    case CHIMP_CTL_CMD_ALL_NEUTRAL:
      chimp_ctl_process_packet_all_neutral(buffer);
      break;
    default:
      chimp_ctl_build_packet(buffer, CHIMP_CTL_STATUS_INVALID_COMMAND, CHIMP_CTL_DIR_NONE);
      break;
  }
}

void chimp_ctl_process(void)
{
  byte buffer[CHIMP_CTL_BUFFER_SIZE] = {0};
  size_t n;

  if (Serial.available())
  {
    n = Serial.readBytes(buffer, CHIMP_CTL_RX_PACKET_SIZE);

    if (n == CHIMP_CTL_RX_PACKET_SIZE)
    {
      // process the packet
      chimp_ctl_process_packet(buffer);

      // send it down the wire
      Serial.write(buffer, CHIMP_CTL_TX_PACKET_SIZE);
    }
  }
}

void setup() {
  // put your setup code here, to run once:

  chimp_ctl_setup();
  chimp_hw_setup();
}

void loop() {
  // put your main code here, to run repeatedly:
  //   chimp_demo_eyes_horizontal();
  //   chimp_demo_eyelids();
  //   chimp_demo_jaw();
  //   chimp_demo_eyebrows();

  chimp_ctl_process();

}
