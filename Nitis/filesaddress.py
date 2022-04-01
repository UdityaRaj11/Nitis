import subprocess


class Filesaddress:

    def call_application(self, application):
#Browsers
        if "Google Chrome" in application or "chrome" in application:
            subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        elif "Internet Explorer" in application:
            subprocess.Popen('C:\\Program Files\\Internet Explorer\\iexplore.exe')
        elif "Mozilla Firefox" in application:
            subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        elif "Microsoft edge" in application:
            subprocess.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
#office apps
        elif "microsoft word" in application or "ms word" in application:
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
        elif "microsoft powerpoint" in application or "ms powerpoint" in application:
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE')
        elif "microsoft excel" in application or "ms excel" in application:
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE')
        elif "microsoft onenote" in application or "ms onenote" in application or "onenote" in application:
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')
#other apps
        elif "spotify" in application:
            subprocess.Popen('C:\\Users\\Uditya Raj\\AppData\\Roaming\\Spotify\\Spotify.exe')
        elif "discord" in application:
            subprocess.Popen('C:\\Users\\Uditya Raj\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe')
