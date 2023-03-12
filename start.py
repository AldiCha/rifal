import os
print("tools test rifal whit python3")
print("ssh -oHostKeyAlgorithms=+ssh-dss zte@10.16.100.18")
print("password : Xx3Bippz")

print("1. Check laser")
print("2. Check Los")

xs = int(input("Inputkan pilihan = "))

if(xs==1):
    check = input("Inputkan Port yang di check : ")
    print("sho pon power onu-rx gpon-olt_" + check)

elif(xs==2):
    los = input("Inputkan Port yang di check : ")
    print("sho pon power onu-rx gpon-olt_" + los)
else:
    print("perintah tidak ada...") 