import qrcode
from PIL import Image

# QR Code URL
url = "https://sacredhaloconnection.com/vip"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create QR code image with sage green color
qr_img = qr.make_image(fill_color="#4A5349", back_color="#F5F3E7")

# Save simple QR code
qr_img.save("vip/qr-code-vip.png")
print("✓ VIP QR code saved: vip/qr-code-vip.png")

# Create larger branded version
canvas_width = 800
canvas_height = 1000
canvas = Image.new('RGB', (canvas_width, canvas_height), '#F5F3E7')

# Resize QR code
qr_img = qr_img.resize((500, 500))

# Position QR code
qr_x = (canvas_width - 500) // 2
qr_y = 300
canvas.paste(qr_img, (qr_x, qr_y))

# Save branded version
canvas.save("vip/qr-code-vip-branded.png")
print("✓ Branded VIP QR code saved: vip/qr-code-vip-branded.png")

print(f"\n✓ VIP QR codes created successfully!")
print(f"  URL: {url}")
print(f"  Location: /home/user/webapp/vip/")
