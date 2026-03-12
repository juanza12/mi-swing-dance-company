import qrcode

url = "http://127.0.0.1:5000"

qr = qrcode.make(url)

qr.save("qr_mi_swing_dance_company.png")