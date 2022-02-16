
# Boxing match for lightweight supremacy between the top fighters at 135 and the lneal champion game between <player> and <kambosos>.
# Play games in two steps:
#1. Player chooses to act as one of the boxers: Loma, Haney, Garcia, Davis
# 2. Fight between <boxer> and <kambosos>




# Assign variables to boxers
loma = "Lomachenko"
haney = "Haney"
garcia = "Garcia"
davis = "Davis"
# Assign Fighter health
loma_hp = 120
haney_hp = 80
garcia_hp = 70
davis_hp= 90

# Fighter punching power
loma_pwr = 250
haney_pwr = 180
garcia_pwr = 270
davis_pwr = 280

# Kambosos stats
kamb_pwr = 230
kamb_hp = 260

# task 2 Prompt for player's choice of fighter
a = 'abcd'
while True:
    # f-string , preformatted string
    userinput = input(
        f"""
choose your fighter:
1) {loma}
2) {haney}
3) {garcia}
4) {davis}

Select (1,2,3,4): """
    )

    # deal with special cases first
    if userinput not in('1','2','3','4'):
        print("unkown fighter", userinput)
        continue
    # initialize 'player'
    if userinput == '1':
        my_boxer = loma
        my_hp = loma_hp
        my_pwr = loma_pwr

    elif userinput == '2':
        my_boxer = haney
        my_hp = haney_hp
        my_pwr = haney_pwr

    elif userinput == '3':
        my_boxer = garcia
        my_hp = garcia_hp
        my_pwr = garcia_pwr

    elif userinput == '4':
        my_boxer = davis
        my_hp = davis_hp
        my_pwr = davis_pwr

    break

print(f'You have chosen: {my_boxer}(health: {my_hp}, power:{my_pwr})')

# Ding ding ding
print("Touch em up.....Blue corner are you ready? Red corner, are you ready? Box!!")
while True:
    # Boxer punches Kambosos
    kamb_hp = kamb_hp - my_pwr
    print(my_boxer, "lands a huge punch on Kambosos!")
    print("Ferocious' looks to be:", kamb_hp)
    if kamb_hp <= 0:
        print("Kambosos cannot continue!")
        print(my_boxer, "is the new lightweight champion!")
        break

    # kambosos punches my_boxer
    my_hp =  my_hp - kamb_pwr
    print("Kambosos lands a huge overhand right", my_boxer)
    print(f"{my_boxer} looks to be at {my_hp}")
    if my_hp <= 0:
        print(f'{my_boxer} has lost the fight')
        print('Kambosos retains his lightweight championship!')
        continue
