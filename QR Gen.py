import qrcode

lis = eval(input("Enter the list: "))
dict = {}

def qcode(data,name,num):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")

    img.save("QR CODES/"+str(k)+" "+name+".png")

j = 504901

for i in lis:    
    dict[j] = i
    j += 1

print(dict)

val = list(dict.values())
ke = list(dict.keys())

for k in range(0,len(val)):
    p = str(ke[k])+" "+str(val[k])
    qcode(p,p,k)