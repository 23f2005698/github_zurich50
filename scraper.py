import requests
import csv

# Replace 'your_github_token' with your GitHub Personal Access Token
token = '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'
headers = {'Authorization': f'token {token}'}

# API endpoint and search query for users in Zurich with more than 50 followers
url = 'https://api.github.com/search/users?q=location:Zurich+followers:>50'

# Send GET request to GitHub API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200 means success)
if response.status_code == 200:
    users = response.json()['items']
    print(f"Found {len(users)} users in Zurich with over 50 followers.")
    
    # List to store user data
    users_data = []

    # Fetch user details
    for user in users:
        user_details = requests.get(f"https://api.github.com/users/{user['login']}", headers=headers).json()
        
        # Clean company name
        company = user_details.get('company', '')
        if company:
            company = company.strip().lstrip('@').upper()

        # Collect user details
        users_data.append({
            'login': user_details.get('login', ''),
            'name': user_details.get('name', ''),
            'company': company,
            'location': user_details.get('location', ''),
            'email': user_details.get('email', ''),
            'hireable': user_details.get('hireable', ''),
            'bio': user_details.get('bio', ''),
            'public_repos': user_details.get('public_repos', 0),
            'followers': user_details.get('followers', 0),
            'following': user_details.get('following', 0),
            'created_at': user_details.get('created_at', '')
        })

    # Write data to users.csv with utf-8 encoding
    with open('users.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=users_data[0].keys())
        writer.writeheader()
        writer.writerows(users_data)

    print("users.csv file created successfully!")

else:
    print(f"Failed to fetch users: {response.status_code} - {response.text}")
import requests
import csv

# Replace 'your_github_token' with your GitHub Personal Access Token
token = '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'
headers = {'Authorization': f'token {token}'}

# API endpoint and search query for users in Zurich with more than 50 followers
url = 'https://api.github.com/search/users?q=location:Zurich+followers:>50'

# Send GET request to GitHub API to fetch users
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200 means success)
if response.status_code == 200:
    users = response.json()['items']
    print(f"Found {len(users)} users in Zurich with over 50 followers.")
    
    # List to store user data
    users_data = []
    
    # Fetch user details
    for user in users:
        user_details = requests.get(f"https://api.github.com/users/{user['login']}", headers=headers).json()
        
        # Clean company name
        company = user_details.get('company', '')
        if company:
            company = company.strip().lstrip('@').upper()

        # Collect user details
        user_data = {
            'login': user_details.get('login', ''),
            'name': user_details.get('name', ''),
            'company': company,
            'location': user_details.get('location', ''),
            'email': user_details.get('email', ''),
            'hireable': user_details.get('hireable', ''),
            'bio': user_details.get('bio', ''),
            'public_repos': user_details.get('public_repos', 0),
            'followers': user_details.get('followers', 0),
            'following': user_details.get('following', 0),
            'created_at': user_details.get('created_at', '')
        }
        
        users_data.append(user_data)

    # Write data to users.csv with utf-8 encoding
    with open('users.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=users_data[0].keys())
        writer.writeheader()
        writer.writerows(users_data)

    print("users.csv file created successfully!")

    # List to store repositories data
    repositories_data = []

    # Fetch repositories for each user and store them in repositories_data
    for user in users:
        user_details = requests.get(f"https://api.github.com/users/{user['login']}", headers=headers).json()
        
        # Fetch repositories for the user (up to 500 repositories)
        repos_url = user_details['repos_url']
        repos_response = requests.get(repos_url, headers=headers)
        
        if repos_response.status_code == 200:
            repositories = repos_response.json()

            # Loop through repositories and collect data
            # Loop through repositories and collect data
            for repo in repositories[:500]:  # Fetch up to 500 repos
                repositories_data.append({
                    'login': user_details['login'],
                    'full_name': repo.get('full_name', ''),
                    'created_at': repo.get('created_at', ''),
                    'stargazers_count': repo.get('stargazers_count', 0),
                    'watchers_count': repo.get('watchers_count', 0),
                    'language': repo.get('language', ''),
                    'has_projects': repo.get('has_projects', False),
                    'has_wiki': repo.get('has_wiki', False),
                    'license_name': repo.get('license', {}).get('name', '') if repo.get('license') else ''
                })
    # Write repository data to repositories.csv with utf-8 encoding
    with open('repositories.csv', 'w', newline='', encoding='utf-8') as file:
        if repositories_data:  # Check if we have repositories data
            writer = csv.DictWriter(file, fieldnames=repositories_data[0].keys())
            writer.writeheader()
            writer.writerows(repositories_data)
            print("repositories.csv file created successfully!")
        else:
            print("No repositories data found.")

else:
    print(f"Failed to fetch users: {response.status_code} - {response.text}")
