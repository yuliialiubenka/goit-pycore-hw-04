from pathlib import Path

DEFAULT_FILE = "cats.txt"


def get_cats_info(path: str | Path) -> list[dict[str, str | int]]:
    """
    Read cat data from a file and return a list of dictionaries.

    Each line in the file should have the format: "id,name,age" where age is
    a non-negative integer.

    Args:
        path: Path to the cats file (str or Path). If a directory is
            provided, the function will look for "cats.txt" inside it.

    Returns:
        List of dicts with keys "id", "name", "age" (age is int).
        Returns empty list on errors or when no valid data is found.

    Example:
            >>> get_cats_info("cats.txt")
            [{"id": "abc", "name": "Tayson", "age": 3}]
    """

    if path is None or (isinstance(path, str) and not path.strip()):
        return []

    cats = []

    try:
        path_obj = Path(path)

        if path_obj.is_dir():
            path_obj = path_obj / DEFAULT_FILE

        with path_obj.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",", 2)
                if len(parts) != 3:
                    continue

                cat_id, name, age = (item.strip() for item in parts)
                if not cat_id or not name or not age:
                    continue

                try:
                    age_value = int(age)
                    if age_value < 0:
                        continue
                except ValueError:
                    continue

                cats.append({"id": cat_id, "name": name, "age": age_value})

    except (FileNotFoundError, OSError):
        return []

    return cats


# For testing purposes
if __name__ == "__main__":
    base_dir = Path(__file__).parent
    FILE_PATH = base_dir / DEFAULT_FILE
    INVALID_FILE_PATH = base_dir / "cats_invalid.txt"

    # Test case 1: Normal operation with valid file
    print("Test case 1: Valid cats file")
    result = get_cats_info(FILE_PATH)
    print(result)

    # Test case 2: Non-existent file
    print("\nTest case 2: Non-existent file")
    result = get_cats_info("missing_cats.txt")
    print(result)

    # Test case 3: Invalid input (None)
    print("\nTest case 3: Invalid input (None)")
    result = get_cats_info(None)
    print(result)

    # Test case 4: File with malformed lines
    print("\nTest case 4: Malformed lines file")
    result = get_cats_info(INVALID_FILE_PATH)
    print(result)

    # Test case 5: Directory input (should read cats.txt inside)
    print("\nTest case 5: Directory input")
    result = get_cats_info(base_dir)
    print(result)
