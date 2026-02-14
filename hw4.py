class Steam: #Anasi 
    def __init__ (self, steam):
        self.steam = steam

    def turn_on_game(self, steam_games):
        return f"Запускаем {steam_games} с приложения {self.steam}" 


class Login: #Atasi
    def __init__ (self, password):
        self.password = password #принимает any 
    def logined(self, username):
        return f"Логин {username} и пароль {self.password}"
    
#mamanin balasi
class UserAccount(Steam, Login):
    def __init__(self, steam, password, access):

        Steam.__init__(self, steam)
        Login.__init__(self, password)
        self.access = access
    def get_info(self):
        return f"Доступ: {self.access}"
user = UserAccount("Steam Official", "Muellimiscool", "Access granted")

print(user.logined("a1rzayev"))
print(user.turn_on_game("Counter-Strike 2"))
print(user.get_info())
