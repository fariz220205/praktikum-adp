# program untuk mengestimasi luas daerah di bawah kurva f(x) = x^2 + 2x menggunakan metode riemann

n=int(input("masukkan nilai n : "))
Xa=1
Xb=3
delta_x=(Xb-Xa)/n
luas=0
for i in range(1, n+1):
    Xi=Xa+i*delta_x
    fx=Xi**2+2*Xi
    luas+=fx
luas*=delta_x
print(f"Luas derah dari fungsi x^2 + 2x dengan batas daerah x=1 dan x=3 dan jumlah partisi n={n} dengan luas daerah di bawah kurva :{luas}")