# modules
import requests

# check updates
def updater():
    version = "1.0.0"
    try:
        check = str(requests.get("https://raw.githubusercontent.com/muyeed15/iras_scheduler/main/version.txt").text)

        if check == version:
            return False, check, version
        else:
            return True, check, version
    except:
        check = version
        return False, check, version
