#this is a test
import random
import time

def displayIntro():
	print('''On s'en tape complètement de ce qu'il devrait y avoir ici''')
	print()

def chooseCave():
	cave =''
	while cave != '1' and cave != '2':
		print ('Dans quelle cave ? (1 ou 2)')
		cave = input()

	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	time.sleep(2)
	print('il fait noir...')
	time.sleep(2)
	print('un gros dragon ouvre la gueule et...')
	print()
	time.sleep(2)

	friendlyCave = random.randint(1,2)

	if chosenCave == str(friendlyCave):
		print(" vous donne un bisous.")
	else:
		print("vous bouffe tout cru.")

playAgain ='yes'
while playAgain =='yes' or playAgain =='y':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)

	print("Essayer encore (yes ou no)")
	playAgain = input().lower()

