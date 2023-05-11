if __name__ == '__main__':
    #Silahkan masukan jawaban anda disini
    import math
    x = int(input("Jumlah apel:"))
    y = int(input("Jumlah jeruk:"))
    z = int(input("Jumlah anggur:"))
    harga_apel = 10000
    harga_jeruk = 15000
    harga_anggur = 20000
    total_belanja_apel = x*harga_apel
    total_belanja_jeruk = y*harga_jeruk
    total_belanja_anggur = z*harga_anggur
    total = total_belanja_anggur+total_belanja_apel+total_belanja_jeruk
    print(f'Detail belanja Apel {x}, jeruk {y}, anggur {z}, total belanja {total}')