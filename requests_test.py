import requests
from io import BytesIO
from PIL import Image

print(requests.get("https://google.com").status_code)