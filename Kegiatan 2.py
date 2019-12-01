berkas = open('L200190168.txt', 'w')
berkas.writelines('L200190168 \n')
berkas.writelines('05/31/00 \n')
berkas.writelines('Imawan Luthfi Pambudi \n')
berkas.writelines('Karanganyar ')
berkas.close()

berkas = open('L200190168.txt', 'r')
NIM = berkas.readline()
TL = berkas.readline()
Nama = berkas.readline()
T = berkas.readline()
ttl = T + TL

print(Nama)
print(ttl)
print(NIM)
