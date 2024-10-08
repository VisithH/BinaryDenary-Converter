import sys
repeat = True

print("Unnecessary")
while repeat == True:
    print("1) Convert to Denary\n2) Convert to Binary\n3) Exit")
    command = int(input("Enter your choice: "))
    binaryList = []
    if command == 1:
        number = input("Please type in your binary number:\n")
        binaryList = list(map(int, number))
        # if lengthBinary == 2:
        #     print((binaryList[0] * 1) + (binaryList[1] * 2))
        # if lengthBinary == 3:
        #     print((binaryList[0] * 1) + (binaryList[1] * 2) + (binaryList[2] * 4))
        # if lengthBinary == 4:
        #     print((binaryList[0] * 1) + (binaryList[1] * 2) + (binaryList[2] * 4) + (binaryList[3] * 8))
        # if lengthBinary == 5:
        #     print((binaryList[0] * 1) + (binaryList[1] * 2) + (binaryList[2] * 4) + (binaryList[3] * 8) + (
        #                 binaryList[4] * 16))
        # if lengthBinary == 6:
        #     print((binaryList[0] * 1) + (binaryList[1] * 2) + (binaryList[2] * 4) + (binaryList[3] * 8) + (
        #                 binaryList[4] * 16) + (binaryList[4] * 16) + (binaryList[4] * 32))
        power = 0
        denary = 0
        for digit in reversed(binaryList):
            if digit != 0 and digit != 1:
                print("Invalid input")
                sys.exit()
            else:
                if digit == 1:
                    denary = denary + 2 ** power
                power = power + 1
        print(denary)


    elif command == 2:
        binary = ""
        number = int(input("Please type in your denary number:\n"))
        if number < 0:
            print("We do not support that yet :)")
        else:
            while number > 0:
                binary = str(number % 2) + binary
                number = number // 2
            print(binary)

    elif command == 3:
        print("Exiting Program")
        repeat = False
    else:
        print("Invalid input")
        repeat = False
