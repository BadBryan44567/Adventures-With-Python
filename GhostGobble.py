def EatGhost(ifPowerPalleteActive, ifTouchingGhost):
	return True if ifPowerPalleteActive == True and ifTouchingGhost == True else False
	
def Score(ifTouchingPowerPallete, ifTouchingDot):
	return True if ifTouchingDot == True or ifTouchingPowerPallete == True else False

def Lose(ifPowerPalleteActive, ifTouchingGhost):
	return True if ifTouchingGhost == True and ifPowerPalleteActive == False else False

def Win(ifEatenAllDots, ifPowerPalleteActive, ifTouchingGhost):
	return True if ifEatenAllDots == True and Lose(ifPowerPalleteActive, ifTouchingGhost) == False else False

print(EatGhost(False, True))
print(Score(True, True))
print(Lose(False, True))
print(Win(False, True, False))