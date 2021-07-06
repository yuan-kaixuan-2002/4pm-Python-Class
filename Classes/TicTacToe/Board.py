class Board:
    key= [" ","o","x"]

    
    board = [[" "," "," "],
             [" "," "," "],
             [" "," ",""]]

    def printBoard(self):
        b = self.board


        print("   1   2   3")
        print("a|",b[0][0],"|",b[0][1],"|",b[0][2],"|")
        print("b|",b[1][0],"|",b[1][1],"|",b[1][2],"|")
        print("c|",b[2][0],"|",b[2][1],"|",b[2][2],"|")




    def checkWin(self):
        b = self.board
        for n in range(3):
            if(b[n][0]==b[n][1] ==b[n][2]):
                if(b[n][0]=="x"):
                    return 1
                else:
                    return 2

            if(b[0][n]==b[1][n]==b[2][n]):
                if(b[0][n]=="x"):
                    return 1
                else:
                    return 2

        if(b[0][0]==b[1][1] ==b[2][2]):
            if(b[0][0]=="x"):
                return 1
            else:
                return 2

        if(b[2][0]==b[1][1] ==b[2][0]):
            if(b[2][0]=="x"):
                return 1
            else:
                return 2

        return 0







