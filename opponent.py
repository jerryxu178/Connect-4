import numpy as np
import random

class opponent(object):

    def __init__(self, game, heuristic=None):
        """

        :param cellstate: an instance of
        :param heuristic: a lambda function on cellstate and player (0 or 1) that returns some given heuristic for theat player
        """
        self._game = game
        self._heuristic = self.defaultheuristic


    def defaultheuristic(self, player, cellstate):

        # TODO build this out
        mycounts = self._game._getConsecutiveCounts(player, cellstate)
        theircounts = self._game._getConsecutiveCounts(3 - player, cellstate)
        #print(counts)
        counts = list(np.array(mycounts) - np.array(theircounts))
        if theircounts[4] > 0:
            return -float('inf')
        if mycounts[4] > 0:
            return float('inf')
        else:
            return counts[3] + counts[2]

    def getMove(self, cellstate, player):
        '''
        Does minimax up until $depth$, assuming you are player "player".

        :param depth:
        :param cellstate:
        :param player:
        :return: the next move!
        '''

        print("Computing minimax for player" + str(player))

        possibleMovedStates = [self._game._testMove(c, np.copy(cellstate), player) for c in range(self._game._columnCounts)]
        outcomes = []
        moves = []

        for (moveIndex, (won, state, invalid)) in enumerate(possibleMovedStates):
            if not invalid:
                outcomes.append(self.minmax(state, "min", 3 - player, 4, player, -float('inf'), float('inf')))
                moves.append(moveIndex)

        print(outcomes)
        bestMove = max(outcomes)
        indices = [i for i, x in enumerate(outcomes) if x == bestMove]
        if len(indices) > 1:
            index = random.choice(indices)
        else:
            index = indices[0]
        return index


    def minmax(self, cellstate, type, player, depth, origplayer, alpha=None, beta=None):
        """
        type is "min" or "max"
        :param cellstate:
        :param type:
        :return:
        """

        if depth == 0:
            return self.defaultheuristic(origplayer, cellstate)

        outcomes = []

        for c in range(self._game._columnCounts):

            (won, state, invalid) = self._game._testMove(c, np.copy(cellstate), player)

            if not invalid:
                if alpha and beta:
                    result = self.minmax(state, ("max" if type == "min" else "min"), 3 - player, depth - 1, origplayer, alpha, beta)
                    if type == "max":
                        if result >= beta:
                            return result
                        alpha = max(alpha, result)
                    elif type == "min":
                        if result <= alpha:
                            return result
                        beta = min(beta, result)
                else:
                    result = self.minmax(state, ("max" if type == "min" else "min"), 3 - player, depth - 1, origplayer)
                outcomes.append(result)

        if type == "max":
            return max(outcomes)
        elif type == "min":
            return min(outcomes)