import json
import os
import requests
from banner.banner import banner
from colorama import Fore, Style

TOOLS_FILE = "data/tools.json"

def load_tools():
    with open(TOOLS_FILE, "r") as file:
        return json.load(file)


def install_tool(name, url):
    print(Fore.YELLOW + f"\n📥 Installing {name}..." + Style.RESET_ALL)
    os.system(f"git clone {url}")
    print(Fore.GREEN + f"✔ Installed: {name}\n" + Style.RESET_ALL)


def category_menu(category, tools):
    os.system("clear")
    banner()
    print(Fore.MAGENTA + f"📦 Category: {category}\n" + Style.RESET_ALL)

    keys = list(tools.keys())
    for i, tool in enumerate(keys, 1):
        print(f"{i}) {tool}")

    print("0) Back\n")
    choice = input("Select tool: ")

    if choice == "0":
        return

    index = int(choice) - 1
    if 0 <= index < len(keys):
        install_tool(keys[index], tools[keys[index]])
    else:
        print("❌ Invalid Choice!")


def main_menu():
    tools = load_tools()

    while True:
        os.system("clear")
        banner()

        print(Fore.CYAN + "📁 CATEGORIES:\n" + Style.RESET_ALL)
        cats = list(tools.keys())

        for i, cat in enumerate(cats, 1):
            print(f"{i}) {cat}")

        print("\n9) Update Store")
        print("0) Exit\n")

        choice = input("Select: ")

        if choice == "0":
            exit()

        elif choice == "9":
            os.system("bash update.sh")
            input("Press Enter...")
            continue

        index = int(choice) - 1
        if 0 <= index < len(cats):
            category_menu(cats[index], tools[cats[index]])
        else:
            print("❌ Invalid Choice!")


if __name__ == "__main__":
    main_menu()
