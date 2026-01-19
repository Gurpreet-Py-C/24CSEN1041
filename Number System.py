DIGITS = "0123456789ABCDEF"
def from_base_real(num_str: str, base: int) -> float:
    if not (2 <= base <= 16):
        raise ValueError("Base must be between 2 and 16.")
    num_str = num_str.strip().upper()
    sign = -1 if num_str.startswith("-") else 1
    if num_str.startswith("-"):
        num_str = num_str[1:]
    if "." in num_str:
        int_part, frac_part = num_str.split(".")
    else:
        int_part, frac_part = num_str, ""
    value = int(int_part, base) if int_part else 0
    frac_value = 0.0
    power = base
    for ch in frac_part:
        frac_value += DIGITS.index(ch) / power
        power *= base
    return sign * (value + frac_value)
def to_base_real(value: float, base: int, precision: int = 10) -> str:
    if not (2 <= base <= 16):
        raise ValueError("Base must be between 2 and 16.")
    if value == 0:
        return "0"
    sign = "-" if value < 0 else ""
    value = abs(value)
    int_part = int(value)
    frac_part = value - int_part
    int_digits = []
    while int_part > 0:
        int_part, rem = divmod(int_part, base)
        int_digits.append(DIGITS[rem])
    int_str = "".join(reversed(int_digits)) if int_digits else "0"
    frac_digits = []
    for _ in range(precision):
        frac_part *= base
        digit = int(frac_part)
        frac_digits.append(DIGITS[digit])
        frac_part -= digit
        if frac_part == 0:
            break
    return sign + int_str + ("." + "".join(frac_digits) if frac_digits else "")
def convert_base_real(num_str: str, base_from: int, base_to: int, precision: int = 10) -> str:
    decimal_value = from_base_real(num_str, base_from)
    return to_base_real(decimal_value, base_to, precision)
if __name__ == "__main__":
    n = input("Enter number: ")
    b1 = int(input("Enter input base (2-16): "))
    b2 = int(input("Enter output base (2-16): "))
    p = int(input("Enter decimal precision: "))
    print("Converted:", convert_base_real(n, b1, b2, p))