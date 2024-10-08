import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    from Crypto.Protocol.KDF import scrypt
except ImportError:
    print("pycryptodome tidak ditemukan. Menginstal...")
    install("pycryptodome")
from Instagram import Instagram
