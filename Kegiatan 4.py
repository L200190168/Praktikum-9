data = shelve.open('Luthfi.data')
data['berkas'] = [NIM, TTL, Nama, Kota]
print(data['berkas'] [0])
print(data['berkas'] [1])
print(data['berkas'] [2])
print(data['berkas'] [3])