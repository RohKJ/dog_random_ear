from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
import webbrowser


root = Path(__file__).resolve().parent
html_file = root / "dog_ear_roulette.html"

if not html_file.exists():
    raise FileNotFoundError(f"Put {html_file.name} in the same folder.")

os.chdir(root)

server = ThreadingHTTPServer(("127.0.0.1", 0), SimpleHTTPRequestHandler)
url = f"http://127.0.0.1:{server.server_port}/index.html"

print(f"Dog Random Ear: {url}")
print("Close this window or press Ctrl+C to stop the local server.")
webbrowser.open(url)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
