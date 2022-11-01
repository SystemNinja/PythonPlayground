import subprocess
import os


applications = ["chrome", "opera", "slack", "ringcentral-embeddable-voice", "prospect-mail", "brave-browser-beta",
                "autokey-qt"]

subprocess.run("/home/white/Work/Setton Consulting/scripts/linux/change_tz.sh")
for app in applications:
    print(app)
    os.system("pkill -f "+app)
