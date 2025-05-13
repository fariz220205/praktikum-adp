# Daftar pelanggan dengan nomor pelanggan, nama pelanggan, dan total belanja
no_pelanggan = ["1","2","3","4","5","6"]
nama_pelanggan = ["budi","abdul","lili","arvin","jamal","wawan"]
total_belanja = ["200.000","150.000","200.000","300.000","50.000","80.000"]

#menambahkan,menghapus,mencetak,dan keluar dari list pelanggan     
while True :
      print("    ")
      print("opsi menu :")
      print("1.upgrade data")
      print("2.hapus data")
      print("3.cetak data")
      print("4.keluar")
      opsi=int(input("masukan nomor yang diberikan : "))
      if opsi == 1 :
          for i in range(opsi) :
               nama=input("Masukkan nama pelanggan yang ingin di-upgrade: ")
               harga=(input("masukkan total belanja dari pelanggan yang ingin di-upgrade: "))
               nomor=str(len(no_pelanggan)+1)
               no_pelanggan.append(nomor)
               nama_pelanggan.append(nama)
               total_belanja.append(harga)
               print("data sudah di upgrade")
     
      if opsi == 2 :
          pelanggan=int(input("masukan pelanggan yang mau dihapus :"))
          nama_pelanggan.pop(pelanggan)
          total_belanja.pop(pelanggan)
          no_dihapus=(len(no_pelanggan)-1)
          no_pelanggan.pop(no_dihapus)
          print("data sudah dihapus")

      if opsi == 3 :
          print ("daftar pelanggan")
          print(f"{'no':5}{'nama':15}{'total belanja (Rp.)':15}")
          for i in range (len(no_pelanggan)):
               print(f"{no_pelanggan[i]:5}{nama_pelanggan[i]:15}{total_belanja[i]:15}")

     
      if opsi == 4 :
           print("pengisian data sudah selesai")
           break
      
      if opsi != 4 and 3 and 2 and 1 :
          continue