# modules
import requests

# check updates
def updater():
    version = 1.0
    try:
        check = float(requests.get('https://raw.githubusercontent.com/muyeed15/iras_scheduler/main/version.txt').text)

        if check > version:
            return True, check, version
        else:
            return False, check, version
    except:
        check = version
        return False, check, version
