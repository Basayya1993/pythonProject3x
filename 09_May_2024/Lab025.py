class Browser():
    password = None
    username = None

    def __init__(self):
        self.__password = "Basu123"
        self.username = "basu.online.com"

    def login_browser(self):
        print("Privated:",self.__password)


a = Browser()
a.login_browser()

print(a.username)
