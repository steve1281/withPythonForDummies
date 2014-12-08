__author__ = 'steve1281'

tryAgain = True

while tryAgain:
    try:
        value = int(input('type a whole number. '))
    except ValueError:
        print("you must type a while number!")

        try:
            doOver = input("try again (y/n)? ")
        except:
            print("ok - see you next time")
            tryAgain = False
        else:
            if (str.upper(doOver) == "N"):
                tryAgain = False
    except KeyboardInterrupt:
        print ("you pressed ctrl-c")
        print ("see you next time!")
        tryAgain = False

    else:
        print(value)
        tryAgain = False


