import http.client
import json
from datetime import datetime
from collections import Counter

# Define the date range (NEED INPUT HERE)
start_date = datetime(2017, 11, 9)  # Start date (inclusive)
end_date = datetime(2021, 3, 24)    # End date (inclusive)

# Set up the connection to GitHub API
conn = http.client.HTTPSConnection("api.github.com")

# Define the repository you want to fetch PRs from
owner = 'samvera'  # Replace with the repo owner
repo = 'hyrax'     # Replace with the repo name

# Define the GitHub API URL for fetching PRs
url = f"/repos/{owner}/{repo}/pulls?state=all&sort=created&direction=asc"

# Add the required headers
headers = {
    'User-Agent': 'python-script',
    'Authorization': 'token VALUE_TOKEN_GOES_HERE'  # Replace with your token
}

# Function to fetch all pull requests
def fetch_prs():
    prs = []
    page = 1
    while True:
        # Make the GET request for PRs with pagination
        conn.request("GET", f"{url}&page={page}", headers=headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")

        if response.status == 200:
            pr_data = json.loads(data)
            if not pr_data:  # If no more PRs are returned, exit the loop
                break
            prs.extend(pr_data)
            page += 1
        else:
            print(f"Failed to fetch PRs. HTTP Status Code: {response.status}")
            break
    return prs

# Function to fetch reviews for a PR
def fetch_reviews(pr_number):
    reviews = []
    url = f"/repos/{owner}/{repo}/pulls/{pr_number}/reviews"
    conn.request("GET", url, headers=headers)
    response = conn.getresponse()
    data = response.read().decode("utf-8")

    if response.status == 200:
        reviews = json.loads(data)
    else:
        print(f"Failed to fetch reviews for PR #{pr_number}. HTTP Status Code: {response.status}")
    return reviews

# Function to count reviewers' frequency
def count_reviewer_frequency(prs):
    reviewer_counter = Counter()

    for pr in prs:
        # Check if the PR was created within the specified date range
        created_at = datetime.fromisoformat(pr['created_at'].rstrip('Z'))
        if start_date <= created_at <= end_date:
            # Fetch the reviews for the PR
            pr_number = pr['number']
            reviews = fetch_reviews(pr_number)

            # Loop through the reviews and count each reviewer
            for review in reviews:
                if review['user']:  # Ensure the user field exists and is not None
                    reviewer = review['user']['login']
                    reviewer_counter[reviewer] += 1

    return reviewer_counter

# Fetch all PRs created within the time period
prs = fetch_prs()

# Count the reviewer frequency for the fetched PRs
reviewer_frequency = count_reviewer_frequency(prs)

# Print the reviewer frequency
print("Reviewer Frequency:")
for reviewer, count in reviewer_frequency.items():
    print(f"{reviewer}: {count} review(s)")

# Close the connection
conn.close()

