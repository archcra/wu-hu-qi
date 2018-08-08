


# 20180726

TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 7, 'drawn': 13, 'current_player': 0}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 7, 'drawn': 13, 'nsp': 0}



ITERATION NUMBER 201
BEST PLAYER VERSION 428


TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 1, 'drawn': 19, 'current_player': 0}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 1, 'drawn': 19, 'nsp': 0}



ITERATION NUMBER 206
BEST PLAYER VERSION 429



# 20180723



TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 0, 'drawn': 20, 'current_player': 0}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 0, 'drawn': 20, 'nsp': 0}



ITERATION NUMBER 647
BEST PLAYER VERSION 377


ubuntu@gd-1:~/docker/wu-hu-qi/run/logs$ grep EPISODE logger_main.log | wc -l
41160
在自对弈大于4万多盘时，kernel dead.


##
TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 1, 'drawn': 19, 'current_player': 0}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 1, 'drawn': 19, 'nsp': 0}



ITERATION NUMBER 650
BEST PLAYER VERSION 377

问题：是不稳定，还是先手必胜？




# 20180721




TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 1, 'drawn': 17, 'current_player': 2}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 1, 'drawn': 17, 'nsp': 2}



ITERATION NUMBER 416
BEST PLAYER VERSION 304

看来，还是没到终点。




=====


TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 3, 'drawn': 9, 'current_player': 8}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 11, 'drawn': 9, 'nsp': 0}



ITERATION NUMBER 457
BEST PLAYER VERSION 324

好像先手必胜？


# 20180720




TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 0, 'drawn': 20, 'current_player': 0}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 0, 'drawn': 20, 'nsp': 0}

ITERATION NUMBER 302
BEST PLAYER VERSION 262


这个在262版本时，全是和棋。应该是到终点了。


TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 0, 'drawn': 9, 'current_player': 11}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 11, 'drawn': 9, 'nsp': 0}



ITERATION NUMBER 304
BEST PLAYER VERSION 263

出现转折：　在263版本时，先手胜了11盘。


ITERATION NUMBER 304
BEST PLAYER VERSION 263
SELF PLAYING 60 EPISODES...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60

RETRAINING...
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 0.8247 - value_head_loss: 0.1894 - policy_head_loss: 1.3867
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 0.8040 - value_head_loss: 0.2149 - policy_head_loss: 1.3199
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 0.8259 - value_head_loss: 0.1938 - policy_head_loss: 1.3849
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 0.8541 - value_head_loss: 0.1833 - policy_head_loss: 1.4517





# 20180718



RETRAINING...
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 0.9470 - value_head_loss: 0.2832 - policy_head_loss: 1.4945
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 0.9582 - value_head_loss: 0.2494 - policy_head_loss: 1.5508
Epoch 1/1
512/512 [==============================] - 5s 9ms/step - loss: 0.9538 - value_head_loss: 0.2639 - policy_head_loss: 1.5275
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 0.9773 - value_head_loss: 0.2977 - policy_head_loss: 1.5407

TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 2, 'drawn': 18, 'current_player': 0}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 0, 'drawn': 18, 'nsp': 2}



ITERATION NUMBER 71
BEST PLAYER VERSION 165


...

TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 4, 'drawn': 14, 'current_player': 2}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 6, 'drawn': 14, 'nsp': 0}

好像只有先手可能赢；而且，和棋好像多。




# 第三次记录
@qing
https://github.com/archcra/wu-hu-qi.git



启动：
cat tensor-flow-20180310 | docker load

docker run -ti --name alpha-xerox -e GRANT_SUDO=yes --user root -p 8899:8888 -v "$PWD":/home/jovyan/work jupyter/tensorflow-notebook

http://www.maizedna.cn:8899/


INITIAL_RUN_NUMBER = 4
INITIAL_MODEL_VERSION = 134
INITIAL_MEMORY_VERSION =  60


in container shell:
```
apt-get update
apt-get install python-pydot python-pydot-ng graphviz
pip install --upgrade pip
pip install pydot graphviz

restart the container:

docker stop alpha-xerox
docker start alpha-xerox
```






TOURNAMENT...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
SCORES
{'best_player': 5, 'drawn': 7, 'current_player': 8}

STARTING PLAYER / NON-STARTING PLAYER SCORES
{'sp': 4, 'drawn': 7, 'nsp': 9}

ITERATION NUMBER 4
BEST PLAYER VERSION 137
SELF PLAYING 60 EPISODES...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60

RETRAINING...
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 1.0196 - value_head_loss: 0.3112 - policy_head_loss: 1.6005
Epoch 1/1
512/512 [==============================] - 5s 9ms/step - loss: 1.0638 - value_head_loss: 0.2978 - policy_head_loss: 1.7024
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 1.0620 - value_head_loss: 0.3420 - policy_head_loss: 1.6546
Epoch 1/1
512/512 [==============================] - 5s 9ms/step - loss: 1.0015 - value_head_loss: 0.3215 - policy_head_loss: 1.5540
Epoch 1/1
512/512 [==============================] - 5s 10ms/step - loss: 1.0291 - value_head_loss: 0.2751 - policy_head_loss: 1.6557
Epoch 1/1


# 以往　

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
