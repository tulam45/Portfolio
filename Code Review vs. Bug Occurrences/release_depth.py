import sys
import http.client
import json
from datetime import datetime

# GitHub API details
OWNER = 'samvera'
REPO = 'hyrax'

# Set up the connection to GitHub API
conn = http.client.HTTPSConnection("api.github.com")

# Add a 'User-Agent' header to the request
headers = {
    'User-Agent': 'python-script',
    'Authorization': 'token VALUE_TOKEN_GOES_HERE'  # Replace with your token
}

# Hardcoded start and end dates (NEED INPUT HERE)
start_date = datetime(2021, 3, 24)  # Start date (inclusive)
end_date = datetime(2023, 5, 30)    # End date (inclusive)

# Fetch pull requests created within a specific time range
def get_pull_requests_in_time_range(start_date, end_date):
    url_prs = f"/repos/{OWNER}/{REPO}/pulls?state=closed&sort=created&direction=asc"
    pulls = []
    page = 1
    while True:
        conn.request("GET", f"{url_prs}&page={page}", headers=headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")

        if response.status == 200:
            pr_data = json.loads(data)
            if not pr_data:
                break
            for pr in pr_data:
                created_at = datetime.fromisoformat(pr['created_at'].rstrip('Z'))
                merged_at = pr.get('merged_at')

                # Log the created_at and merged_at for debugging purposes
                print(f"PR #{pr['number']} created at: {created_at}, merged at: {merged_at}")

                # Check if PR's creation or merge date is within the specified time range
                if start_date <= created_at <= end_date or (merged_at and start_date <= datetime.fromisoformat(merged_at.rstrip('Z')) <= end_date):
                    pulls.append(pr)

            page += 1
        else:
            break

    return pulls

# Fetch reviews for a PR
def get_reviews_for_pr(pr_number):
    url_reviews = f"/repos/{OWNER}/{REPO}/pulls/{pr_number}/reviews"
    conn.request("GET", url_reviews, headers=headers)
    response = conn.getresponse()
    data = response.read().decode("utf-8")

    if response.status == 200:
        return json.loads(data)
    else:
        return []

# Fetch comments for a PR
def get_comments_for_pr(pr_number):
    url_comments = f"/repos/{OWNER}/{REPO}/issues/{pr_number}/comments"
    conn.request("GET", url_comments, headers=headers)
    response = conn.getresponse()
    data = response.read().decode("utf-8")

    if response.status == 200:
        return json.loads(data)
    else:
        return []

# Calculate review depth
def calculate_review_depth(pulls):
    total_comments = 0
    total_commits = 0

    for pr in pulls:
        pr_number = pr['number']

        # Get reviews and comments for the PR
        reviews = get_reviews_for_pr(pr_number)
        comments = get_comments_for_pr(pr_number)

        # Count the reviews and comments
        total_comments += len(reviews) + len(comments)

        # Get the number of commits for the PR
        commits_url = pr['_links']['commits']['href']
        conn.request("GET", commits_url, headers=headers)
        response = conn.getresponse()
        commits_data = response.read().decode("utf-8")

        if response.status == 200:
            commits = json.loads(commits_data)
            total_commits += len(commits)

    # Calculate review depth
    if total_commits > 0:
        return total_comments / total_commits
    else:
        return 0

# Main function to fetch PRs within a time frame and calculate review depth
def main():
    # Get the pull requests within the hardcoded time frame
    pulls = get_pull_requests_in_time_range(start_date, end_date)

    if not pulls:
        print(f"No pull requests found within the time frame {start_date} to {end_date}.")
        return

    # Calculate review depth for the pull requests in this time frame
    review_depth = calculate_review_depth(pulls)
    print(f"Review Depth from {start_date} to {end_date}: {review_depth:.5f}")

if __name__ == "__main__":
    main()