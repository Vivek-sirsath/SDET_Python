f = open("abc.txt","r")
print(f.tell())   # 0  - Initial index position of cursor.
print(f.read(3))   # Fil
print(f.tell())   # 3  - Next index  position of cursor after reading data.

f.seek(9)   # Seeking the cursor to the 9th index position.
print(f.tell())   # 9  - Index position of the cursor after seeking.

f.close()







