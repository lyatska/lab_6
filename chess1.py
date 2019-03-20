class ChessSet:
    """
    Class that represents the ChessSet.
    """
    def __init__(self, board):
        pieces = []
        self.board = board
        if self.board == 1:
            #white pieces
            for r in ["a", "h"]:
                pieces.append((Rook("white").type, Position(1, r).get_position()))
            for n in ["b", "g"]:
                pieces.append((Knight("white").type, Position(1, n).get_position()))
            for b in ["c", "f"]:
                pieces.append((Bishop("white").type, Position(1, b).get_position()))
            
            for p in ["a", "b", "c","d", "e", "f", "g", "h"]:
                pieces.append((Pawn("white").type, Position(2, p).get_position()))
            pieces.append((King("white").type, Position(1, "d").get_position()))
            pieces.append((Queen("white").type, Position(1, "e").get_position()))

            #red pieces
            for r in ["a", "h"]:
                pieces.append((Rook("red").type, Position(8, r).get_position()))
            for n in ["b", "g"]:
                pieces.append((Knight("red").type, Position(8, n).get_position()))
            for b in ["c", "f"]:
                pieces.append((Bishop("red").type, Position(8, b).get_position()))
            
            for p in ["a", "b", "c","d", "e", "f", "g", "h"]:
                pieces.append((Pawn("red").type, Position(7, p).get_position()))
            pieces.append((King("red").type, Position(8, "d").get_position()))
            pieces.append((Queen("red").type, Position(8, "e").get_position()))

            #black pieces
            for r in ["a", "h"]:
                pieces.append((Rook("black").type, Position(12, r).get_position()))
            for n in ["b", "g"]:
                pieces.append((Knight("black").type, Position(12, n).get_position()))
            for b in ["c", "f"]:
                pieces.append((Bishop("black").type, Position(12, b).get_position()))
            
            for p in ["a", "b", "c","d", "e", "f", "g", "h"]:
                pieces.append((Pawn("black").type, Position(11, p).get_position()))
            pieces.append((King("black").type, Position(12, "d").get_position()))
            pieces.append((Queen("black").type, Position(12, "e").get_position()))

        if self.board == 2:
            #white pieces
            for r in ["c", "j"]:
                pieces.append((Rook("white").type, Position(8, r).get_position()))
            for n in ["d", "h"]:
                pieces.append((Knight("white").type, Position(9, n).get_position()))
            for b in [11, 10, 9]:
                pieces.append((Bishop("white").type, Position(b, "k" ).get_position()))
            
            for i in ["b", "k"]:
                pieces.append((Pawn("white").type, Position(11, i).get_position()))
            for i in ["c", "i"]:
                pieces.append((Pawn("white").type, Position(10, i).get_position()))
            for i in [ "d", "h"]:
                pieces.append((Pawn("white").type, Position(9, i).get_position()))
            for i in ["e", "g"]:
                pieces.append((Pawn("white").type, Position(8, i).get_position()))
            pieces.append((Pawn("white").type, Position(7, "f").get_position()))          
            pieces.append((King("white").type, Position(10, "e").get_position()))
            pieces.append((Queen("white").type, Position(10, "g").get_position()))

            #black pieces
            for r in ["c", "j"]:
                pieces.append((Rook("black").type, Position(1, r).get_position()))
            for n in ["d", "h"]:
                pieces.append((Knight("black").type, Position(1, n).get_position()))
            for b in [1, 2, 3]:
                pieces.append((Bishop("black").type, Position(b, "f" ).get_position()))
            
            for i in ["b", "k"]:
                pieces.append((Pawn("black").type, Position(1, i).get_position()))
            for i in ["c", "i"]:
                pieces.append((Pawn("black").type, Position(2, i).get_position()))
            for i in [ "d", "h"]:
                pieces.append((Pawn("black").type, Position(3, i).get_position()))
            for i in ["e", "g"]:
                pieces.append((Pawn("black").type, Position(4, i).get_position()))
            pieces.append((Pawn("black").type, Position(5, "f").get_position()))          
            pieces.append((King("black").type, Position(1, "e").get_position()))
            pieces.append((Queen("black").type, Position(1, "g").get_position()))

        if self.board == 3:
            #white pieces
            for r in ["d", "k"]:
                pieces.append((Rook("white").type, Position(1, r).get_position()))
            for n in ["e", "j"]:
                pieces.append((Knight("white").type, Position(1, n).get_position()))
            for b in ["f", "i"]:
                pieces.append((Bishop("white").type, Position(1, b).get_position()))
            
            for p in ["d", "e", "f", "g", "h", "i", "j", "k"]:
                pieces.append((Pawn("white").type, Position(2, p).get_position()))
            pieces.append((King("white").type, Position(1, "g").get_position()))
            pieces.append((Queen("white").type, Position(1, "h").get_position()))


            #yellow pieces
            for r in [11, 4]:
                pieces.append((Rook("yellow").type, Position(r, "a").get_position()))
            for n in [5, 10]:
                pieces.append((Knight("yellow").type, Position(n, "a").get_position()))
            for b in [6, 9]:
                pieces.append((Bishop("yellow").type, Position(b, "a").get_position()))
            
            for p in [4, 5, 6, 7, 8, 9, 10, 11]:
                pieces.append((Pawn("yellow").type, Position(p, "b").get_position()))
            pieces.append((King("yellow").type, Position(7, "a").get_position()))
            pieces.append((Queen("yellow").type, Position(8, "a").get_position()))

            #red pieces
            for r in [11, 4]:
                pieces.append((Rook("red").type, Position(r, "n").get_position()))
            for n in [5, 10]:
                pieces.append((Knight("red").type, Position(n, "n").get_position()))
            for b in [6, 9]:
                pieces.append((Bishop("red").type, Position(b, "n").get_position()))
            
            for p in [4, 5, 6, 7, 8, 9, 10, 11]:
                pieces.append((Pawn("red").type, Position(p, "m").get_position()))
            pieces.append((King("red").type, Position(8, "n").get_position()))
            pieces.append((Queen("red").type, Position(7, "n").get_position()))


            #black pieces
            for r in ["d", "k"]:
                pieces.append((Rook("black").type, Position(14, r).get_position()))
            for n in ["e", "j"]:
                pieces.append((Knight("black").type, Position(14, n).get_position()))
            for b in ["f", "i"]:
                pieces.append((Bishop("black").type, Position(14, b).get_position()))
            
            for p in ["d", "e", "f", "g", "h", "i", "j", "k"]:
                pieces.append((Pawn("black").type, Position(13, p).get_position()))
            pieces.append((King("black").type, Position(14, "h").get_position()))
            pieces.append((Queen("black").type, Position(14, "g").get_position()))

        if self.board == 4:
            #white pieces
            for r in ["a", "h", "i", "p"]:
                pieces.append((Rook("white").type, Position(1, r).get_position()))
            for n in ["b", "g", "j", "o"]:
                pieces.append((Knight("white").type, Position(1, n).get_position()))
            for b in ["c", "f", "k", "n"]:
                pieces.append((Bishop("white").type, Position(1, b).get_position()))
            
            for p in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]:
                pieces.append((Pawn("white").type, Position(2, p).get_position()))
            for k in ["d", "i"]:
                pieces.append((King("white").type, Position(1, k).get_position()))
            for q in ["e", "m"]:
                pieces.append((Queen("white").type, Position(1, q).get_position()))

            #black pieces
            for r in ["a", "h", "i", "p"]:
                pieces.append((Rook("black").type, Position(12, r).get_position()))
            for n in ["b", "g", "j", "o"]:
                pieces.append((Knight("black").type, Position(12, n).get_position()))
            for b in ["c", "f", "k", "n"]:
                pieces.append((Bishop("black").type, Position(12, b).get_position()))
        
            for p in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]:
                pieces.append((Pawn("black").type, Position(11, p).get_position()))
            for k in ["d", "i"]:
                pieces.append((King("black").type, Position(12, k).get_position()))
            for q in ["e", "m"]:
                pieces.append((Queen("black").type, Position(12, q).get_position()))
            
        self.pieces= pieces

    def __str__(self):
        return "{}".format(self.pieces)
    
        

        
class Position:
    """
    Class that represents a position/
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_position(self):
        """
        Return a tuple of coordinates.
        """
        return (self.x, self.y)
    
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    

class Piece:
    """
    Class that represents a piece.
    """

    def __init__(self, color):
        self.color = color
        
    def __str__(self):
        return self.color
    
    
    
class King(Piece):
    """
    Class that represents the King.
    """
  
    def __init__(self, color):
        super().__init__(color)
        if self.color == "black":
            type = "Black King"
        if self.color == "white":
            type = "White King"
        if self.color == "yellow":
            type = "Yellow King"
        if self.color == "red":
            type = "Red King"
        
        self.type = type
   
    def __str__(self):
        return "{}".format(self.type)

class Knight(Piece):
    """
    Class that represents the Knight.
    """
    
    def __init__(self, color):
        
        super().__init__(color)
        if self.color == "black":
            type = "Black Knight"
        if self.color == "white":
            type = "White Knight"
        if self.color == "yellow":
            type = "Yellow Knight"
        if self.color == "red":
            type = "Red Knight"
        
        
        self.type = type
    def __str__(self):
        return "{}".format(self.type)

   

class Bishop(Piece):
    """
    Class that represents the Bishop.
    """

    def __init__(self, color):
        super().__init__(color)
        if self.color == "black":
            type = "Black Bishop"
        if self.color == "white":
            type = "White Bishop"
        if self.color == "yellow":
            type = "Yellow Bishop"
        if self.color == "red":
            type = "Red Bishop"
        
        
        self.type = type
    def __str__(self):
        return "{}".format(self.type)


class Rook(Piece):
    """
    Class that represents the Rook.
    """
    def __init__(self, color):
        super().__init__(color)
        if self.color == "black":
            type = "Black Rook"
        if self.color == "white":
            type = "White Rook"
        if self.color == "yellow":
            type = "Yellow Rook"
        if self.color == "red":
            type = "Red Rook"
        
        
        self.type = type
    def __str__(self):
        return "{}".format(self.type)
 

class Pawn(Piece):
    """
    Class that represents the Pawn.
    """
    def __init__(self, color):
        super().__init__(color)
        if self.color == "black":
            type = "Black Pawn"
        if self.color == "white":
            type = "White Pawn"
        if self.color == "yellow":
            type = "Yellow Pawn"
        if self.color == "red":
            type = "Red Pawn"
        
        
        self.type = type
    def __str__(self):
        return "{}".format(self.type)

    

class Queen(Piece):
    """
    Class that represents the Queen.
    """
    def __init__(self, color):
        super().__init__(color)
        if self.color == "black":
            type = "Black Queen"
        if self.color == "white":
            type = "White Queen"
        if self.color == "yellow":
            type = "Yellow Queen"
        if self.color == "red":
            type = "Red Queen"
        
        
        self.type = type 
    def __str__(self):
        return "{}".format(self.type)  

  
        
if __name__ == "__main__":
    text = '''
    Варіанти шахівниць:
    1 -  Шестикутна шахівниця для гри утрьох зі стартовою позицією
    2 -  Один з варіантів шестикутних шахів Глинського
    3 -  Шахівниця для гри вчотирьох зі стартовою позицією
    4 -  Шахівниця для подвоєних шахів зі стартовою позицією
    Виберіть тип шахів під заданим числом,щоб отримати
    інформацію про розміщення шахових фігур : '''
    
    
    name_of_chess = int(input(text))
    chess = ChessSet(name_of_chess)
    if chess.board == 1:
        print("Ви обрали шестикутну шахівницю для гри утрьох зі стартовою позицією." + "\n")
        
    if chess.board == 2:
        print("Ви обрали один з варіантів шестикутниз шахів Глинського." + "\n")
        
    if chess.board == 3:
        print("Ви обрали шахівницю для гри вчотирьох зі стартовою позицією. " + "\n")
        
    if chess.board == 4:
        print("Ви обрали шахівницю для подвоєних шахів зі стартовою позицією. " + "\n")
 
    print("Розміщення фігур відбувається таким чином: " + "\n")
    print(chess)



    