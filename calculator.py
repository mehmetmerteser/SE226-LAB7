
import math_utils

def main():
    try:
        x = float(input("Birinci sayıyı girin: "))
        y = float(input("İkinci sayıyı girin: "))
        op = input("İşlem seç (+, -, *, /, **, %): ")

        operations = {
            '+': math_utils.add,
            '-': math_utils.subtract,
            '*': math_utils.multiply,
            '/': math_utils.divide,
            '**': math_utils.power,
            '%': math_utils.mod,
        }

        if op in operations:
            result = operations[op](x, y)
            print("Sonuç:", result)
        else:
            print("Geçersiz işlem operatörü.")
    except ValueError:
        print("Lütfen geçerli sayılar girin.")

if __name__ == "__main__":
    main()
