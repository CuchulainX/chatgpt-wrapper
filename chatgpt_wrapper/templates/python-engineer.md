I have a list of github urls. I would like to fetch a short summary of what the repo is about and the last update made to it. How can I do this in Python. Please provide the source code.

1. Revised prompt:
Provide Python source code to fetch a short summary and the last update date for a list of GitHub repositories.
                                                                                                               
2. Suggestions:                                                                                                
- Use the GitHub API to fetch repository information.
- Process the JSON response to extract the repository description and last update date.
- Iterate through the list of GitHub URLs and apply the above steps for each repository.

3. Questions:
- Are you looking for a standalone Python script, or a function that can be integrated into an existing project?
- Do you have a personal access token for the GitHub API, or would you prefer to use the unauthenticated rate-limited requests?

Based on your input, I have provided an example Python script that demonstrates how to achieve your goal using the GitHub API:

```python
import requests
import json

def fetch_repo_info(github_urls):
    repo_info = []
    base_url = "https://api.github.com/repos/"

    for url in github_urls:
        user_and_repo = url.split("github.com/")[1]
        api_url = base_url + user_and_repo
        response = requests.get(api_url)

        if response.status_code == 200:
            data = json.loads(response.text)
            repo_info.append({
                "url": url,
                "description": data["description"],
                "last_updated": data["updated_at"]
            })
        else:
            print(f"Error fetching data for {url}: {response.status_code}")

    return repo_info

# Replace this list with your GitHub URLs
github_urls = [
    "https://github.com/user/repo1",
    "https://github.com/user/repo2"
]


```

Please note that this script utilizes the unauthenticated GitHub API, which has a rate limit of 60 requests per hour. If you need a higher rate limit, you should use a personal access token for authentication.

