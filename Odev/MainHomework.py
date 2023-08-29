def CreateNumberList():
    newList = []
    while True:
        number = int(input("Bir sayı girin (çıkış için 0): "))
        if number == 0:
            break
        newList.append(number)
    return newList

def MaxNumber(numberList):
    maxNumber = -99999999
    for i in numberList:
        if i > maxNumber:
            maxNumber = i
    return maxNumber

numberList = CreateNumberList()
print("Numbers", numberList)
print("Max number is: ", MaxNumber(numberList))
