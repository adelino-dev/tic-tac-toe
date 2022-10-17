class Player(object):
    """
    Create a player object for the  to play Tic-Toc-Toe.
    """
    def __init__(self, symbol):
        """
        symbol --> a string (X or O)
        """
        self._symbol = symbol
    
    def markSquare(grid, position):
        """
        Paramenters:
            grid --> a Grid object.
            position --> a letter (A-I) representing the position
            
            ╔═════════════╗
            ║  A │ B │ C  ║
            ║────┼───┼────║
            ║  D │ E │ F  ║
            ║────┼───┼────║
            ║  G │ H │ I  ║
            ╚═════════════╝

        ---------------------------------

        Set the symbol in the indicated position.

        """
        grid.markSquare(position, self._symbol)
    
    def getSymbol(self):
        "Return the symbol (X or O)."
        return self._symbol