import datetime


def set_expiration_date(days):
    expiration_date = datetime.datetime.now()+datetime.timedelta(days=days)
    return expiration_date
