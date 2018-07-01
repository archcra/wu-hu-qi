import numpy as np
import logging

class Game:

    def __init__(self):        
        self.currentPlayer = 1
        self.gameState = GameState(np.zeros(5*5,  dtype=np.int), 1)
        self.actionSpace = np.zeros(5*5,  dtype=np.int)
        self.pieces = {'1':'X', '0': '-', '-1':'O'}
        self.grid_shape = (5,5)
        self.input_shape = (2,5,5)
        self.name = 'wuhuqi'
        self.state_size = len(self.gameState.binary)
        self.action_size = len(self.actionSpace)

    def reset(self):
        self.gameState = GameState(np.zeros(5*5,  dtype=np.int), 1)
        self.currentPlayer = 1
        return self.gameState

    def step(self, action):
        next_state, value, done = self.gameState.takeAction(action)
        self.gameState = next_state
        self.currentPlayer = -self.currentPlayer
        info = None
        return ((next_state, value, done, info))

    def identities(self, state, actionValues):
        identities = [(state,actionValues)]

        return identities


class GameState():
    FIVE_POS=[[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14], [15,16,17,18,19],[20,21,22,23,24],
              [0,5,10,15,20], [1,6,11,16,21], [2,7,12,17,22], [3,8,13,18,23], [4,9,14,19,24],
              [0,6,12,18,24], [4,8,12,16,20]]
    FOUR_POS= [[5,11,17,23], [1,7,13,19], [3,7,11,15], [9,13,17,21]]
    THREE_POS=[[2,6,10], [2,8,14], [10,16,22],[14,18,22]]
    MINI_SQUARE=[[0,1,5,6], [1,2,6,7], [2,3,7,8], [3,4,8,9],[5,6,10,11], [6,7,11,12], [7,8,12,13],[8,9,13,14],
                 [10,11,15,16], [11,12,16,17], [12,13,17,18], [13,14,18,19], [14,15,19,20],[15,16,20,21], [17,18,22,23], [18,19,23,24]]
    
    SCORE_CATEGORY = {1: {'POS': MINI_SQUARE, 'SIZE': 1, 'SCORE': 1}, 
                      3: {'POS': THREE_POS, 'SIZE': 3, 'SCORE': 3} ,
                      4: {'POS': FOUR_POS, 'SIZE': 4, 'SCORE': 4} ,
                      5: {'POS': FIVE_POS, 'SIZE': 5, 'SCORE': 5} 
                     }
    
    def __init__(self, board, playerTurn):
        self.board = board
        self.pieces = {'1':'X', '0': '-', '-1':'O'}

        self.playerTurn = playerTurn
        self.binary = self._binary()
        self.id = self._convertStateToId()
        self.allowedActions = self._allowedActions()
        self.isEndGame = self._checkForEndGame()
        self.value = self._getValue()
        self.score = self._getScore()

    def _allowedActions(self):
        allowed = [i for i, e in enumerate(self.board) if e == 0]
        return allowed

    def _binary(self):

        currentplayer_position = np.zeros(len(self.board), dtype=np.int)
        currentplayer_position[self.board==self.playerTurn] = 1

        other_position = np.zeros(len(self.board), dtype=np.int)
        other_position[self.board==-self.playerTurn] = 1

        position = np.append(currentplayer_position,other_position)

        return (position)

    def _convertStateToId(self):
        player1_position = np.zeros(len(self.board), dtype=np.int)
        player1_position[self.board==1] = 1

        other_position = np.zeros(len(self.board), dtype=np.int)
        other_position[self.board==-1] = 1

        position = np.append(player1_position,other_position)

        id = ''.join(map(str,position))

        return id

    def _checkForEndGame(self):
        if np.count_nonzero(self.board) == 25:
            return 1

        return 0

    def getScore(self, scoreCategory, piece):
        count = 0
        posList = GameState.SCORE_CATEGORY[scoreCategory]['POS']
        size = GameState.SCORE_CATEGORY[scoreCategory]['SIZE']
        score = GameState.SCORE_CATEGORY[scoreCategory]['SCORE']
        
        for pos in posList:
            if ''.join(map(str,self.board[pos])) == piece * size:
                count = count + 1
                
        return count*score
    
    
    def _getValue(self):
        # This is the value of the state for the current player
        # i.e. if the previous player played a winning move, you lose
        # 第一个位置，对方走完局面相对于自己的结果：-1 输，1 赢, 0和；第二个位置：...已方分数；第三个位置:...对方分数
        # find Five
        xFive = self.getScore(5, '1')
        oFive = self.getScore(5, '-1')
        
        # find Four
        xFour = self.getScore(4, '1')
        oFour = self.getScore(4, '-1')
        
        # find Three
        xThree = self.getScore(3, '1')
        oThree = self.getScore(3, '-1')
        
        # find mini-square
        xSquare = self.getScore(1, '1')
        oSquare = self.getScore(1, '-1')
        
        # sum up
        xScore = xFive + xFour + xThree + xSquare
        oScore = oFive + oFour + oThree + oSquare
        
        # 这个后手还是x，即到这步时，必须是 self.playerTurn  == 1
        # assert self.playerTurn  == 1
        if xScore> oScore:
            return (1, xScore, oScore)
        elif xScore == oScore: 
            return (0, xScore, oScore)
        else:
            return (-1, xScore, oScore)
            

    def _getScore(self):
        tmp = self.value
        return (tmp[1], tmp[2])


    def takeAction(self, action):
        newBoard = np.array(self.board)
        newBoard[action]=self.playerTurn
        
        newState = GameState(newBoard, -self.playerTurn)

        value = 0
        done = 0

        if newState.isEndGame:
            value = newState.value[0]
            done = 1

        return (newState, value, done) 




    def render(self, logger):
        for r in range(5):
            logger.info([self.pieces[str(x)] for x in self.board[5*r : (5*r + 5)]])
        logger.info('--------------')