print("tempat makan : Rp. 50.000")
print("shampo : Rp. 70.000")
print("sabun : Rp. 60.000")
print("minyak : Rp. 70.000")
print("susu : Rp. 50.000")
print("kemeja : Rp. 100.000")
print("parfum : Rp. 80.000")
print("galon : Rp. 60.000")
print("sendal : Rp. 50.000")
print("celana : Rp. 90.000")
barang=(input("masukkan barang yang dibeli: "))
if barang == "tempat makan":
    harga = 50000
    nama = "tempat makan"
elif barang == "shampo":
    harga = 70000
    nama = "shampo"
elif barang == "sabun":
    harga = 60000
    nama = "sabun"
elif barang == "minyak": 
    harga = 70000
    nama = "minyak"
elif barang == "susu":
    harga = 50000
    nama = "susu"
elif barang == "kemeja":
    harga = 100000
    nama = "kemeja"
elif barang == "parfum":
    harga = 80000
    nama = "parfum"
elif barang == "galon":
    harga = 60000
    nama = "galon"
elif barang == "sendal":
    harga = 50000
    nama = "sendal"
elif barang == "celana":
    harga = 90000
    nama = "celana"
else :
    harga = 0
    nama = "barang tidak ada"
    print("barang tidak ada")

if harga > 0:
    kuantitas = int(input("masukan banyak barang yang dibeli: "))
    if harga > 0 :
        total_barang = harga*kuantitas
        print("barang yang dibeli adalah " +nama) 
        print("sebanyak",kuantitas,"buah")
        print("dengan harga satuan Rp.",harga) 
        print("dengan total harga Rp.",total_barang)
        if total_barang <1000000 :
            diskon = 0
            harga_diskon = total_barang - diskon
            print("potongan harga yang didapat Rp.",diskon)
            print("harga yang harus dibayar adalah Rp.",harga_diskon)
        elif 1500000 >= total_barang >= 1000000 :
            diskon = total_barang * 0.1
            harga_diskon = total_barang - diskon
            print("potongan harga yang didapat Rp.",diskon)
            print("harga yang harus dibayar adalah Rp.",harga_diskon)
        elif total_barang > 1500000 :
            diskon = total_barang * 0.15
            harga_diskon = total_barang - diskon
            print("potongan harga yang didapat Rp.",diskon)
            print("harga yang harus dibayar adalah Rp.",harga_diskon)
    else :
        print("harga barang tidak ditemukan")
else :
    print("harga barang tidak ditemukan")
