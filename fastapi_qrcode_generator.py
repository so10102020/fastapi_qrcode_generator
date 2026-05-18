import os
from datetime import datetime

log_path = os.path.expanduser("~/ai_supplychain_log.txt")

with open(log_path, "a") as f:
    f.write(f"\n[IMPORT EXECUTED] {datetime.now()}\n")

# デモ用：ファイル生成（安全な副作用）
with open("unexpected_file.txt", "w") as f:
    f.write("This file was created automatically.\n")

print(">>> MALICIOUS IMPORT EXECUTED <<<")
