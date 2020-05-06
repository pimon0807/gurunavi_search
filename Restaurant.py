class Restaurant(object):
    def __init__(self, name, url, access):
        self.name = name
        self.url = url
        self.access = access

    def get_shop_info(self):
        access_info = self.access_info()
        return f'{self.name}.{self.url}.{access_info}'

    def access_info(self):
        return f"{self.access['line']}{self.access['station']}{self.access['station_exit']}徒歩{self.access['walk']}分"
