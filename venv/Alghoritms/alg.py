print("[INIT] algorytmy")

# input:
a_ball_x = 0
a_ball_y = 0
a_ball_w = 0

val_speed = 0
val_diff = 0

base_speed = 0

gain_speed = 5
gain_diff = 5

motor_temp_l = 90
motor_temp_r = 90

# output:
o_servo_V = 90
o_servo_H = 90
o_motor_L = 90
o_motor_R = 90

# screensize
screen_max_x = 640
screen_max_y = 480

#fuzzy_dist = dict()
#fuzzy_dist

pid_p = 1
pid_i = 1
pid_d = 1

def alg():
   #  print("ALG")
    global a_ball_x
    global screen_max_x
    a_ball_x =  (a_ball_x/(screen_max_x/2))-1
    global a_ball_y
    global screen_max_y
    a_ball_y =  ((a_ball_y/(screen_max_y/2))-1)*(-1)
     
     
    if a_ball_w > 45:
        #cofaj
        val_speed = -0.5
    elif a_ball_w >37:
        #stoj
        val_speed = 0
    elif a_ball_w >25:
        #jedz wolno
        val_speed = 0.5
    elif a_ball_w >10:
        #jedz szykbo
        val_speed = 1
    else:
        #stoj, nic nie widac
        val_speed = 0
        
     
    if a_ball_x > 0.5:
        #ostro lewo
        val_diff = 1
    elif a_ball_x > 0.2:
        #słabo w lewo
        val_diff = 0.5
    elif a_ball_x > -0.2:
        #stoj
        val_diff = 0
    elif a_ball_x >-0.5:
      #  jedz szykbo
        val_diff = -0.5
    else:
        #stoj, nic nie widac
        val_diff = -1



    global motor_temp_l
    global motor_temp_r

    motor_temp_r = base_speed + (gain_speed * val_speed) + (gain_diff * val_diff)
    motor_temp_l = base_speed + (gain_speed * val_speed) - (gain_diff * val_diff)
    
    
#    motor_temp_r = 90 
         
     
    print("X=",  round(a_ball_x,3), "Y=",  round(a_ball_y,3) , "W=",  a_ball_w, " speed=", val_speed, " diff=", val_diff, " L=", motor_temp_l, " R=", motor_temp_r)
    
    
    