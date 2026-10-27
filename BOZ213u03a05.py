secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

tahmin = int(input("Lütfen bir sayı girin: "))

while tahmin != secret_number:
    print("Ha ha! You're stuck in my loop!")
    tahmin = int(input("Tekrar bir sayı girin: "))

print(tahmin)
print("Well done, muggle! You are free now.")
