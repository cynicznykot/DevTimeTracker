import pystray
from PIL import Image, ImageDraw


def create_icon():
    image = Image.new('RGB', (64, 64), 'white')
    draw = ImageDraw.Draw(image)
    draw.ellipse([8, 8, 56, 56], fill='green')
    return image


def on_click(icon, item):
    print(f"✅ Clicked: {item}")


icon = pystray.Icon(
    'test',
    create_icon(),
    'Test Tray',
    menu=pystray.Menu(
        pystray.MenuItem('Item 1', on_click),
        pystray.MenuItem('Item 2', on_click),
    )
)

print("🚀 Running...")
icon.run()