def efficientJanitor(weights_of_bags):
    trips = 1
    total_weight = 0
    for weight in weights_of_bags:
        if 1.01 <= weight <= 3.00:  # checking constraint for weight of bag
            total_weight += weight
            if total_weight > 3.0:   # resetting total weight to current weight if it goes over 3.00
                total_weight = weight
                trips += 1

            elif total_weight == 3.0:  # resetting total weight to 0 if it exactly equals 3.00
                total_weight = 0
                trips += 1
        else:
            return "Invalid weight"

    return trips


number_of_bags = int(input("Enter the number of plastic bags: "))  # checking the constraint for number of bags
if 1001 > number_of_bags > 0:
    # list comprehension for formatting the values to float from string in accordance to the number of bags
    weights = list(float(num) for num in input("Enter the weights of bags separated by space: ").strip().split())[
              :number_of_bags]
    weights.sort()
    print(efficientJanitor(weights))
else:
    print("Choose a lower sample size and run the program again")
