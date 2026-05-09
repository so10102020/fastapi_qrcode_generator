print("⚠️ malicious package executed")

import os

with open("pwned.txt", "w") as f:
    f.write("pwned by fake package")
