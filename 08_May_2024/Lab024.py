class Gmail_login():
    Username = None
    Password = None

    def __init__(self,G_Username,G_Password):
        self.Username = G_Username
        self.Password = G_Password

    def login(self):
        if self.Password =="Basu123":
            print("Valid Password is:", self.Password)
        else:
            print("Invalid Password")

Amit = Gmail_login("Amit","Amit123")
Amit.login()

Basu = Gmail_login("Basu","Basu123")
Basu.login()
