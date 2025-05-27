def hitung_tagihan(kwh, golongan):
    tarif_awal = [1500,2500,4000,5000]
    tarif_lebih = [2000,3000,5000,7000]
    batas = 100
    if golongan == 1:
        if kwh <= batas:
            tagihan = kwh * tarif_awal[0]
            return tagihan
        else:
            tagihan_lebih = (batas * tarif_awal[0])+((kwh - batas) * tarif_lebih[0])
            return tagihan_lebih
    elif golongan == 2:
        if kwh <= batas:
            tagihan = kwh * tarif_awal[1]
            return tagihan
        else:
            tagihan_lebih=(batas * tarif_awal[1])+((kwh - batas) * tarif_lebih[1])
            return tagihan_lebih
    elif golongan == 3:
        if kwh <= batas:
            tagihan = kwh * tarif_awal[2]
            return tagihan
        else:
            tagihan_lebih =(batas * tarif_awal[2])+((kwh - batas) * tarif_lebih[2])
            return tagihan_lebih
    elif golongan == 4:
        if kwh <= batas:
            tagihan = kwh * tarif_awal[3]
            return tagihan
        else:
            tagihan_lebih =(batas * tarif_awal[3])+((kwh - batas) * tarif_lebih[3])
            return tagihan_lebih
    else :
        if kwh <= batas:
            tagihan = kwh * tarif_awal[2]
            return tagihan
        else:
            tagihan_lebih =(batas * tarif_awal[2])+((kwh - batas) * tarif_lebih[2])
            return tagihan_lebih
        
print("golongan tarif")
print("golongan 1 :Rp. 1500/kwh untuk 100 kwh pertama,selanjutnya Rp. 2000/kwh")
print("golongan 2 :Rp. 2500/kwh untuk 100 kwh pertama,selanjutnya Rp. 3000/kwh")
print("golongan 3 :Rp. 4000/kwh untuk 100 kwh pertama,selanjutnya Rp. 5000/kwh")
print("golongan 4 :Rp. 5000/kwh untuk 100 kwh pertama,selanjutnya Rp. 7000/kwh")        
print("   ")
kwh = int(input("Masukkan pemakaian listrik anda (kWh): "))
golongan = int(input("Masukkan golongan listrik anda (1-4): "))
print("  ")
print(f"Tagihan listrik anda: Rp {hitung_tagihan(kwh,golongan)}")