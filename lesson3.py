#********************************************************************
# lesson3.py sisältää Minecraft Education maailman PYTHON 101 WITH MAKECODE- LESSON 3 ratkaisukoodit
# @author: Timo Kuukka
# @since: 9.5.2023
# @version: 1.0
# change: original
#******************************************************************** 

# Activity 1 solution
#--------------------

a = "berries"
b = "melon"
c = "apple"
d = a
fruit = a
player.say(fruit)
fruit = c
player.say(fruit)
fruit = b
player.say(fruit)
fruit = d
player.say(fruit)


# Activity 2 solution
#--------------------

location1 = world(-24, 40, -18)
location2 = world(-31, 40, -11)
location3 = world(-28, 40, -16)
location4 = world(-25, 40, -13)
location5 = world(-31, 40, -17)
# Replace the lines below with your code #
# place block at location1 command
blocks.place(MELON_BLOCK, location1)
# place block at location2 command
blocks.place(MELON_BLOCK, location2)
# place block at location3 command
blocks.place(PUMPKIN, location3)
# place block at location4 command
blocks.place(PUMPKIN, location4)
# place block at location5 command
blocks.place(MELON_BLOCK, location5)


# Activity 3 solution
#--------------------

# STEP 1
apple = 10
melon = 15
berries = 20
potato = 2
# Replace the lines below with your code #
cost = apple + melon + (berries * 2) + potato
player.say(cost)
# Aja koodi ja paina pelissä numeroa 67

# STEP 2
apple = 10
melon = 15
berries = 20
potato = 2
pumpkin = 10
# Replace the lines below with your code #
cost = apple + melon + (berries * 2) + potato + pumpkin
player.say(cost)
# Aja koodi ja paina pelissä numeroa 77

# STEP 3
apple = 12
melon = 12
berries = 20
potato = 2
pumpkin = 10
# Replace the lines below with your code #
cost = apple + melon + (berries * 2) + potato + pumpkin
player.say(cost)
# Aja koodi ja paina pelissä numeroa 76