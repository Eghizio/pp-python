the_truth = ("Mleko", "Płatki")

# Accessing Tuple elements
print(the_truth)
print("Najpierw ", the_truth[0])
print("Potem ", the_truth[1])



# Ooopsie, no changing values
# the_truth[0] = "Płatki"
# the_truth[1] = "Mleko"


# Ooopsie, no adding new elements
# the_truth[2] = "Cukier"



try:
    the_truth[0] = "Płatki"
    the_truth[1] = "Mleko"
    
    the_truth.__add__("Cukier")
except:
    print("Tuples are Immutable - they cannot change")



# Comparing Tuples
first = (3, 2, 1)
second = (3, 2, 1)

print("\nAre the Tuples the same (equals)?:\n", first == second)
print("\nAre the Tuples the same (is)?:\n", first is second)
