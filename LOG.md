


用时：
2018-07-01 11:23:53,094 INFO EPISODE 1 OF 30
2018-07-01 15:04:33,325 INFO EPISODE 9 OF 30

3.5小时

训练盘数：
huoyongxue@HSHY-151-SERVER:~/todo/wu-hu-qi/run/logs$ grep EPISODE logger_main.log | wc -l
703


比赛盘数：
huoyongxue@HSHY-151-SERVER:~/todo/wu-hu-qi/run/logs$ grep EPISODE logger_tourney.log | wc -l
400


战线：
SCORES
{'best_player': 11, 'drawn': 2, 'current_player': 7}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 10, 'drawn': 2, 'nsp': 8}



ITERATION NUMBER 24
BEST PLAYER VERSION 12


# 第二次记录
```
huoyongxue@HSHY-151-SERVER:~/todo/wu-hu-qi/run/logs$ ls ../models/ -al
total 92756
drwxrwxr-x 2 huoyongxue huoyongxue    4096 Jul  2 07:48 .
drwxrwxr-x 5 huoyongxue huoyongxue    4096 Jul  1 15:35 ..
-rw-r--r-- 1 huoyongxue users       448767 Jul  1 19:23 model.png
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 19:50 version0001.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 20:11 version0002.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 20:21 version0003.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 21:11 version0004.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 21:21 version0005.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 21:32 version0006.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 21:42 version0007.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 22:02 version0008.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 22:12 version0009.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 22:22 version0010.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 22:42 version0011.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 22:52 version0012.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  1 23:43 version0013.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 00:03 version0014.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 01:24 version0015.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 01:54 version0016.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 02:24 version0017.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 02:55 version0018.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 03:35 version0019.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 04:16 version0020.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 04:26 version0021.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 04:46 version0022.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 05:16 version0023.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 05:36 version0024.h5
-rw-r--r-- 1 huoyongxue users      3771224 Jul  2 07:48 version0025.h5

huoyongxue@HSHY-151-SERVER:~/todo/wu-hu-qi/run/logs$ grep EPISODE logger_tourney.log | wc -l
1450
huoyongxue@HSHY-151-SERVER:~/todo/wu-hu-qi/run/logs$ grep EPISODE logger_main.log | wc -l
2280


1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 9, 'drawn': 3, 'current_player': 8}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 12, 'drawn': 3, 'nsp': 5}



ITERATION NUMBER 77
BEST PLAYER VERSION 25

```
后手还能赢5盘

新的配置调整如下：
```
#### SELF PLAY
EPISODES = 30
MCTS_SIMS = 50
MEMORY_SIZE = 10000
TURNS_UNTIL_TAU0 = 10 # turn on which it starts playing deterministically
CPUCT = 2
EPSILON = 0.2
ALPHA = 0.8


#### RETRAINING
BATCH_SIZE = 512
EPOCHS = 1
REG_CONST = 0.0001
LEARNING_RATE = 0.01
```
