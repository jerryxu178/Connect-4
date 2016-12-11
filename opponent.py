import numpy as np

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
            print("possible WIN for them :(")
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
        for (won, state, invalid) in possibleMovedStates:
            #print(state)
            if invalid:
                # If the move is invalid, what do we do?? lets make it infinitely bad
                outcomes.append(-float('inf'))
            # elif won:
            #     #in this case we want to guarantee it is picked, since we've def. won the game :)
            #     outcomes.append(float('inf'))
            else:
                # Send this off to minimax if it's neither
                outcomes.append(self.minmax(state, "min", 3 - player, 3, player))

        print(outcomes)
        return np.argmax(outcomes)


    def minmax(self, cellstate, type, player, depth, origplayer):
        """
        type is "min" or "max"
        :param cellstate:
        :param type:
        :return:
        """

        if depth == 0:
            # We've reached max depht
            return self.defaultheuristic(origplayer, cellstate)

        possibleMovedStates = [self._game._testMove(c, np.copy(cellstate), player) for c in range(self._game._columnCounts)]
        outcomes = []

        for (won, state, invalid) in possibleMovedStates:

            if invalid:
                # If the move is invalid, what do we do?? lets make it infinitely bad
                outcomes.append(-float('inf'))
            # elif won:
            #     print("oops")
            #     # in this case we want to guarantee it is picked, since we've def. won the game :)
            #     outcomes.append(float('inf'))
            else:
                # Send this off to minimax if it's neither
                outcomes.append(self.minmax(state, ("max" if type == "min" else "min"), 3 - player, depth - 1, origplayer))

       # print("taking " + type + " of")
        #print(outcomes)
        if type == "max":
            return max(outcomes)
        elif type == "min":
            #print(outcomes)
            return min(outcomes)