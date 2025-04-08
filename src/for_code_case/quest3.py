def quest3(n):
    for i in range(1, n+1):

        match i:
            case 1:
                print("Um  elefante incomoda muita gente")
                print(i+1, "elefantes", "incomodam "*(int(i)+2), "muito mais")

            case _ if i!=2:
                print(i-1, "elefantes incomodam muita gente")
                print(i, "elefantes", "incomodam "*i, "muito mais")

quest3(3)