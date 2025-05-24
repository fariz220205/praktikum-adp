while True :
    print("=== Sistem Persamaan Linier ===")
    persamaan_linier = int(input("Masukkan banyak persamaan linier (2/3): "))
    variabel = int(input("Masukkan banyak variabel dalam persamaan linier (1/2/3): "))
    if persamaan_linier > variabel :
        print(" SPL tidak memiliki solusi")
    if persamaan_linier < variabel :
        print(" SPL memiliki banyak solusi (tak terhingga)")
    if persamaan_linier==variabel :
        print("SPL memiliki solusi tunggal")
        break

matriks=[]
for i in range(persamaan_linier):
    print(f"Persamaan ke-{i+1}:")
    baris = []
    for j in range(variabel):
        koefisien = float(input(f"  Masukkan koefisien x{j+1}: "))
        baris.append(koefisien)
    konstanta = float(input("  Masukkan nilai konstanta: "))
    baris.append(konstanta)
    matriks.append(baris)
print("matriks")
for  baris in matriks :
    print(baris)

eliminasi_gauss = True 
for k in range (variabel) :
    bagi=matriks[k][k]
    if matriks[k][k]==0 :
        print("elemen diagonal pada baris ",k+1," adalah nol,sehingga tidak dapat dilakukan pembagian")
        eliminasi_gauss = False
        break
    for j in range(persamaan_linier+1) :
        matriks [k][j]/=bagi
    for i in range(variabel) :
        if i != 1 :
            f = matriks[i][k]
            for j in range (variabel+1) :
                matriks[i][j]-=f*matriks[k][j]
       

if eliminasi_gauss :
    print("matriks seteleh di eliminasi gauss")
    for baris_matriks in matriks :
        print(baris_matriks)
    print("solusinya : ")
    for i in range(persamaan_linier) :
        print(f"x{i+1}={matriks[i][variabel]}")
else :
    print("eliminasi gauss tidak berhasil")