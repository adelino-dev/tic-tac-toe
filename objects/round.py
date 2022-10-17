import objects.moderator as m

class Round(object):
    """
    Create a Round object for to play a Tic-Toc-Toe round.
    """

    def start(self):
        self._moderator = m.Moderator()

        while self._moderator.analyze() == "no winner":
            self._moderator.askPosition()
        
        self._moderator.printResult()