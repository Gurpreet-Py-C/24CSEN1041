DIGITS = "0123456789ABCDEF"

def from_base(num_str: str, base: int) -> int:
    if not (2 <= base <= 16):
        raise ValueError("Base must be between 2 and 16.")
    num_str = num_str.strip().upper()
    return int(num_str, base)  # supports 0-9 and A-F for base<=16


def to_base(value: int, base: int) -> str:
    if not (2 <= base <= 16):
        raise ValueError("Base must be between 2 and 16.")
    if value == 0:
        return "0"

    sign = ""
    if value < 0:
        sign = "-"
        value = -value

    out = []
    while value > 0:
        value, rem = divmod(value, base)
        out.append(DIGITS[rem])
    return sign + "".join(reversed(out))


def convert_base(num_str: str, base_from: int, base_to: int) -> str:
    decimal_value = from_base(num_str, base_from)
    return to_base(decimal_value, base_to)


if __name__ == "__main__":
    n = input("Enter number: ")
    b1 = int(input("Enter input base (2-16): "))
    b2 = int(input("Enter output base (2-16): "))

    print("Converted:", convert_base(n, b1, b2))