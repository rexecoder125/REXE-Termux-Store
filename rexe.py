import os

def banner():
    os.system("clear")
    print("""
██████╗ ███████╗██╗  ██╗███████╗
██╔══██╗██╔════╝██║ ██╔╝██╔════╝
██████╔╝█████╗  █████╔╝ █████╗
██╔══██╗██╔══╝  ██╔═██╗ ██╔══╝
██║  ██║███████╗██║  ██╗███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
HACKER TERMUX TOOL STORE
Developer : REXE
""")

def menu():
    print("""
1) Information Gathering
2) Web Tools
3) Network Tools
0) Exit
""")

def info_tools():
    while True:
        os.system("clear")
        print("""
Information Gathering Tools

1) Nmap
2) Red Hawk
3) theHarvester
0) Back
""")

        choice = input("Select tool: ")

        if choice == "1":
            os.system("pkg install nmap -y")
            os.system("nmap")
            input("Press Enter...")

        elif choice == "2":
            os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd RED_HAWK && php rhawk.php")
            input("Press Enter...")

        elif choice == "3":
            os.system("pkg install python -y")
            os.system("pip install theHarvester")
            os.system("theHarvester")
            input("Press Enter...")

        elif choice == "0":
            break

def web_tools():
    while True:
        os.system("clear")
        print("""
Web Tools

1) Subfinder
2) XSStrike
0) Back
""")

        choice = input("Select tool: ")

        if choice == "1":
            os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
            os.system("subfinder")
            input("Press Enter...")

        elif choice == "2":
            os.system("git clone https://github.com/s0md3v/XSStrike")
            os.system("cd XSStrike && pip install -r requirements.txt && python xsstrike.py")
            input("Press Enter...")

        elif choice == "0":
            break

def network_tools():
    while True:
        os.system("clear")
        print("""
Network Tools

1) Hping3
2) Netcat
0) Back
""")

        choice = input("Select tool: ")

        if choice == "1":
            os.system("pkg install hping -y")
            os.system("hping3")
            input("Press Enter...")

        elif choice == "2":
            os.system("pkg install netcat -y")
            os.system("nc")
            input("Press Enter...")

        elif choice == "0":
            break

while True:
    banner()
    menu()

    choice = input("Select: ")

    if choice == "1":
        info_tools()

    elif choice == "2":
        web_tools()

    elif choice == "3":
        network_tools()

    elif choice == "0":
        print("Bye Hacker")
        break
