import qrcode

# QR 코드로 변환하고 싶은 URL
url = 'https://www.incheon-old-new.com/'

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=14,
    border=2,
)
qr.add_data(url)
qr.make(fit=True)

# QR 코드 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 이미지 파일로 저장
img.save("인천올드앤뉴2.png")