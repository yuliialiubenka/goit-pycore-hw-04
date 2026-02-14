import sys
from pathlib import Path
from colorama import Fore, Style, init


def walk_directory(current: Path, prefix: str = "") -> None:
    """
    Recursively walk and print directory structure.

    Args:
        current: Current directory path to process.
        prefix: Prefix string for tree formatting (internal use).
    """
    try:
        entries = sorted(current.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except OSError:
        print(f"{prefix}|-- {Fore.RED}[permission denied]{Style.RESET_ALL}")
        return

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "`-- " if is_last else "|-- "
        next_prefix = "    " if is_last else "|   "

        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{entry.name}{Style.RESET_ALL}/")
            walk_directory(entry, prefix + next_prefix)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def print_directory_structure(path: str | Path) -> None:
    """
    Print a colored directory tree for the given path.

    Args:
        path: Path to the directory (str or Path object).
            Supports relative and absolute paths.

    Raises:
        SystemExit: If path is invalid, doesn't exist, or is not a directory.
    """

    if path is None or (isinstance(path, str) and not path.strip()):
        print("Invalid path.")
        raise SystemExit(1)

    try:
        root = Path(path).resolve()
    except (OSError, ValueError) as e:
        print(f"Error processing path: {e}")

    if not root.exists():
        print(f"Path not found: {root}")
        raise SystemExit(1)
    if not root.is_dir():
        print(f"Path is not a directory: {root}")
        raise SystemExit(1)

    init(autoreset=True)
    print(f"{Fore.BLUE}{root.name}{Style.RESET_ALL}/")

    walk_directory(root)


# For testing purposes
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_3/task_3.py <path_to_directory>")
        raise SystemExit(1)

    print_directory_structure(sys.argv[1])
