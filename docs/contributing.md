# Contributing
If you wish to contribute to the Edge-Carolina repository, please fork the repository and make changes there. This keeps the main repository clean for official use.

## Forking The Repository

1. Navigate to the Edge-Carolina repository on GitHub
2. Click on the 'Fork' button in the top right corner to fork the repo to your own GitHub account. This creates a copy of the repository in your account.

## Cloning Your Fork Locally
1. On your forked copy, click on the 'Code' button to view the clone URL
2. Copy the HTTPS or SSH clone URL
3. Type git clone <clone-url> into your terminal to clone your forked repository

```git clone https://github.com/YOUR-USERNAME/Edge-Carolina.git```

This will create a local copy of the repository to work on.

## Syncing Your Fork
1. Add the upstream repository as a remote to keep your local copy in sync

```git remote add upstream https://github.com/WestonVoglesonger/Edge-Carolina.git```

2. Fetch the latest changes from upstream to your local machine

```git fetch upstream```

3. Ensure you don't have any local changes and merge the upstream branch

```git checkout main```
```git merge upstream/main```

## Finishing up
Once you have completed these steps you are free to push and pull from your repository!