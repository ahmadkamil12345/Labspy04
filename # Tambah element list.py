# Tambah element list
## Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
a = [6, 7, 8, 9, 10]
b = []

b.extend(a[0:2])
print(b)

## tambah list B dengan nilai string
print()
b.extend("5")
print(b)

## tambah list B dengan 3 nilai
print()
print(b + [12, 13, 14])

## gabungkan list B dengan list A
print()
print(a + b)
