import urllib.parse
import qrcode

def generateQr():

    #recibo del usuario el numero de telefono y el query
    telephoneNumber = input("Numero de telefono a redireccionar, con  +549 : ")
    query = input("Texto a escribir : ")

    #realizo un encode para que el query se pueda enviar a la url
    encodeQuery = urllib.parse.quote(query)

    #creo la url con el numero de telefono y el query
    url = "https://api.whatsapp.com/send?phone=" + telephoneNumber + "&text=" + encodeQuery

    #genero el qr con la url
    qr = qrcode.make(url)
    qr.save("A "+telephoneNumber+"_"+query+".png")

    #verifico que el qr se haya generado
    print("QR generado con exito")



if __name__ == "__main__":
    generateQr()