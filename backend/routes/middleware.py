import subprocess

# Function to execute shell commands
def run_command(command):
    try:
        # Run the command
        result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
        # If there's any error, print it but don't raise an exception
        if result.stderr:
            print("Error:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the command:", e)

# Function to add all files to the staging area
def git_add():
    run_command(["git", "add", "."])

# Function to commit changes
def git_commit(message):
    run_command(["git", "commit", "-m", message])

# Function to push changes
def git_push(branch_name="main"):
    run_command(["git", "push", "origin", branch_name])

# Example usage:
if __name__ == "__main__":
    commit_message = input("Enter the commit message: ")
    branch_name = input("Enter the branch name to push to (default 'main'): ") or "main"

    # Add all files to the staging area
    git_add()

    # Commit changes
    git_commit(commit_message)

    # Push changes
    git_push(branch_name)

"""
When running the script, you'll be prompted to enter the commit message and the
branch name to push to. If you don't enter a branch name, it will default to main.
The script will add all files to the staging area, commit the changes, and push
them to the specified branch.

Note: If you're using a private repository, you'll need to enter your username
and password to push changes. If you're using a public repository, you can
configure your Git client to cache your credentials so you don't have to enter
them every time.

To do this, run the following command in your terminal: 
'git config --global'
'credential.helper cache' 

You can also set a timeout for the cache by running the following command:
'git config --global credential.helper 'cache --timeout=3600'

This will set the cache to timeout after 3600 seconds (1 hour). You can change
the timeout to whatever you want.

If you want to clear the cache, run the following command:
git config --global --unset credential.helper

For more information, see the Git documentation: https://git-scm.com/docs/git-credential-cache

If you're using a public repository, you can also use SSH instead of HTTPS to
avoid having to enter your username and password. For more information, see the
GitHub documentation: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh
"""