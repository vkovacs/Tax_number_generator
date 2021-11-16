# https://hu.wikipedia.org/wiki/Ad%C3%B3azonos%C3%ADt%C3%B3_jel
from datetime import date
input_customer_birth_date = date(1982, 10, 3)
input_customer_serial_number = str(13)


reference_date = date(1867, 1, 1)
customer_elapsed_days = str((input_customer_birth_date - reference_date).days)

part1 = str(8)
part2 = customer_elapsed_days.zfill(5)
part3 = input_customer_serial_number.zfill(3)

tax_number_without_checksum = part1 + part2 + part3

print(f"Adóazonosító az ellenőrző utolsó számjegy nélkül: {tax_number_without_checksum}")

position = 1
checksum = 0
for i in tax_number_without_checksum:
    checksum = checksum + int(i) * position
    position = position + 1

checksum = checksum % 11

if checksum == 10:
    print("Invalid customer_serial_number, checksum mod 11 cannot be 10!")
    raise SystemExit

tax_number = tax_number_without_checksum + str(checksum)
print(f"Adóazonosító : {tax_number}")
