from github import PullRequest, InputGitAuthor, Repository

def get_latest_commit_message(pull_request : PullRequest) -> list[str]:
    commit_message = []
    for commit in pull_request.get_commits():
        commit_message.append(commit.get_message())
    return commit_message[-1]
    #raise NotImplementedError("TODO")

def commit_and_push(repo: Repository, target_branch:str, file_path: str) -> None:
    author = InputGitAuthor(
    "GitHub Action",
    "action@github.com")
    remote_file = repo.get_contents(file_path, ref=target_branch)
    with open(file_path) as f: 
        new_file_content = f.read()
    
    commit_message = 'New haiku'
    repo.update_file(
        remote_file, 
        commit_message,
        new_file_content,
        remote_file.sha,
        branch = target_branch,
        author=author
    )



    ##TODO use update_file from github.Repository to push the new file contents to the open PR 
