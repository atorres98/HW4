import requests
import json



def gitHubAPI(ID):
    #url for accessing user repos
    url = "http://api.github.com/users/" + ID + "/repos"
    repos = requests.get(url)
    userRepos = repos.json()
    # json.loads(repos.content.decode('utf-8'))
    repoList = []
    for repo in userRepos: #collect # of commits for repos in dictionary
        commURL = "https://api.github.com/repos/"+ID+"/"+repo["name"]+"/commits"
        commits = requests.get(commURL)
        comm = json.loads(commits.content.decode('utf-8'))
        
        #display ID, Repo, and Number of Commits
        print("User ID: " + ID + "Repo: " + repo["name"] + " Number of Commits: " + str(len(comm)))
        
        repoList.append((str(repo["name"]), len(comm)))
  
    return repoList

if __name__ == "__main__":
    gitHubAPI("atorres98")
    gitHubAPI("richkempinski")







