from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot('Megatron')
        self.dinosaur = Dinosaur('T-Rex', 25)
        

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to an epic battle for the ages! Only on side can win!')
        print(input(f'Who would you like to win, {self.robot.name} or {self.dinosaur.name}? Enter here: '))
        print("")

    def battle_phase(self):

        self.robot.attack(self.dinosaur)
        print('Megatron attacked T-Rex with a sword for 25 damage!')
        print(f'T-Rex health is now at {self.dinosaur.health}!')
        print('')

        self.dinosaur.attack(self.robot)
        print('T-Rex attacked Megatron for 25 damage!')
        print(f'Megatrons health is now at {self.robot.health}! ')
        print('')

        self.robot.attack(self.dinosaur)
        print('Megatron attacked T-Rex with a sword for 25 damage!')
        print(f'T-Rex health is now at {self.dinosaur.health}!')
        print('')

        self.dinosaur.attack(self.robot)
        print('T-Rex attacked Megatron for 25 damage!')
        print(f'Megatrons health is now at {self.robot.health}!')
        print('')

        self.robot.attack(self.dinosaur)
        print('Megatron attacked T-Rex with a sword for 25 damage!')
        print(f'T-Rex health is now at {self.dinosaur.health}!')
        print('')

        self.dinosaur.attack(self.robot)
        print('T-Rex attacked Megatron for 25 damage!')
        print(f'Megatrons health is now at {self.dinosaur.health}!')
        print('')

        self.robot.attack(self.dinosaur)
        print('Megatron attacked T-Rex with a sword for 25 damage!')
        print(f'T-Rex has {self.dinosaur.health} health remaining!')
        print('')
 
    def display_winner(self):
        print('Megatron made T-Rex extinct')
        print('Megatron Wins!!')
        
