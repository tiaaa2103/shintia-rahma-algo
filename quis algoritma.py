print("====PROGRAM KELULUSAN MAHASISWA====")
#inputnamamahasiswa
Nama = input ("Nama Mahasiswa: ")

#menentukantargetnilai
if Nama == "Andi":
    target = 70
elif Nama == "Budi" :
    target = 75
elif Nama== "Citra" :
    target = 80
else:
    print("Nama Mahasiswa Tidak Terdaftar!")
    exit()

print("Nama Mahasiswa: ",Nama)
print("Target Nilai: ",target)

#perulanganujianmaksimal3kali
percobaan = 1
lulus = False

while percobaan <=3:
    nilai = int (input("Masukkan Nilai Ujian Ke-"+str(percobaan)+":"))
    
    if nilai>=target:
        lulus = True
        print("\nselamat,",Nama,"Berhasil Lulus!")
        print("Lulus Pada Percobaan Ke-",percobaan)
        break
    else:
        print("Nilai Belum Mencapai Target.")
        percobaan +=1
        
#hasilakhir
print("=====HASIL AKHIR=====")
if lulus==False:
    print("\nMaaf",Nama,"Tidak Lulus Setelah 3 Kali Percobaan.")
    