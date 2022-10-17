from objects.grid import Grid
from objects.player import Player

class Moderator(object):
    """
    Create a Moderator object for to moderate the Tic Tac Toe game.
    """
    def __init__(self):
        self._grid = Grid()
        self._playerX = Player("x")
        self._playerO = Player("o")

        self._currentPlayer = self._playerX
        self._plays = 0 #Number of plays

    def askPosition(self):
        symbol = self._currentPlayer.getSymbol()
        self._grid.printGrid()
        
        position = input("Jogador %s, escolha uma posição:" % symbol)
        position = self.validatePosition(position)
        
        self._currentPlayer.markSquare(self._grid, position)

        #Change the current Player:
        if self._currentPlayer == self._playerX:
            self._currentPlayer = self._playerO
        
        else:
            self._currentPlayer = self._playerX
    
    def validatePosition(self, position):
        """
        Analyzes if the given position is valid and 
        if it has been typed before. 
        If yes for either case, ask the user
        to enter the position again.
        """
        valid_positions = Grid.coord.keys()
        square = self._grid.getPosition(position)

        test1 = not position in valid_positions
        test2 = square == "x" or square == "o"

        while test1 or test2:
            if test1:
                print("\n  Ops! Você digitou algo inválido.")
                print("Digite apenas uma letra do alfabeto entre A e I.")
                position = input("Digite novamente:")

            else:
                print("\n  Ops! Essa posição já foi escolhida antes."
                position = input("Digite outra posição:")
                
            
            test1 = not position in valid_positions
            square = self._grid.getPosition(position)
            test2 = square == "x" or square == "o"
        
        return position

    
    def analyze(self):
        """
        Review the grid to see if there are any winners. 
        And return "x won" or "o won" or "tied" "no winner" .
        """
        squares = self._grid.getSquares()

        x_won = ["x","x","x"]
        o_won = ["o","o","o"]

        status = "no winner"

        #Analyzes lines:
        for line in squares:
            if line == x_won:
                status = "x won"

            elif line == o_won:
                status = "o won"
        
        #Analyzes columns:
        for i in range(3):
            column = [squares[0][i], squares[1][i], squares[2][i]]
            if column == x_won:
                status = "x won"

            elif  column == o_won:
                status = "o won"
        
        #Analyzes diagonal:
        diagonal1 = [squares[0][0], squares[1][1], squares[2][2]]
        diagonal2 = [squares[0][2], squares[1][1], squares[2][0]]

        if diagonal1 == x_won or diagonal2 == x_won:
            status =  "x won"

        elif diagonal1 == o_won or diagonal2 == o_won:
            status = "o won

        #analyze if there was a tie:
        if status == "no winner" and self._plays == 9:
            status = "tied"
        
        return status

    def printResult(self):
        """
        Print the final result. It can be:
        - Jogador X Vence!!
        - Jogador O venceu!!
        - Jogo empatado.
        """
        if self.analyze() == "x won":
            print("Jogador X venceu!!")

        
        elif self.analyze() == "o won":
            print("Jogador O venceu!!")
        
        else:
            print("Jogo empatado.")