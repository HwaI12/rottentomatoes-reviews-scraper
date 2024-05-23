import datetime

def convert_date(date_str):
    """
    日付文字列を変換する関数
    """
    date_obj = datetime.datetime.strptime(date_str, "%b %d, %Y")
    return date_obj.strftime("%Y-%m-%d")
