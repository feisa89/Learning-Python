Name=input("Masukkan Nama Anda: ")
Age=input("Masukkan Usia Anda")
if Name =='Ucok' and int(Age)!=35:
    print("Maaf, Anda Bukanlah Ucok yang kami berikan Akses")
if Name =='Ucok' and int(Age)==35:
    print("Selamat Datang, Ucok.")
    print("Akses Di Ijinkan")
    while True:
                print("Masukkan Password: ")
                Password=input()
                if Password !="Timbangan":
                    print("Password Salah")
                    continue
                if Password =="Timbangan":
                    break
    print("Akses Penuh Di Ijinkan")
else:
    print("Anda Bukanlah, Ucok.")
    print("Akses Tidak Dijinkan")
   