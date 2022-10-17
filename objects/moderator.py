from objects.grid import Grid
from objects.player import Player
import os

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
        self.clear()
        symbol = self._currentPlayer.getSymbol()
        self._grid.printGrid()
        
        position = input("\nJogador %s, escolha uma posição:" % symbol).upper()
        position = self._validatePosition(position)
        
        self._currentPlayer.markSquare(self._grid, position)

        #Change the current Player:
        if self._currentPlayer == self._playerX:
            self._currentPlayer = self._playerO
        
        else:
            self._currentPlayer = self._playerX
        
        self._plays += 1
    
    def _validatePosition(self, position):
        """
        Analyzes if the given position 
        is valid and if it has been typed before. 
        If it is not valid or it's was typed before, ask the user
        to enter the position again.
        """
        position = self._validateLetter(position)   
        
        square = self._grid.getSquare(position)
        test = square == "x" or square == "o"

        while test:
            print("\n  Ops! Essa posição já foi escolhida antes.")
            position = input("Digite outra posição:").upper()
            position = self._validateLetter(position)
            
            square = self._grid.getSquare(position)
            test = square == "x" or square == "o"
        
        return position
    
    def _validateLetter(self, position):
        """
        Analyzes if the given position is valid.
        If it's not valid, ask the user
        to enter the position again.
        """
        valid_positions = Grid.coord.keys()

        test = not position in valid_positions

        while test:
            print("\n  Ops! Você digitou algo inválido.")
            print("Digite apenas uma letra do alfabeto entre A e I.")
            position = input("Digite novamente:").upper()
            
            test = not position in valid_positions  

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
            status = "o won"

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
        self.clear()
        self._grid.printGrid()

        if self.analyze() == "x won":
            print("\nJogador X venceu!!\n")

        
        elif self.analyze() == "o won":
            print("\nJogador O venceu!!\n")
        
        else:
            print("\nJogo empatado.\n")
    
    def clear(self):
        """
        Clear the screen.
        """
        
        if os.name == "nt": #if the Operational System is Windows
            os.system("cls") 
            
        else:
            os.system("clear")