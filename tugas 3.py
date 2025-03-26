n=int(input("masukkan jumlah pendaftar : "))
print("     ")
for i in range (1,n+1) :
    print("         ")
    nama=input("masukkan nama pendaftar : ")
    matkul=input("masukkan mata kuliah yang diminati pendaftar : ")
    
    while True :
        nilai_wawancara=int(input("masukkan nilai wawancara : "))
        if 0 <= nilai_wawancara <= 100 :
            break 
        else :
            print("nilai wawancara tidak valid")
            continue
        
    while True :
        tes_tulis=int(input("masukkan nilai tes tulis : "))
        if 0 <= tes_tulis <= 100 :
            break
        else :
            print("nilai tes tulis tidak valid")
            continue
        
    while True :
        tes_mengajar=int(input("masukan nilai mengajar : "))
        if 0 <= tes_mengajar <= 100 :
            break
        else :
            print("nilai mengajar tidak valid")
            continue
        
    rata_rata1=(nilai_wawancara+tes_tulis+tes_mengajar)/3

    if rata_rata1 >= 80 :
        print("        ")
        print("pendaftar no.",i)
        print("Nama :",nama)
        print("Mata Kuliah yang diminati :",matkul)
        print("Nilai Wawancara :",nilai_wawancara)
        print("Nilai Tes Tulis :",tes_tulis)
        print("Nilai Mengajar :",tes_mengajar)
        print("Keterangan : Lulus")
    else :
        print("        ")
        print("pendaftar no.",i)
        print("Nama :",nama)
        print("Mata Kuliah yang diminati :",matkul)
        print("Nilai Wawancara :",nilai_wawancara)
        print("Nilai Tes Tulis :",tes_tulis)
        print("Nilai Mengajar :",tes_mengajar)
        print("Keterangan : Tidak Lulus")