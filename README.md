# Haiku commit art generator

A haiku is a Japanese poem of seventeen syllables, in three lines of five, seven, and five: 

    An old silent pond...
    A frog jumps into the pond,
    splash! Silence again

This action checks if the latest commit message is a haiku. The commit message is a haiku if the following requirements are met:
1) Consitst of three lines, each line must separated by a dash (-)
2) The first line consits of five syllables
3) The second line consitst of seven syllables
4) The third line consits of five syllables

If the commit message is a haiku the action will take its contents and generate ascii art. The art is then written to a file poetry.md. 
Example format:

```
    _                  _     _       _ _            _   
   / \   _ __     ___ | | __| |  ___(_) | ___ _ __ | |_ 
  / _ \ | '_ \   / _ \| |/ _` | / __| | |/ _ \ '_ \| __|
 / ___ \| | | | | (_) | | (_| | \__ \ | |  __/ | | | |_ 
/_/   \_\_| |_|  \___/|_|\__,_| |___/_|_|\___|_| |_|\__|
                                                        
                       _           _____ _             __                 
 _ __   ___  _ __   __| |         |_   _| |__   ___   / _|_ __ ___   __ _ 
| '_ \ / _ \| '_ \ / _` |  _____    | | | '_ \ / _ \ | |_| '__/ _ \ / _` |
| |_) | (_) | | | | (_| | |_____|   | | | | | |  __/ |  _| | | (_) | (_| |
| .__/ \___/|_| |_|\__,_|           |_| |_| |_|\___| |_| |_|  \___/ \__, |
|_|                                                                 |___/ 
   _                             _       _          _   _          
  (_)_   _ _ __ ___  _ __  ___  (_)_ __ | |_ ___   | |_| |__   ___ 
  | | | | | '_ ` _ \| '_ \/ __| | | '_ \| __/ _ \  | __| '_ \ / _ \
  | | |_| | | | | | | |_) \__ \ | | | | | || (_) | | |_| | | |  __/
 _/ |\__,_|_| |_| |_| .__/|___/ |_|_| |_|\__\___/   \__|_| |_|\___|
|__/                |_|                                            
                       _           ____        _           _     _ 
 _ __   ___  _ __   __| |         / ___| _ __ | | __ _ ___| |__ | |
| '_ \ / _ \| '_ \ / _` |  _____  \___ \| '_ \| |/ _` / __| '_ \| |
| |_) | (_) | | | | (_| | |_____|  ___) | |_) | | (_| \__ \ | | |_|
| .__/ \___/|_| |_|\__,_|         |____/| .__/|_|\__,_|___/_| |_(_)
|_|                                     |_|                        
 ____  _ _                                         _         
/ ___|(_) | ___ _ __   ___ ___    __ _  __ _  __ _(_)_ __    
\___ \| | |/ _ \ '_ \ / __/ _ \  / _` |/ _` |/ _` | | '_ \   
 ___) | | |  __/ | | | (_|  __/ | (_| | (_| | (_| | | | | |_ 
|____/|_|_|\___|_| |_|\___\___|  \__,_|\__, |\__,_|_|_| |_(_)
                                       |___/                 

```

## Getting started
Fork this repository and update the file in `.github\workflows\haiku_art.yml`

```yml
name: Haiku Commit Art Generator
on:
  pull_request
  
jobs: 
 generate_haiku_art:
    runs-on: ubuntu-latest
    permissions:
        contents: write 
        pull-requests: write  

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Generate haiku art
        uses: henriettelienrebnor/Fagdag@main
        env:
          GITHUB_TOKEN: ${{ secrets.github_token }}
          PR_NUMBER: ${{ github.event.number }}
```

The line `uses: henriettelienrebnor/Fagdag@main` means that the workflow is using a custom action from this repository's main branch. Update this to point to your fork of this repository so that it runs the code that you will implement.

When github sees this line of code it looks inside the repository for an `action.yml` file. The `action.yml` file is a metadata file that defines:
- what kind of action it is
- what inputs and outputs it expects
- what environment variables it needs
- and how it should be executed

Our `action.yml` specifies to run the action using our `Dockerfile`. Github will then build and run a docker container based on the `Dockerfile` within this repository. 

## Implementation
We will be writing the code in python, and use [PyGithub](https://pygithub.readthedocs.io/en/stable/index.html#) for managing our Github resources. This is
a Python library to use the Github API v3. 

### Requirements
run `pip install -r requirements.txt`

### github_utils.py
- Implement get_latest_commit_message and commit_and_push
- Use the PyGithub module, reference the documentation for [PullRequest](https://pygithub.readthedocs.io/en/stable/examples/PullRequest.html) and [Repository](https://pygithub.readthedocs.io/en/stable/examples/Repository.html)

### haiku_checker.py
- Implement the functions in haiku_checker.py
- Run haiku_test.py to verify that the functions works as expected. 
- **Note**: The tests only check english words, not expected that it should work in other languages as well. 

### main.py
- Follow the steps in the TODO list at the end of main.py

## Testing
To run the action open a new pull request and change the following step in the workflow:

```
      - name: Generate haiku art
        uses: <YOUR_FORK>@<PR_BRANCH_NAME>
```
Changing this step to point to the current PR will allow you to see changes in the behaviour of the action immediatly when you push new code to the open PR.

## Useful links
- [Creating a docker container action](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)
- [actions.yml](https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)
- [github actionc context](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)
