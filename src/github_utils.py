from github import PullRequest, InputGitAuthor, Repository

def get_latest_commit_message(pull_request : PullRequest) -> list[str]:
    commit = pull_request.get_commits()[pull_request.commits - 1]
    message = commit.message()
    return(message)

def commit_and_push(repo: Repository, target_branch:str, file_path: str) -> None:
    author = InputGitAuthor(
    "GitHub Action",
    "action@github.com")
    remote_file = repo.get_contents(file_path, ref=target_branch)
    with open(file_path) as f: 
        new_file_content = f.read()

    repo.update_file(remote_file.path, "add art", new_file_content, remote_file.sha, branch = target_branch, author = author)