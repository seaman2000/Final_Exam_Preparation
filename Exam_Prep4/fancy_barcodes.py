import re

number_of_barcodes = int(input())

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
pattern_digits = r'\d'

for _ in range(number_of_barcodes):
    current_barcode = input()
    match = re.fullmatch(pattern, current_barcode)

    if match is None:
        print("Invalid barcode")

    else:
        digits = re.findall(pattern_digits, match.group())
        if not digits:
            print(f"Product group: 00")

        else:
            print(f"Product group: {''.join(digits)}")

