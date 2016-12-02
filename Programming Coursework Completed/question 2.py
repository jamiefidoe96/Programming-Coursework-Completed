def frac_calc (x):
    five = 0
    for number in range (2,x+1) : 	#O(n)
        while number > 0:	 	#0(n^2)
            if number % 5 == 0:		#0(n^2)
                five +=1		#0(n^2)
                number = number/5	#O(n^2)
            else:			
                break

    return five				#O(1)

					#The Run- Time bounds of this function is 0(n^2)
