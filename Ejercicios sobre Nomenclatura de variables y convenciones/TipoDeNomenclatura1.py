# Observa las siguientes variables y escribe qué tipo de convención de nomenclatura
# se está utilizando (camelCase, PascalCase, snake_case, SCREAMING_SNAKE_CASE,
# kebab-case).
# a) totalAmount
# b) TotalAmount
# c) total_amount
# d) TOTAL_AMOUNT
# e) total-amount

totalAmount = 100
TotalAmount = 200
total_amount = 300
TOTAL_AMOUNT = 400
# total-amount no es válida como variable en Python, así que la usamos como string
total_amount_kebab = "total-amount"

print("totalAmount:", totalAmount)
print("Convención: camelCase\n")

print("TotalAmount:", TotalAmount)
print("Convención: PascalCase\n")

print("total_amount:", total_amount)
print("Convención: snake_case\n")

print("TOTAL_AMOUNT:", TOTAL_AMOUNT)
print("Convención: SCREAMING_SNAKE_CASE\n")

print("total-amount:", total_amount_kebab)
print("Convención: kebab-case (no se puede usar como variable en Python, solo como string)\n")
