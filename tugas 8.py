while True :
    print("Menu:")
    print("1. Tambah catatan")
    print("2. Lihat catatan")
    print("3. Keluar")
    opsi = int(input("Pilih menu: "))
    
    if opsi==1 :
        catatan = open("teks catatan.txt",'a')
        teks=input("masukan judul catatan yang mau dimasukan :")
        isi=input("masukan isi dari catatan tersebut ? ")
        catatan.write(f"{teks}: {isi}\n")
        print("catatan berhasil disimpan")
        catatan.close()

    elif opsi==2 :
        with open("teks catatan.txt", "r") as f:
            nomor = 1
            for line in f:
                print(f"{nomor}. {line}")
                nomor += 1
            if nomor == 1:
                print("Belum ada catatan.")

    elif opsi == 3 :
        print("terima kasih,program diakhiri")
        break