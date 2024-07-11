import os
import json
import requests
from urllib.parse import quote

# GitHub environment variables
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')
GITHUB_EVENT_PATH = os.getenv('GITHUB_EVENT_PATH')

# Load GitHub pull request event data
with open(GITHUB_EVENT_PATH, 'r') as f:
    event_data = json.load(f)

# Extract necessary information
pr_title = event_data['pull_request']['title']
pr_body = event_data['pull_request']['body']
pr_source_branch = event_data['pull_request']['head']['ref']
pr_target_branch = event_data['pull_request']['base']['ref']
pr_url = event_data['pull_request']['html_url']

# GitLab environment variables
GITLAB_TOKEN = os.getenv('GITLAB_TOKEN')
GITLAB_PROJECT_ID = os.getenv('GITLAB_PROJECT_ID')
GITLAB_API_URL = f'https://gitlab.com/api/v4/projects/{quote(GITLAB_PROJECT_ID)}/merge_requests'

# Create merge request in GitLab
headers = {
    'Private-Token': GITLAB_TOKEN,
    'Content-Type': 'application/json',
}

data = {
    'source_branch': pr_source_branch,
    'target_branch': pr_target_branch,
    'title': pr_title,
    'description': f'{pr_body}\n\nOriginal pull request: {pr_url}',
}

response = requests.post(GITLAB_API_URL, headers=headers, json=data)

if response.status_code == 201:
    print('Merge request created successfully in GitLab.')
else:
    print(f'Failed to create merge request in GitLab: {response.content}')
    response.raise_for_status()
