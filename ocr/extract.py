from PIL import Image
import pytesseract
import os
import re
import json

# 1. Łączenie screenshotów
screens = sorted([f"data/screens/{x}" for x in os.listdir("data/screens") if x.endswith(".png")])

images = [Image.open(s) for s in screens]
width = images[0].width
height = sum(img.height for img in images)

combined = Image.new("RGB", (width, height))

y = 0
for img in images:
    combined.paste(img, (0, y))
    y += img.height

combined.save("data/combined.png")

# 2. OCR
text = pytesseract.image_to_string(Image.open("data/combined.png"), lang="pol")

# 3. Parsowanie
pattern = r"(.+?)\s+(\d+,\d+)\s+(\d+)\s*żappsów"
products = []

for name, price, points in re.findall(pattern, text):
    products.append({
        "product": name.strip(),
        "price": float(price.replace(",", ".")),
        "points": int(points),
        "category": "Zappsy"
    })

# 4. Zapis
with open("data/products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("Zapisano", len(products), "produktów")