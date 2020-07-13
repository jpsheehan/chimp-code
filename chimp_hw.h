#ifdef __cplusplus
extern "C" {
#endif

#ifndef CHIMP_HW_H_
#define CHIMP_HW_H_

typedef enum {
  VDIR_NEUTRAL,
  VDIR_UP,
  VDIR_DOWN
} vdir_t;

typedef enum {
  HDIR_NEUTRAL,
  HDIR_LEFT,
  HDIR_RIGHT
} hdir_t;

typedef enum {
  DIR_NEUTRAL,
  DIR_OPEN,
  DIR_CLOSE
} dir_t;

void chimp_hw_setup(void);

void chimp_hw_move_eyes_vertical(vdir_t dir);

void chimp_hw_move_eyes_horizontal(hdir_t dir);

void chimp_hw_move_eyelids(dir_t dir);

void chimp_hw_move_jaw(dir_t dir);

void chimp_hw_move_eyebrows(vdir_t dir);

void chimp_hw_move_head_horizontal(hdir_t dir);

void chimp_hw_move_head_vertical(vdir_t dir);

void chimp_hw_move_upper_lip(vdir_t dir);

#endif

#ifdef __cplusplus
} // extern "C"
#endif
