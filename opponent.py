import numpy as np

class opponent(object):

    def __init__(self, cellsobject, heuristic=None):
        """

        :param cellstate: an instance of
        :param heuristic: a lambda function on cellstate and player (0 or 1) that returns some given heuristic for theat player
        """
        self._game = cellsobject
        self._cells = cellsobject._cells
        self._heuristic = self.defaultheuristic


    def defaultheuristic(self, cellstate, player):

        # TODO
        return 0.999

    def getMove(self, cellstate, player):
        '''
        Does minimax up until $depth$, assuming you are player x.

        :param depth:
        :param cellstate:
        :param player:
        :return: the next move!
        '''

        possibleMovedStates = [self._game._makeMove(c, cellstate, player) for c in range(self._game.columns)]
        outcomes = []
        for (won, state) in possibleMovedStates:
            if not won and not state:
                # If the move is invalid, what do we do?? lets make it infinitely bad
                outcomes.append(-float('inf'))
            elif won:
                #in this case we want to guarantee it is picked, since we've def. won the game :)
                outcomes.append(float('inf'))
            else:
                # Send this off to minimax if it's neither
                outcomes.append(self.minmax(state, "min", player, 3))

        return np.argmax(outcomes)


    def minmax(self, cellstate, type, player, depth):
        """
        type is "min" or "max"
        :param cellstate:
        :param type:
        :return:
        """

        if depth == 0:
            # We've reached max depht
            return self.defaultheuristic(cellstate, player)

        possibleMovedStates = [self._game._makeMove(c, cellstate, player) for c in range(self._game.columns)]
        outcomes = []

        for (won, state) in possibleMovedStates:
            if not won and not state:
                # If the move is invalid, what do we do?? lets make it infinitely bad
                outcomes.append(-float('inf'))
            elif won:
                # in this case we want to guarantee it is picked, since we've def. won the game :)
                outcomes.append(float('inf'))
            else:
                # Send this off to minimax if it's neither
                outcomes.append(self.minmax(state, ("max" if type == "min" else "min")))

        if type == "max":
            return max(outcomes)
        elif type == "min":
            return min(outcomes)






