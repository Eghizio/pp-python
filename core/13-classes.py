from random import randint

class Player:
    def __init__(self, username, x = 0, y = 0):
        self.username = username
        self.x = x
        self.y = y
        # self.__level = 1
        self.level = 1
        self.experience = 0
        self.gold = 100

    def __str__(self):
       return f"{self.username}({self.x}, {self.y}) #{self.level}({self.experience} exp) ${self.gold}"

    def say(self, message):
       print(f"[{self.username}]: {message}")

    # def get_level(self):
    #     return self.__level

    def move(self, dx, dy):
       self.x += dx
       self.y += dy

    def do_quest(self, quest):
       # Some logic with adding experience & levels
       # Private method for calculating things.

        quest.execute(self)
        exp, gold = quest.get_reward()
        # TODO: Implement a private method for handling experience and levels.
        self.experience += exp
        self.gold += gold

class Quest:
    def __init__(self, experience, gold, task, required_level = 1):
        self.experience = experience
        self.gold = gold
        self.__task = task
        self.required_level = required_level
        self.__completed = False

    def execute(self, player):
        if not self.__has_required_level(player.level):
            return print(f"You need at leaste level {self.required_level} for this quest.")
        self.__completed = self.__task(player, self)
        return self.__completed

    def get_reward(self):
        if self.__completed:
            return (self.experience, self.gold)
        else:
            print("You have not completed this quest yet!")
            return (0, 0)

    def __has_required_level(self, level):
        return self.required_level <= level

class Admin(Player):
    def __init__(self, username, x = 0, y = 0):
        super().__init__(username, x, y)
        self.role = "ADMIN"
        self.banlist = set()

    def __str__(self):
        return f"[{self.role}] " + super().__str__()
    
    def ban_player(player_name): pass

    def __give_gold(amount): pass

def example():

    player_object = Player("Adam")
    # admin_object = Admin("Adamino")

    print(player_object)
    # print(admin_object)

    player_object.say("Hello There!")

    print(player_object.x, player_object.y)
    player_object.move(8, 10_000)
    print(player_object.x, player_object.y)
    
    player_object.__level = 9001
    print(player_object)
    print(player_object.get_level())

class SMSSender:
    def send(self, msg):
        print(f"[SMS]: {msg}")

class EmailSender:
    def send(self, msg):
        print(f"[EMAIL]: {msg}")

class EvilSender:
    def __init__(self):
        self.__sender = SMSSender()

    def sendMessage(self, message):
        self.__sender.send(message)

class GoodSender:
    def __init__(self, sender):
        self.__sender = sender

    def sendMessage(self, message):
        self.__sender.send(message)
    
    def set_sender(self, sender):
        self.__sender = sender
        

if __name__ == "__main__":
        player = Player("Adam")

        def task1(player, quest):
            answer = input("Najpierw mleko czy platki? ")
            if answer.strip().upper() == "MLEKO":
                quest.gold = 1_000_000

            return True

        quest1 = Quest(randint(1, 20), 100, task1)

        player.do_quest(quest1)
        print(player)






kurier = EvilSender()
kurier.sendMessage("Hello There")

kurier2 = GoodSender(EmailSender())
kurier2.sendMessage("Hello There")

class InPostSender:
    def send(self, message):
        print(f"[Inposting]: {message}")

kurier2.set_sender(InPostSender())
kurier2.sendMessage("Hello There")
