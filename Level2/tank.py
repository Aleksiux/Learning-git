import random
import time


class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.score = 300
        self.shots = 0
        self.position = 'n'
        self.positions = {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West'}
        self.shots_fire = {'n': 0, 'e': 0, 's': 0, 'w': 0}

    def forward(self):
        self.y += 1
        self.position = 'n'
        print('You moved North')

    def backwards(self):
        self.y -= 1
        self.position = 's'
        print('You moved South')

    def left(self):
        self.x -= 1
        self.position = 'w'
        print('You moved West')

    def right(self):
        self.x += 1
        self.position = 'e'
        print('You moved East')

    def shooting(self):
        self.shots += 1
        self.shots_fire[self.position] += 1

    def info(self):
        print(f'Tank facing to:{self.positions[self.position]} side')
        print(f'{self.shots_fire} all shots')
        print(f'X:{self.x}, Y:{self.y}')
        print(f"Tank has made:{self.shots} shot's")
        time.sleep(2)

    # def check_enemy(self):
    #     print(f"Target - X:{self.x}, Y:{self.y}")
    #     if self.x == (enemy.x - 1) and self.y == self.y and tank.position == 'e':
    #         print('Nice job you killed target.')
    #         return True
    #     elif tank.x == self.x and tank.y == (self.y - 1) and tank.position == 'n':
    #         print('Nice job you killed target.')
    #         return True
    #     elif tank.x == (self.x + 1) and tank.y == self.y and tank.position == 'w':
    #         print('Nice job you killed target.')
    #         return True
    #     elif tank.x == self.x and tank.y == (self.y + 1) and tank.position == 's':
    #         print('Nice job you killed target.')
    #         return True
    #     else:
    #         print('You missed.')
    #         return False

    def check_enemy(self):
        print(f"Target - X:{self.x}, Y:{self.y}")
        if self.x == enemy.x:
            if self.y < enemy.y and self.position == 'n':
                print('Nice job you killed target.')
                return True
            if self.y > enemy.y and self.position == 's':
                print('Nice job you killed target.')
                return True
            return False
        if self.y == enemy.y:
            if self.x > enemy.x and self.position == 'e':
                return True
            if self.x < enemy.x and self.position == 'w':
                return True
            return False


class Enemy(Tank):
    def __init__(self):
        super().__init__()
        self.x = random.randint(-5, 6)
        self.y = random.randint(-5, 6)


side = []
tank = Tank()
enemy = Enemy()

counter = 0
while tank.score > 0:
    print(tank.score)
    player = input("f,b,l,r. 5-shoot, 1.-info\n-")
    # player = input("Choose what do want to do with tank:\nGo forward-f\nGo backwards-b\nGo left-l\nGo "
    #                "right-r\nIf you want to shoot to your direction press 5.\n1.-Check info.\n0.Quit game\n-")
    if player == 'f':
        tank.forward()
        tank.score -= 10
    elif player == 'b':
        tank.backwards()
        tank.score -= 10
    elif player == 'l':
        tank.left()
        tank.score -= 10
    elif player == 'r':
        tank.right()
        tank.score -= 10
    elif player == '1':
        tank.info()
    elif player == '5':
        tank.shooting()
        if enemy.check_enemy():
            tank.score += 70
            counter += 1
            enemy = Enemy()
            print(f"You killed one and now your score is - {tank.score} and you killed {counter} targets.")
    elif player == '0':
        print(f"You ended game with:{tank.score} and {counter} kills")
        break

print(f"You ended game with:{tank.score} and {counter} kills")
