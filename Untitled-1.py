from pathlib import Path
import os


html_file = Path(__file__).with_name("dog_ear_roulette.html")

if not html_file.exists():
    raise FileNotFoundError(f"Put {html_file.name} in the same folder.")

os.startfile(html_file.resolve())
