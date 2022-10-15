class Grid(object):
    """
    Create a Grid object for to play Tic-Toc-Toe.
    """
    coord ={
        'A':(0,0), 'B':(0,1), 'C':(0,2),
        'D':(1,0), 'E':(1,1), 'F':(1,2),
        'G':(2,0), 'H':(2,1), 'I':(2,2),
    } 

    def __init__(self):
        self._squares = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
            ]
    
    def markSquare(self, position, symbol):
        """
        Paramenters:
            position --> a letter (A-I) representing the position
            
            ╔═════════════╗
            ║  A │ B │ C  ║
            ║────┼───┼────║
            ║  D │ E │ F  ║
            ║────┼───┼────║
            ║  G │ H │ I  ║
            ╚═════════════╝
        
             symbol --> a string (X or O)

        ---------------------------------

        Set the symbol in the indicated position.
        """
        x, y = Grid.coord(position)
        self._squares[x][y] = symbol
    
    def getSquares(self):
        """
        return the current matrix.
        """
        return self._squares

    def printGrid(self):
        """
        Print the grid.
        """

        print(" JOGO DA VELHA: \n")

        print("╔═════════════╗")
        print("║  %s │ %s │ %s  ║" % tuple(self._squares[0]))
        print("║────┼───┼────║")
        print("║  %s │ %s │ %s  ║" % tuple(self._squares[1]))
        print("║────┼───┼────║")
        print("║  %s │ %s │ %s  ║" % tuple(self._squares[2]))
        print("╚═════════════╝")
        print()