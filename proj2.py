import sys

#parser not working yet
#parser = argparse.ArgumentParser()
#parser.add_argument('db_type_option')
#args = parser.parse_args()
#if args.db_type_option ==

def CreateDB():
    print("Create and populate selected")
    return

def SearchByKey():
    print("Search by key selected")
    return

def SearchByData():
    print("Search by data selected")
    return

def SearchByRange():
    print("Search by range selected")
    return

def DestroyDB():
    print("Destroy database selected")
    return

def Quit():
    quit = input("Quit selected. Are you sure(y/n)?")
    if quit.lower() == 'y':
        sys.exit(0)
    
    elif quit.lower() == 'n':
        print('Returning to main menu.')
        return
    
    else:
        print('Input not recognized, returning to main menu.')
        return
    
def main():
    command = {
        1 : CreateDB,
        2 : SearchByKey,
        3 : SearchByData,
        4 : SearchByRange,
        5 : DestroyDB,
        6 : Quit,
        }
    screen = [
        "Choose from the following commands:",
        "1 : CreateDB",
        "2 : SearchByKey",
        "3 : SearchByData",
        "4 : SearchByRange",
        "5 : DestroyDB",
        "6 : Quit"
        ]
    while True:
        for i in range(0,7):
            print(screen[i])
            
        choice = int(input("Please enter a command: "))
        if choice in command:
            command[choice]()
        else:
            print("Invalid choice, try again.")
            
            
if __name__ == "__main__":
    main()