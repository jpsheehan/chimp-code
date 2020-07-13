#ifndef CHIMP_CTL_H_
#define CHIMP_CTL_H_

#define CHIMP_CTL_BAUDRATE  115200

#define CHIMP_CTL_BUFFER_SIZE 4

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

void chimp_ctl_setup(void);

void chimp_ctl_process(void);

#endif // CHIMP_CTL_H_