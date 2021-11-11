print("Menghitung Total Keuntungan")
print()
a = 100000000
laba = [a*0, a*0, a*1/100, a*1/100, a*5/100, a*5/100, a*5/100, a*3/100]
bulan = 0
sum = 0

print("Modal Awal",a)
for i in laba:
    sum = sum + i
    bulan += 1
    print("Laba Bulan ke-", bulan, "laba =", i)
print("Keuntungan yang didapat = ", sum)
