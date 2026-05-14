"""<DevLog — a personal developer productivity tool for the terminal.>"""

VERSION = "0.1.0"

def show_banner():
    print("====================")
    print(f"   DevLog v{VERSION}")
    print("====================")

def main():
    show_banner()
    print("DevLog is ready.")

if __name__ == "__main__":
    main()