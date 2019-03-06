import sys
import urllib.request as urllib2
import json

def main(userName):
    sindhuRepo = []
    url = "https://api.github.com/users/"+userName+"/repos"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    gitHubRepoJson = response.read()
    gitRepos = json.loads(gitHubRepoJson)
    for repo in gitRepos:
        sindhuRepo.append(repo['name'])
        print(repo['name'])
    response.close()

if __name__ == '__main__':
    args = sys.argv
    main(args[1])
