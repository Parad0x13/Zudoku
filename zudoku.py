import math

class Sudoku:
    def __init__(self, board):
        # [TODO] Add sanity checking for board length
        # [TODO] Account for other board sizes such as not just 3x3x3s
        self.N = int(math.sqrt(len(board)))
        self.n = int(math.sqrt(self.N))

        # Setup the actual board data
        data = []
        for i in range(self.N):
            for ii in range(self.N):
                data.append("123456789")

        # [TODO] Add checks to ensure figures greater than one digit are accounted for
        for i in range(len(board)):
            c = board[i]
            if c != "0": data[i] = c

        self.data = data

    def getRow(self, r):
        # [TODO] Add sanity checking on bounds
        y = r * self.N
        return self.data[y : y + self.N]

    def setRow(self, r, value):
        # [TODO] Add sanity checking on bounds
        y = r * self.N
        for x in range(len(value)):
            self.data[y + x] = value[x]

    def getColumn(self, c):
        # [TODO] Add sanity checking on bounds
        retVal = []

        x = c
        for n in range(self.N):
            retVal.append(self.data[x + n * self.N])

        return retVal

    def setColumn(self, c, value):
        # [TODO] Add sanity checking on bounds
        #x = c
        #for y in range(len(value)):
        #    self.data[x * self.N + y]
        y = c
        for x in range(self.N):
            self.data[y * self.N + x] = value[x]
            # This doesn't work...

    def getBlock(self, b):
        pass

    # [TODO] Make this render nicer
    def render(self):
        solveCount = 0
        for N in range(self.N):
            row = self.getRow(N)

            visual = "|"
            for cell in row:
                if len(cell) > 1:
                    #visual += ". "
                    visual += "{} ".format(cell)
                else:
                    visual += "{} ".format(cell)
                    solveCount += 1

            visual += "|"
            print(visual)
        print("Solve Count: {}".format(solveCount))

    def pruneRow(self, r):
        row = self.getRow(r)
        stables = []
        for cell in row:
            if len(cell) == 1:
                stables.append(cell)

        for i in range(len(row)):
            cell = row[i]
            if len(cell) > 1:
                for s in stables:
                    cell = cell.replace(s, "?")
            row[i] = cell

        self.setRow(r, row)

    def pruneColumn(self, c):
        column = self.getColumn(c)
        stables = []
        for cell in column:
            if len(cell) == 1:
                stables.append(cell)

        for i in range(len(column)):
            cell = column[i]
            if len(cell) > 1:
                for s in stables:
                    cell = cell.replace(s, "?")
            column[i] = cell

        self.setColumn(c, column)

    def solve(self):
        for column in range(self.N):
            self.pruneColumn(column)

game = Sudoku("300000007057080001020030058000958000891304000600071039206000915000020700080009400")

#game.render()
#print()
game.solve()
game.render()
