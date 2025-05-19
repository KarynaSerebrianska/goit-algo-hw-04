import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_structure(path: Path, indent: int = 0):
    if path.is_dir():
        print("  " * indent + Fore.BLUE + f"📂 {path.name}")
        for child in sorted(path.iterdir()):
            print_structure(child, indent + 1)
    else:
        print("  " * indent + Fore.GREEN + f"📄 {path.name}")

def main():
    if len(sys.argv) < 2:
        print("❌ Будь ласка, вкажіть шлях до директорії як аргумент.")
        sys.exit(1)

    root = Path(sys.argv[1])

    if not root.exists() or not root.is_dir():
        print("❌ Помилка: шлях не існує або це не директорія")
        sys.exit(1)

    print_structure(root)

if __name__ == "__main__":
    main()
