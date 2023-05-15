choice=int(input("enter number beween 1 to 7"))
match choice:
    case 1:
        print("you selected 1")
    case 2:
        print("you selected 2")
    case 3|4|5:
        print("you selected bteween 4 to 5")
    case _:
        print("you selected nmber > 5")
        
    
           
