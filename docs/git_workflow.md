# Git workflow and guidelines

## Branches
The run control git repo has these branches:
- **main**: Should be a stable version, fully tested. Should have a version number.
- **develop**: Development branch. When we are not taking data, the distinction between main and develop is probably not as important. When we are taking data, we want to keep track of any changes in run control with a version number, documentation and changelog, etc. And those things should be updated when merging from develop into main.
- **feature/xxx**, **bugfix/xxx**: separate branches for each feature we want to add, or bug fix. If there are multiple smaller fixes or changes, it’s probably fine to combine them in a single branch. If someone is working on multiple features at the same time, there can be multiple branches. If multiple people are working on the same feature, then they should probably share the same branch.

## Workflow
1. When starting to work on a new feature or a bugfix, create a new branch named `feature/xxx` or `bugfix/xxx` based on the latest develop branch. 
    ```
    git fetch
    git checkout -b feature/xxx develop
    ```
2. Make the changes in the branch. Feel free to commit as often as you like. 
3. *(Optional)* Create a pull request  on github from feature branch to develop branch. Document what’s done in this change. Code review and approvals happen here.
4. After this feature is done, merge into develop branch
    - *(Recommended)* Rebase from the develop branch again, to get any new commits there. Now the new commits in the feature branch should be after all of the commits in the develop branch. Merge the new commits into the develop branch.
        ```
        git fetch
        git rebase origin/develop
        git switch develop
        git pull
        git merge feature/xxx
        git push
        ```
    - Or if you like to have a separate merge commit available, merge without rebase.
        ```
        git fetch
        git switch develop
        git merge feature/xxx
        ```
    - Or if you don’t care about the commit history, can squash all the changes into one commit in the develop branch.
        ```
        git fetch
        git switch develop
        git merge –squash feature/xxx
        git commit
        ```
5. Then, the feature or bug fix branch can be safely deleted, both locally and on github.
    ```
    git branch -d feature/xxx
    git push origin --delete feature/xxx
    ```
6. When the develop branch is stable enough, it can be merged into the main branch. Then we can generate a release with a version number, update documentation, etc.
