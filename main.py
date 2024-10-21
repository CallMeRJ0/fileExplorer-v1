"""
Virtual FIle Explorer
"""

# Variables
BOLD = "\033[1m"
RESET = "\033[0m"
ITALIC = "\033[3m"

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print(f"{BOLD}┌───────────────┐")
    print("│ FILE EXPLORER │")
    print(f"└───────────────┘{RESET}")
   
    action = str(input(" Type 1 to Locate Directory\n Type 2 to view File Directory\n Type 3 to Instructions and Features\n"))
def beginChecks():
    import os
    import time
    clear()
    if os.path.exists("fileData.txt"):
        main()
    else:
        clear()
        user_name = str(input("Select a user name: "))



        
        """
        time.sleep(1.5)
        print(f"{ITALIC}Initializing data Folder{RESET}")
        time.sleep(0.5)
        with open('fileData.txt', 'w') as file:
            # add here the text 1 users on the first line
            # add here the text 2 user1 on the second line
            file.write()
        print(f"{BOLD}Folder Initialize{RESET}")
        time.sleep(0.5)
        clear()
       
       """
    beginChecks()
       
beginChecks()

