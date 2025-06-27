import random
import time
import os

def loading():
    print('hello,player')
    print(" ")
    time.sleep(1)
    os.system("cls")
    print("loading")
    for i in range(101):
        persen = i
        bar = '█' * (i // 2) + '-' * (50 - i // 2)
        print(f'\rProgress: |{bar}| {persen}%', end='')
        time.sleep(0.02)
    print('\nGame completed')
    time.sleep(1)

def pembersih_output():
    os.system("cls")

def main_menu():
    pembersih_output()
    while True:
        print("\n========== THE NUMBER HUNT GAME ==========")
        print("1. Main")
        print("2. Lihat Skor")
        print("3. Keluar")
        pilihan = input("Pilih (1/2/3): ")
        if pilihan == '1':
            print(" ")
            print("\n========== MODE GAME ==========")
            print("1. mode normal")
            print("2. mode waktu")
            print("3. mode pvp")
            mode = input("pilih (1/2/3) :")
            if mode == '1':
                play_game()
            elif mode == '2':
                play_game_time()
            elif mode == '3':
                play_game_pvp()
            else:
                print("mode tidak valid")
        elif pilihan == '2':
            print(" ")
            print("========== LEADERBOARD MODE ==========")
            print('1. leaderboard mode biasa')
            print('2. leaderboard mode waktu')
            pil_leaderboard = input("pilih (1/2) :")
            if pil_leaderboard == '1':
                leaderboard_normal()
            elif pil_leaderboard == '2':
                leaderboard_time()
            else:
                print("Pilihan tidak valid.")
        elif pilihan == '3':
            print("\nTerima kasih sudah bermain. Sampai jumpa kembali :)")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def pilih_level(pvp=False):
    while True:
        if pvp:
            print("\nPilih Tingkat Kesulitan PVP:")
            print("1. PVP Special normal(1-250)")
            print("2. PVP special hard(1-500)")
            print("3. PVP special ekstrem(1-1000)")
            level = input("Pilih (1/2/3): ")
            if level == '1':
                return 1, 250, 0, "PVP special normal"
            if level == "2" :
                return 1, 500, 0, "PVP special hard"
            if level == '3' :
                return 1, 1000, 0, "PVP special ekstrem"
            else:
                print("Pilihan tidak valid. Silakan pilih angka 1.")
        else:
            print("\nPilih Tingkat Kesulitan:")
            print("1. Easy (1-50)")
            print("2. Medium (1-100)")
            print("3. Hard (1-200)")
            print("4. Impossible (1-250)")
            level = input("Pilih (1/2/3/4): ")

            if level == '1':
                return 1, 50, 10, "Easy"
            elif level == '2':
                return 1, 100, 10, "Medium"
            elif level == '3':
                return 1, 200, 10, "Hard"
            elif level == '4':
                return 1, 250, 10, "Impossible"
            else:
                print("Pilihan tidak valid. Silakan pilih angka 1-4.")

def beri_clue(angka, level_id):
    clues = []
    if level_id == "Easy":
        if angka % 2 == 0:
            clues.append("Angka genap")
        else:
            clues.append("Angka ganjil")
        if angka % 5 == 0:
            clues.append("Kelipatan 5")
        if angka > 25:
            clues.append("Lebih besar dari 25")
        if angka < 25:
            clues.append("Lebih kecil dari 25")
        if angka % 10 == 0:
            clues.append("Kelipatan 10")
    elif level_id == "Medium":
        if angka > 25:
            clues.append("Lebih besar dari 25")
        if angka < 75:
            clues.append("Lebih kecil dari 75")
        if angka % 3 == 0:
            clues.append("Kelipatan 3")
        if angka % 4 == 0:
            clues.append("Kelipatan 4")
        if angka % 7 == 0:
            clues.append("Kelipatan 7")
        if str(angka).endswith("5"):
            clues.append("Angka diakhiri 5")
    elif level_id == "Hard":
        if angka > 150:
            clues.append("Lebih besar dari 150")
        if angka < 50:
            clues.append("Lebih kecil dari 50")
        if angka % 4 == 0:
            clues.append("Kelipatan 4")
        if angka % 6 == 0:
            clues.append("Kelipatan 6")
        if angka % 9 == 0:
            clues.append("Kelipatan 9")
        if str(angka)[0] == "1":
            clues.append("Angka diawali 1")
    elif level_id == "Impossible":
        if angka > 100:
            clues.append("Lebih besar dari 100")
        if angka < 200:
            clues.append("Lebih kecil dari 200")
        if angka % 7 == 0:
            clues.append("Kelipatan 7")
        if angka % 11 == 0:
            clues.append("Kelipatan 11")
        if angka % 13 == 0:
            clues.append("Kelipatan 13")
        if str(angka)[-1] == "9":
            clues.append("Angka diakhiri 9")
    elif level_id == "PVP special normal":
        if angka % 2 == 0:
            clues.append("Angka genap")
        else:
            clues.append("Angka ganjil")
        if angka % 5 == 0:
            clues.append("Kelipatan 5")
        if angka % 7 == 0:
            clues.append("Kelipatan 7")
        if angka > 200:
            clues.append("Lebih besar dari 200")
        if angka < 100:
            clues.append("Lebih kecil dari 100")
        if angka % 10 == 0:
            clues.append("Kelipatan 10")
        if str(angka).startswith("1"):
            clues.append("Angka diawali 1")
        if angka % 4 == 0:
            clues.append("Kelipatan 4")
    elif level_id == "PVP special hard":
        if angka % 3 == 0:
            clues.append("Kelipatan 3")
        if angka % 6 == 0:
            clues.append("Kelipatan 6")
        if angka > 300:
            clues.append("Lebih besar dari 300")
        if angka < 200:
            clues.append("Lebih kecil dari 200")
        if angka % 10 == 0:
            clues.append("Kelipatan 10")
        if angka % 9 == 0:
            clues.append("Kelipatan 9")
        if angka % 8 == 0:
            clues.append("Kelipatan 8")
        if angka % 5 == 0:
            clues.append("Kelipatan 5")
        if str(angka)[-1] == "7":
            clues.append("Angka diakhiri 7")
    elif level_id == "PVP special ekstrem":
        if angka % 11 == 0:
            clues.append("Kelipatan 11")
        if angka > 700:
            clues.append("Lebih besar dari 700")
        if angka < 300:
            clues.append("Lebih kecil dari 300")
        if angka % 2 == 0:
            clues.append("Angka genap")
        else:
            clues.append("Angka ganjil")
        if angka % 13 == 0:
            clues.append("Kelipatan 13")
        if angka % 17 == 0:
            clues.append("Kelipatan 17")
        if angka % 100 == 0:
            clues.append("Kelipatan 100")
        if str(angka).startswith("9"):
            clues.append("Angka diawali 9")
        if str(angka)[-1] == "3":
            clues.append("Angka diakhiri 3")
    if not clues:
        clues.append("Tidak ada clue khusus.")
    return random.choice(clues)

def play_game():
    pembersih_output()
    print("========== MODE NORMAL ==========")
    nama = input("Masukkan nama anda: ").strip()
    if not nama:
        nama = "Player"

    min_val, max_val, kesempatan, level_id = pilih_level()
    angka_rahasia = random.randint(min_val, max_val)
    menang = False

    print(f"\nTebak angka dari {min_val} sampai {max_val}!")
    print(f"Anda punya {kesempatan} kesempatan.\n")

    for tebak in range(1, kesempatan + 1):
        tebakan_input = input(f"Tebakan ke-{tebak}: ")
        if tebakan_input.isdigit():
            tebakan = int(tebakan_input)
        else:
            print("Masukkan angka yang valid!")
            continue

        if tebakan == angka_rahasia:
            print(f"🎉 Selamat {nama}! Tebakan Anda benar!")
            menang = True
            break
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar!")
        else:
            print("Angka terlalu kecil!")

        if tebak in [3, 5]:
            hint = beri_clue(angka_rahasia, level_id)
            print(f"💡 Clue: {hint}")

    skor = (kesempatan - tebak + 1) * 10 if menang else 0
    if level_id == "Hard" and menang:
        skor += 15
    elif level_id == "Impossible" and menang:
        skor += 30
    print(f"\nSkor anda: {skor}")
    if not menang:
        print(f"💀 Anda kalah! Angka yang benar adalah {angka_rahasia}")

    save_leaderboard_normal(nama, skor, level_id)
    time.sleep(2)
    pembersih_output()

def play_game_time():
    pembersih_output()
    print("========== MODE WAKTU ==========")
    nama = input("Masukkan nama anda: ").strip()
    if not nama:
        nama = "Player"

    min_val, max_val,_,level_id = pilih_level()
    angka_rahasia = random.randint(min_val, max_val)

    print(f"\nTebak angka dari {min_val} sampai {max_val}!")
    print("Waktu Anda akan dihitung. Semakin cepat, semakin baik!\n")

    start_time = time.time()
    tebak = 0
    while True:
        tebak += 1
        tebakan_input = input(f"Tebakan ke-{tebak}: ")
        if tebakan_input.isdigit():
            tebakan = int(tebakan_input)
        else:
            print("Masukkan angka yang valid!")
            continue

        if tebakan == angka_rahasia:
            print(f"🎉 Selamat {nama}! Tebakan Anda benar!")
            break
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar!")
        else:
            print("Angka terlalu kecil!")

        if tebak in [3, tebak+3]:
            hint = beri_clue(angka_rahasia, level_id)
            print(f"💡 Clue: {hint}")
    pembersih_output()

    end_time = time.time()
    waktu = round(end_time - start_time, 2)

    print(f"\nWaktu anda: {waktu} detik")
    save_leaderboard_time(nama, waktu, level_id)
    time.sleep(2)
    pembersih_output()

def play_game_pvp():
    pembersih_output()
    print("========== MODE PVP ==========")
    nama1 = input("Masukkan nama pemain 1: ").strip() or "Player 1"
    nama2 = input("Masukkan nama pemain 2: ").strip() or "Player 2"

    min_val, max_val, _, level_id = pilih_level(pvp=True)
    angka_rahasia = random.randint(min_val, max_val)
    print(f"\nTebak angka dari {min_val} sampai {max_val}!")
    print(f"Level: {level_id}")
    giliran = 0
    total_tebakan = 0

    while True:
        pemain = nama1 if giliran % 2 == 0 else nama2
        tebakan_input = input(f"{pemain}, masukkan tebakan: ")
        if tebakan_input.isdigit():
            tebakan = int(tebakan_input)
        else:
            print("Masukkan angka yang valid!")
            continue
        total_tebakan += 1
        if tebakan == angka_rahasia:
            print(f"🎉 Selamat {pemain}! Tebakan Anda benar dan menang!")
            break
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar!")
        else:
            print("Angka terlalu kecil!")

        if total_tebakan % 5 == 0:
            hint = beri_clue(angka_rahasia, level_id)
            print(f"💡 Clue: {hint}")
        giliran += 1
    input("\nTekan Enter untuk kembali ke menu...")
    pembersih_output()

def leaderboard_normal():
    pembersih_output()
    print("========== LEADERBOARD MODE BIASA ==========")
    print(f"{'Nama':<15}{'Skor':<10}{'Kesulitan':<12}{'Medali':<8}")
    try:
        with open("leaderboard_normal.txt", "r") as f:
            lines = [line.strip().split(',') for line in f if len(line.strip().split(',')) == 3]
            lines.sort(key=lambda x: int(x[1]), reverse=True)
            for i, data in enumerate(lines):
                medal = ''
                if i == 0:
                    medal = '🥇'
                elif i == 1:
                    medal = '🥈'
                elif i == 2:
                    medal = '🥉'
                print(f"{data[0]:<15}{data[1]:<10}{data[2]:<12}{medal:<8}")
    except FileNotFoundError:
        print("Belum ada skor.")
    input("\nTekan Enter untuk kembali ke menu...")
    pembersih_output()

def leaderboard_time():
    pembersih_output()
    print("========== LEADERBOARD MODE WAKTU ==========")
    print(f"{'Nama':<15}{'Waktu':<10}{'Kesulitan':<20}{'Medali':<8}")
    try:
        with open("leaderboard_time.txt", "r") as f:
            lines = [line.strip().split(',') for line in f if len(line.strip().split(',')) == 3]
            lines.sort(key=lambda x: float(x[1]))
            for i, data in enumerate(lines):
                medal = ''
                if i == 0:
                    medal = '🥇'
                elif i == 1:
                    medal = '🥈'
                elif i == 2:
                    medal = '🥉'
                print(f"{data[0]:<15}{data[1]:<10}{data[2]:<20}{medal:<8}")
    except FileNotFoundError:
        print("Belum ada skor.")
    input("\nTekan Enter untuk kembali ke menu...")

def save_leaderboard_normal(nama, skor, level_id):
    with open("leaderboard_normal.txt", "a") as f:
        f.write(f"{nama},{skor},{level_id}\n")

def save_leaderboard_time(nama, waktu, level_id):
    with open("leaderboard_time.txt", "a") as f:
        f.write(f"{nama},{waktu},{level_id}\n")

pembersih_output()
loading()
main_menu()