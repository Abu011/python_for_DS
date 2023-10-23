noor_age=input("What is your age? ")
noor_age = int(noor_age)
required_age_at_school = 5

#question: Noor can join the school?

if noor_age==required_age_at_school:
    print("you can join the school")
    #we can use multiple elif statements Such as
elif noor_age>required_age_at_school:
    print("you should join the secondary school")
elif noor_age<=2:
    print("you should take care of your child bcoz he is still young")    
else:
    print("You cannot join the school") 
