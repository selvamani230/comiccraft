from PIL import Image, ImageDraw, ImageFont
import os

def generate_image(prompt: str, panel_num: int):
    # Path set pannurom
    base_dir = os.path.dirname(__file__)
    panels_dir = os.path.join(base_dir, "static", "panels")
    os.makedirs(panels_dir, exist_ok=True)

    file_name = f"panel_{panel_num}.png"
    file_path = os.path.join(panels_dir, file_name)
    
    # Web la kaamikura path
    web_path = f"/static/panels/{file_name}"

    # Oru dummy comic image create pannurom
    img = Image.new('RGB', (500, 500), color=(255, 255, 200))
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rectangle([0, 0, 499, 499], outline=(108, 92, 231), width=8)
    
    # Text
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except:
        font = ImageFont.load_default()

    # Prompt ah 2 line ah split panni ezhuthurom
    text = f"Panel {panel_num}\n\n{prompt[:80]}"
    draw.multiline_text((20, 20), text, fill=(0,0,0), font=font, spacing=10)
    
    # Cat emoji maathiri oru simple drawing
    draw.ellipse([150, 250, 350, 450], fill=(255, 150, 100), outline=(0,0,0), width=3)
    draw.text((200, 320), "😺", font=font, fill=(0,0,0))

    img.save(file_path)
    print(f"Image saved: {file_path}")
    
    return web_path