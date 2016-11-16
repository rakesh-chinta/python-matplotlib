import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

response_dict = r.json()
print("Total respositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Respositories returned: ", len(repo_dicts))

print("\n Selected information about each repository: ")
for repo_dict in repo_dicts:
    print('Name:',repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print('stars:',repo_dict['stargazers_count'])
    print("repository:",repo_dict['html_url'])
    print('created:',repo_dict['created_at'])
    print('updated:',repo_dict['updated_at'])
    print('Description:',repo_dict['description'])

    

