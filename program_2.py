def average_age():
    # Get User Input
    age1 = float(input("Enter 1st person age: "))
    age2 = float(input("Enter 2nd persons age: "))
    age3 = float(input("Enter 3nd persons age: "))
    age4 = float(input("Enter 4nd persons age: "))
    age5 = float(input("Enter 5nd persons age: "))
    
    # Sum ages
    results = (age1 + age2 + age3 + age4 + age5)
    # Average the ages
    results_f = (results / 5)
    # Print the results
    print("the result is:", results_f)
# Line which calls the above function.
average_age() 
