if __name__ == '__main__':
    #Silahkan masukan jawaban anda disini
    jumlah_hari = 485 
    tahun = jumlah_hari//360
    sisa_tahun = jumlah_hari%360
    bulan = sisa_tahun//30
    sisa_bulan = sisa_tahun%30
    minggu = sisa_bulan//7
    sisa_minggu = sisa_bulan%7
    print(f'{tahun} tahun, {bulan} bulan, {minggu} minggu, {sisa_minggu} hari')