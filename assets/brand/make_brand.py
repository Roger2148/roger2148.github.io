"""Favicon set + social preview card, rendered from build.html with headless Chrome so they use the site's fonts.
Run from the repo root with the local server up on :8070:
    conda run -n bcpnn_local python assets/brand/make_brand.py
"""
import subprocess, shutil
from pathlib import Path
from PIL import Image
HERE = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE = "http://127.0.0.1:8070/assets/brand/build.html"
def shot(fragment, w, h, out):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
                    "--force-device-scale-factor=1", "--virtual-time-budget=8000", f"--screenshot={out}", f"{BASE}#{fragment}"],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
tmp = HERE / "_icon.png"; shot("icon", 512, 512, tmp)
src = Image.open(tmp).convert("RGBA")
# transparent outside the rounded square so the icon sits cleanly on any tab strip
mask = Image.new("L", src.size, 0)
from PIL import ImageDraw
ImageDraw.Draw(mask).rounded_rectangle((0, 0, 511, 511), radius=112, fill=255)
src.putalpha(mask)
for size, name in ((512, "icon-512.png"), (192, "icon-192.png"), (180, "apple-touch-icon.png"), (64, "favicon-64.png"), (32, "favicon-32.png")):
    im = src.resize((size, size), Image.LANCZOS)
    if name == "apple-touch-icon.png":          # iOS adds its own corner radius; give it a solid square
        flat = Image.new("RGB", (size, size), (250, 249, 247)); flat.paste(im, mask=im.split()[3]); flat.save(HERE / name, optimize=True)
    else:
        im.save(HERE / name, optimize=True)
Image.open(HERE / "favicon-64.png").save(HERE / "favicon.ico", sizes=[(64, 64), (32, 32), (16, 16)])
tmp.unlink()
shot("card", 1200, 630, HERE / "og-card.png")
im = Image.open(HERE / "og-card.png").convert("RGB"); im.save(HERE / "og-card.png", optimize=True)
print("ok", im.size, (HERE / "og-card.png").stat().st_size // 1024, "KB")
