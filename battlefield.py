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
        print(input('Who would you like to win, Megatron the robot or T-Rex the dinosaur? Enter here: '))
        print("")

    def battle_phase(self):
        team_dino = Dinosaur('T-Rex', 25)
        team_robo = Robot('Megatron')

        team_robo.attack(team_dino)
        print('Megatron attacked T-Rex with a sword for 25 damage!')
        print(f'T-Rex health is now at {team_dino.health}!')
        print('')

        team_dino.attack(team_robo)
        print('T-Rex attacked Megatron for 25 damage!')
        print(f'Megatrons health is now at {team_robo.health}! ')
        print('')

        team_robo.attack(team_dino)
        print('Megatron attacked T-Rex with a sword for 25 damage!')
        print(f'T-Rex health is now at {team_dino.health}!')
        print('')

        team_dino.attack(team_robo)
        print('T-Rex attacked Megatron for 25 damage!')
        print(f'Megatrons health is now at {team_robo.health}!')
        print('')

        team_robo.attack(team_dino)
        print('Megatron attacked T-Rex with a sword for 25 damage!')
        print(f'T-Rex health is now at {team_dino.health}!')
        print('')

        team_dino.attack(team_robo)
        print('T-Rex attacked Megatron for 25 damage!')
        print(f'Megatrons health is now at {team_robo.health}!')
        print('')

        team_robo.attack(team_dino)
        print('Megatron attacked T-Rex with a sword for 25 damage!')
        print(f'T-Rex has {team_dino.health} health remaining!')
        print('')
 
    def display_winner(self):
        print('Megatron made T-Rex extinct')
        print('Megatron Wins!!')
        
