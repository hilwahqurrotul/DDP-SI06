from Gempa import *

# Membuat objek gempa dengan lokasi dan skala
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# Info Gempa
print("## Gempa bumi info ##")
print()
gempa1.dampak() # Memanggil method dampak()

print()
print("## Gempa bumi info ##")
print()
gempa2.dampak() # Memanggil method dampak()

print()
print("## Gempa bumi info ##")
print()
gempa3.dampak() # Memanggil method dampak()

print()
print("## Gempa bumi info ##")
print()
gempa4.dampak() # Memanggil method dampak()

print()
print("## Gempa bumi info ##")
print()
gempa5.dampak() # Memanggil method dampak()
