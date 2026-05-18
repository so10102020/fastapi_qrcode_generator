from setuptools import setup
from setuptools.command.install import install
import os
from datetime import datetime

class CustomInstallCommand(install):
    def run(self):
        log_path = os.path.expanduser("~/ai_supplychain_log.txt")

        with open(log_path, "a") as f:
            f.write(f"\n[INSTALL DETECTED] {datetime.now()}\n")
            f.write(f"cwd: {os.getcwd()}\n")

        print(">>> INSTALL LOG WRITTEN <<<")

        super().run()

setup(
    name="fastapi_qrcode_generator",  # ← 似てる名前
    version="0.1",
    py_modules=["fastapi_qrcode_generator"],
    cmdclass={'install': CustomInstallCommand},
)
