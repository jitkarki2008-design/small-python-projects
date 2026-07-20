# 10 - QR Code Generator using qrcode + Pillow
import qrcode
import os

def generate_qr():
    data = input("\nEnter text / URL to make QR: ").strip()
    if not data:
        print("Empty input!")
        return

    file_name = input("Save as (default qr.png): ").strip() or "qr.png"
    
    # color customization - Pillow concept
    print("\n--- Customization (optional) ---")
    fill = input("QR color (default black): ").strip() or "black"
    back = input("Background color (default white): ").strip() or "white"

    # QR settings
    qr = qrcode.QRCode(
        version=1,  # size 1-40
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # make_image uses Pillow behind the scenes
    img = qr.make_image(fill_color=fill, back_color=back)
    
    # ensure .png extension
    if not file_name.lower().endswith(".png"):
        file_name += ".png"

    img.save(file_name)
    print(f"\nQR saved! -> {os.path.abspath(file_name)}")
    print(f"Open it to scan: {file_name}")

print("--- QR Code Generator [qrcode + Pillow] ---")
while True:
    generate_qr()
    again = input("\nMake another? (y/n): ").lower()
    if again != 'y':
        break

print("Done!")