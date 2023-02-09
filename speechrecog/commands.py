import subprocess
import os

class Commander:
    def __init__(self):
        self.confirm = ["y", "Y", "yes", "Yes"]
        self.cancel = ["N", "n", "No", "no"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            self.respond("My name is pie commander.")

    def respond(self, response):
        subprocess.call(" echo \"" + response + "\"|rtts", shell=True)