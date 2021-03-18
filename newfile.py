
#use good ide to run
#quick rules (you can read my readme file for that contct me at my instagram handle @pygohil_007)
#player and computer have same hp attack value and defence,while any player defende at that instat attack value becomes 400 from 250 and defender get 50 defence point which will help him for further rounds.... anyway i can not explain everything here go play!

import random

class player:
	def __init__(self,player,attack,hp,defence):
		self.player=player
		self.attack=attack
		self.hp=hp
		self.defence=defence
	def dodged_attack(self):
		self.defence=self.defence+50
	def normal_lost(self):
		self.hp=self.hp-250+self.defence
	def power_lost(self):
		self.hp=self.hp-400+self.defence
	def power_attack(self):
		self.attack=self.attack+150

	def status_of_player(self):
		print(str(self.player))
		print('------------------------------')
		print('attack value:'+str(self.attack)+'\n')
		print('hp value:'+str(self.hp)+'\n')
		print('defence value:'+str(self.defence)+'\n')
		
player1=player('player1',250,1000,0)
computer=player('computer',250,1000,0)



def status():
 	print('-----------------------------------------')
 	print(player1.status_of_player())
 	print('------------------------------------------')
 	print(computer.status_of_player())
 	print('--------------------------------------------')
 

status()

def game():
	print('enter your attack:\n')
	print('1:water')
	print('2:grass')
	print('3:fire')
	print('4:dodge')
	
game()
player1_select=int(input())
co_select=random.randint(1,4)

	

while player1.hp > 0 and computer.hp > 0:
	  if player1_select==co_select:
	  	print('tie')
	  	status()
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==1 and co_select==2:
	  	print('you lost this round')
	  	player1.normal_lost()
	  	status()
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==1 and co_select==3:
	  	print('you won this round')
	  	computer.normal_lost()
	  	status()
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==1 and co_select==4:
	  	print('computer dodged')
	  	computer.power_lost()
	  	computer.dodged_attack()
	  	status()
	  	print('additional damaged applied')
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==2 and co_select==1:
	  	print('you won this round!')
	  	computer.normal_lost()
	  	status()
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==2 and co_select==3:
	  	print('you lost this round!')
	  	player.normal_lost()
	  	status()
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==2 and co_select==4:
	  	print('computer dodged')
	  	computer.power_lost()
	  	computer.dodged_attack()
	  	status()
	  	print('additional damage applied')
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==3 and co_select==1:
	  	print('you lost this round')
	  	player1.normal_lost()
	  	status()
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==3 and co_select==2:
	  	print('you won this round')
	  	computer.normal_lost()
	  	status()
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==3 and co_select==4:
	  	print('computer dodged')
	  	computer.power_lost()
	  	computer.dodged_attack()
	  	status()
	  	print('additional damage applied')
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==4 and co_select==1:
	  	print('you dodged')
	  	player1.power_lost()
	  	player1.dodged_attack()
	  	status()
	  	print('additional damage applied')
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==4 and co_select==2:
	  	print('you dodged')
	  	player1.power_lost()
	  	player1.dodged_attack()
	  	status()
	  	print('additional damage applied')
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)
	  elif player1_select==4 and co_select==3:
	  	print('you dodged')
	  	player1.power_lost()
	  	player1.dodged_attack()
	  	status()
	  	game()
	  	print('additional damage applied')
	  	game()
	  	player1_select=int(input())
	  	co_select=random.randint(1,4)		
	  else:
	  	print('enter valid number')
	  	break
	  	
print('game is over!')

if (player1.hp>computer.hp):
	  print('congratulations! warrior you beat opponent\n')

else:
	  print('sorry! you lost this game')
	  
	  
	  
print('game developer : @pygohil__007 contact instagram account')
	  
	  	
	  
	





 	
 	
 
 
 


		
		
			
	
	