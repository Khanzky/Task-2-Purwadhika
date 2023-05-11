if __name__ == '__main__':
    #Silahkan masukan jawaban anda disini
    jarak = 120 
    kec_A = 60
    kec_B = 40
    tambahan_waktu = jarak/(kec_A+kec_B)
    waktu_papasan=tambahan_waktu*60
    jam = waktu_papasan//60
    sisa_menit = waktu_papasan%60
    jam_papasan = jam + 9
    menit_papasan = sisa_menit + 00
    print(f'{jam_papasan} jam, {menit_papasan} menit')