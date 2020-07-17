angry = 1
bored = 1
hungry = 1
tired = 0

#If T-Rex is angry, hungry, and bored he will eat the Triceratops.
if angry and bored and hungry:
    print("T-Rex will eat Triceratops")
#Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
elif tired and hungry:
  print("T-Rex will eat Iguanadon")
#Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
elif bored and hungry:
  print("T-Rex will eat Stegasaurus")
#Otherwise if T-Rex is tired, he goes to sleep.
elif tired:
  print("T-Rex goes to sleep")
#Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
elif angry and bored:
  print("T-Rex fights Velociraptor")
#Otherwise if T-Rex is angry or bored, he roars.
elif angry or bored:
  print("T-Rex roars")
#Otherwise T-Rex gives a toothy smile.
else:
  print("T-Rex smiles")