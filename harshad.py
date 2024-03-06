class Harshad:
    def __init__(self):
        self.num = self.getNum()
        self.numList = []
        self.giveHarshad()
        self.resetVals()

    def getNum(self):
        num = input("Enter your number: ")
        return num

    def giveHarshad(self):
        i = 0
        count = 0
        while count != int(self.num):
            i+= 1
            if i < 10:
                self.numList.append(i)
                count += 1
            else:
                temp = str(i)
                loop = len(temp)
                summation = 0
                for x in range(0, loop):
                    summation += int(temp[x])
                if i % summation == 0:
                    self.numList.append(i)
                    count += 1
                    


        print("Harshad number",self.num,"is", self.numList[int(self.num)-1])
        return self.numList[int(self.num)-1]

    def resetVals(self):
        self.numList = []
