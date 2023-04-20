import sys
import random
import statistics

orig_stdout = sys.stdout
f = open('random_health_data.csv', 'w')
sys.stdout = f

print("age,height,weight")

ages = []
heights = []
weights = []

for i in range(0, 2500):
    age = random.randint(18, 75)
    ages.append(age)
    height = random.randint(58,82)
    heights.append(height)
    weight = random.randint(100,300)
    weights.append(weight)
    print(f"{age},{height},{weight}")

sys.stdout = orig_stdout
f.close()

print("Mean")
print(f"Age: {sum(ages)/len(ages)}")
print(f"Height: {sum(heights)/len(heights)}")
print(f"Weight: {sum(weights)/len(weights)}")
print("Sum")
print(f"Age: {sum(ages)}")
print(f"Height: {sum(heights)}")
print(f"Weights: {sum(weights)}")
print("Median")
print(f"Age: {statistics.median(ages)}")
print(f"Height: {statistics.median(heights)}")
print(f"Weight: {statistics.median(weights)}")
print("Min")
print(f"Age: {min(ages)}")
print(f"Heights: {min(heights)}")
print(f"Age: {min(weights)}")
print("Max")
print(f"Age: {max(ages)}")
print(f"Heights: {max(heights)}")
print(f"Age: {max(weights)}")
print("Standard Deviation")
print(f"Age: {statistics.stdev(ages)}")
print(f"Heights: {statistics.stdev(heights)}")
print(f"Age: {statistics.stdev(weights)}")
print("Variance")
print(f"Age: {statistics.variance(ages)}")
print(f"Heights: {statistics.variance(heights)}")
print(f"Age: {statistics.variance(weights)}")