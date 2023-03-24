class CallbreakHierarchy(GameInterface):

    cardValueOrder = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    trumpSuit = "hukum"

    def compareSuits(self, a, b, suit_preference):
        if a == trumpSuit and b == trumpSuit:
            return 0
        elif a == trumpSuit:
            return 1
        elif b == trumpSuit:
            return -1
        elif a == suit_preference and b == suit_preference:
            return 0
        elif a == suit_preference:
            return 1
        elif b == suit_preference:
            return -1
        else:
            return 0

    def compareValues(self, a, b):
        ai =cardValueOrder.indexOf(a)
        bi = cardValueOrder.indexOf(b)
        if ai < bi:
            return 1
        elif ai > bi:
            return -1
        else:
            return 0 

    # suit_preference capture the suit that started the play
    def comparePlays(self, a, b, suit_preference):
        x = compareSuit(a, b, suit_preference)
        return x if x !=0 else compareValues(a, b)

    def getWinningPlay(self, plays):
        for play1 in plays:
            beats_all = True
            for play2 in plays:
                if play1 != play2 and self.comparePlay(play1, play2) == -1:
                    beats_all = False
                    break
            if beats_all:
                return play1
        return None