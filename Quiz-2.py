import sys
// Point Calculator
try:
    number_of_two_point_score=int(sys.argv[1])
    number_of_three_point_score=int(sys.argv[2])
    number_of_one_point_score=int(sys.argv[3])
    total_score=((number_of_two_point_score)*2)+((number_of_three_point_score)*3)+((number_of_one_point_score)*1)
    print(total_score)
except IndexError:
    pass


//BMI Calculator


def healthStatus(height,mass):
    height=float(height)
    mass=float(mass)
    if mass <=0:
        return("Please enter a number which higher than 0")
    elif height<=0:
         return("Please enter a number which higher than 0")
    else:
        BMI=mass/(height**2)
        if BMI >= 30:
            return("You are obese:")
        elif BMI>=24.9:
            return("You are overweight")
        elif BMI>=18.5:
            return("You are healty")
        else:
            return("You are underweight")    
    
