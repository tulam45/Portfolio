# Data from bug closed & frequency review
bugs_closed = [278, 909, 337, 124, 75]
total_reviews = [1545, 3920, 1728, 738, 202]
reviewer_count = [49, 74, 41, 25, 13] 
review_depths = [1.77, 0.99, 1.07, 0.65, 0.35]

# Initialize counters
count_greater = 0
count_less = 0
m = len(total_reviews)  # Size of first sample
n = len(bugs_closed)  # Size of second sample
m2 = len(reviewer_count) # Size of third sample
m3 = len(review_depths) # Size of fourth sample

# Compare each pair
for x in bugs_closed:
    for y in total_reviews:
        if x > y:
            count_greater += 1
        elif x < y:
            count_less += 1

# Calculate Cliff's Delta for review frequency
delta = (count_greater - count_less) / (m * n)

# Calculate Cliff's Delta for reviewer count
count_greater = 0
count_less = 0
for x in bugs_closed:
    for y in reviewer_count:
        if x > y:
            count_greater += 1
        elif x < y:
            count_less += 1
delta2 = (count_greater - count_less) / (m2 * n)

# Calculate Cliff's Delta for review depth
count_greater = 0
count_less = 0
for x in bugs_closed:
    for y in review_depths:
        if x > y:
            count_greater += 1
        elif x < y:
            count_less += 1
delta3 = (count_greater - count_less) / (m3 * n)

print(f"Cliff's Delta - REVIEW FREQUENCY: {delta}")
print(f"Cliff's Delta - REVIEWER COUNT: {delta2}")
print(f"Cliff's Delta - REVIEW DEPTH: {delta3}")