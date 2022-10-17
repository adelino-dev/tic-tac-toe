class Player(object):
    """
    Create a player object for the  to play Tic-Toc-Toe.
    """
    def __init__(self, symbol):
        """
        symbol --> a string (X or O)
        """
        self._symbol = symbol
    
    def markSquare(self, grid, position):
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
        """
        Return the symbol (X or O).
        """
        coord ={
            'A':(0,0), 'B':(0,1), 'C':(0,2),
            'D':(1,0), 'E':(1,1), 'F':(1,2),
            'G':(2,0), 'H':(2,1), 'I':(2,2),
        }
        return self._symbol