class HierarchyInterface:

    def compareSuits(self, a, b):
        """
        Compares the suit a to b and returns:
        -1 if a is less than b
         0 if a is equal to b
         1 if a is greater than b
        """
        raise NotImplementedError("compareSuit method not implemented")

    
    def compareValues(self, a, b):
        """
        Compares the value a to b and returns:
        -1 if a is less than b
         0 if a is equal to b
         1 if a is greater than b
        """
        raise NotImplementedError("compareValue method not implemented")
    
    # Need to pin a as a single card or a combination of card
    # Suit Preference can be a dict/array of 4
    def comparePlays(self, a, b, suit_preference):
        """
        Compares the play a to b and returns:
        -1 if a is less than b
         0 if a is equal to b
         1 if a is greater than b
        """
        raise NotImplementedError("comparePlay method not implemented")

    # Abstract this to result one single play or mutiple play if multiple plays can win
    def getWinningPlay(self, plays):
        """
        Returns the winning play from a list of plays.
        """
        raise NotImplementedError("getWinningPlay method not implemented")
