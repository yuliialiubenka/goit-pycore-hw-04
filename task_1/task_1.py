from decimal import Decimal, InvalidOperation
from pathlib import Path

ZERO = Decimal("0")
DEFAULT_FILE = "salaries.txt"


def format_money_tuple(data: tuple[Decimal, Decimal]) -> tuple[Decimal, Decimal]:
    return (
        data[0].quantize(Decimal("0.01")),
        data[1].quantize(Decimal("0.01")),
    )


def total_salary(path: str | Path) -> tuple[Decimal, Decimal]:
    """
    Calculate the total and average salary from a text file.

    Each line in the file should have the format: "Name,Salary".

    Args:
        path: Path to the salary file (str or Path)

    Returns:
        Tuple of (total_salary, average_salary). Returns (Decimal('0'), Decimal('0')) on errors
        or when no valid salaries are found.

    Example:
        >>> total_salary("salaries.txt")
        (6000, 2000)
    """

    if path is None or (isinstance(path, str) and not path.strip()):
        return ZERO, ZERO

    total = ZERO
    count = 0

    try:
        path_obj = Path(path)

        if path_obj.is_dir():
            path_obj = path_obj / DEFAULT_FILE

        with path_obj.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",", 1)
                if len(parts) != 2:
                    continue

                try:
                    salary_str = parts[1].strip()
                    salary = Decimal(salary_str)
                except InvalidOperation:
                    continue

                if not salary.is_finite():
                    continue

                total += salary
                count += 1

    except (FileNotFoundError, OSError):
        return ZERO, ZERO

    if count == 0:
        return ZERO, ZERO

    average = total / count
    return format_money_tuple((total, average))


# For testing purposes
if __name__ == "__main__":
    base_dir = Path(__file__).parent
    FILE_PATH = base_dir / DEFAULT_FILE

    # Test case 1: Normal operation with valid file
    print("Test case 1: Valid salary file")
    total_salary_sum, average_salary = total_salary(str(FILE_PATH))
    print(f"Total salary: {total_salary_sum}, Average salary: {average_salary}")

    # Test case 2: Non-existent file (error handling)
    print("\nTest case 2: Non-existent file")
    total_salary_sum, average_salary = total_salary("non_existent.txt")
    print(f"Total salary: {total_salary_sum}, Average salary: {average_salary}")

    # Test case 3: Invalid input (None)
    print("\nTest case 3: Invalid input (None)")
    total_salary_sum, average_salary = total_salary(None)
    print(f"Total salary: {total_salary_sum}, Average salary: {average_salary}")

    # Test case 4: Directory input (should read salaries.txt inside)
    print("\nTest case 4: Directory input")
    total_salary_sum, average_salary = total_salary(base_dir)
    print(f"Total salary: {total_salary_sum}, Average salary: {average_salary}")
