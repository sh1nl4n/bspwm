from typing import Literal
import subprocess


class Daemons:
    def docker(self, method: Literal["start", "enable", "disable"]):
        if method in ("start", "enable"):
            subprocess.run(["sudo", "systemctl", method, "docker", "now"], stdout=subprocess.DEVNULL, check=True)


    def ly(self, method: Literal["start", "enable", "disable"]):
        if method in ("start", "enable"):
            subprocess.run(["sudo", "systemctl", method, "ly", "now"], stdout=subprocess.DEVNULL, check=True)