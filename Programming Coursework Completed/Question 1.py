# Question 1 Coursework
import random

def shuffle ( hat ):
    table = []									

    while len (hat) != 0:						#0(n)
        randomPosition = random.randint (0, len (hat) -1)		

        randomValue = hat.pop (randomPosition)				#0(n)
        table.append (randomValue)					#0(n)

    return table							#0(n)

test1 = list (range(1,10))

print ("test {}".format(test1))

shuffledHat = shuffle(test1)					#The run time bounds of this  function are 0(n)
print("shuffledArray: {}".format(shuffledHat))
       


#test1 = list (range (1,10) )
#est2 = list (range (1,10 ))

#print( "test: () ".format(test1) )

#shuffled1= shuffle(test1)
#print ("shuffled: ()".format(shuffled1))


#shuffled2= shuffle(test2)
#print ("shuffled: ()".format(shuffled2))
