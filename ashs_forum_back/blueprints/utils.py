from datetime import timezone, timedelta

tw_zone = timezone(timedelta(hours=8))
def get_tw_zone():
    return tw_zone