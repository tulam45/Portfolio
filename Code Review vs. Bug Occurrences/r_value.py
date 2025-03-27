def calc_r_value (x_value, y_value, x_average, y_average):
    # Calculate the necessary sums for Pearson's correlation formula
    n = len(x_value)

    sum_xy = 0
    for i in range(n):
        sum_xy += (x_value[i] - x_average[i]) * (y_value[i] - y_average[i])

    sum_x2 = 0
    for i in range(n):
        sum_x2 += (x_value[i] - x_average[i]) ** 2

    sum_y2 = 0
    for i in range(n):
        sum_y2 += (y_value[i] - y_average[i]) ** 2

    # Calculate Pearson correlation coefficient (r)
    r = sum_xy / ((sum_x2 * sum_y2) ** 0.5)

    return r

# Data for bugs closed, total reviews, and review depth
bugs_closed = [278, 909, 337, 124, 75]  # Total is 1723
total_reviews = [1545, 3920, 1728, 738, 202]    # Total is 8133
reviewer_count = [49, 74, 41, 25, 13]   # Total is 202 
bugs_mean = [(278.0/1723.0), (909.0/1723.0), (337.0 / 1723.0), (124.0 / 1723.0), (75.0 / 1723.0)]
total_reviews_mean = [(1545.0/8133.0), (3920.0/8133.0), (1728.0/8133.0), (738.0/8133.0), (202.0/8133.0)]
reviewer_count_mean = [(49.0/202.0), (74.0/202.0), (41.0/202.0), (25.0/202.0), (13.0/202.0)]
# This is in data of review depth is in percentage
review_depths = [1.77, 0.99, 1.07, 0.65, 0.35]  # Total is 4.83
review_depths_mean = [1.77/4.83, 0.99/4.83, 1.07/4.83, 0.65/4.83, 0.35/4.83] 

# Calculate the necessary sums for Pearson's correlation formula
sum_x = sum(bugs_closed)
sum_y = sum(total_reviews)
sum_z = sum(review_depths)
sum_x2 = sum(x**2 for x in bugs_closed)
sum_y2 = sum(y**2 for y in total_reviews)
sum_z2 = sum(y**2 for y in review_depths)
sum_xy = sum(x * y for x, y in zip(bugs_closed, total_reviews))
sum_xy2 = sum(x * y for x, y in zip(bugs_closed, review_depths))
sum_x3 = sum(x * y for x, y in zip(total_reviews, review_depths))

# alt_sum_x = 0
# alt_calc_review_r = 0


# for i in range(5):
#     alt_calc_review_r += (bugs_mean[i] - total_reviews_mean[i]) * (bugs_mean[i] - reviewer_count_mean[i])

# alt_sum_y = 0
# for i in range(5):
#     alt_sum_y += (total_reviews_mean[i] - reviewer_count_mean[i]) ** 2

# Number of data points
n = len(bugs_closed)

# Calculate Pearson correlation coefficient (r)
r = (n * sum_xy - sum_x * sum_y) / ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5
r2 = (n * sum_xy2 - sum_x * sum_z) / ((n * sum_x2 - sum_x ** 2) * (n * sum_z2 - sum_z ** 2)) ** 0.5

# Output the result
print("Pearson correlation coefficient (r): REVIEW FREQUENCY - ", r)
print("Pearson correlation coefficient (r): REVIEWER DEPTH - ", r2)

# Might use these values instead
alt_r = calc_r_value(bugs_closed, total_reviews, bugs_mean, total_reviews_mean)
print("Alt Pearson correlation coefficient (r): REVIEW FREQUENCY - ", alt_r)

alt_r_review_depth = calc_r_value(bugs_closed, review_depths, bugs_mean, review_depths_mean)
print("Alt Pearson correlation coefficient (r): REVIEWER DEPTH - ", alt_r_review_depth)

alt_r_reviewer_count = calc_r_value(bugs_closed, reviewer_count, bugs_mean, reviewer_count_mean)
print("Alt Pearson correlation coefficient (r): REVIEWER COUNT - ", alt_r_reviewer_count)
