class Board:
    key= [" ","o","x"]

    board = {"a1": " ", "a2" : " ", "a3" : " ",
             "b1": " ", "b2" : " ", "b3" : " ",
             "c1": " ", "c2" : " ", "c3" : " "}

    def printBoard(self):
        b = self.board


        print("   1   2   3")
        print("a|",b.get("a1"),"|",b.get("a2"),"|",b.get("a3"),"|")
        print("b|",b.get("b1"),"|",b.get("b2"),"|",b.get("b3"),"|")
        print("c|",b.get("c1"),"|",b.get("c2"),"|",b.get("c3"),"|")

  
