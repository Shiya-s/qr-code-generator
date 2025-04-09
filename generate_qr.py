import qrcode

form_url = "https://forms.gle/6KtKKtWt7hrtVyzm6"
img = qrcode.make(form_url)
img.save("lost_and_found_qr.png")

print("QR code generated! Check 'lost_and_found_qr.png'.")
