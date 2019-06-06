# Branch

show branches
    git branch  ~  show branches

create a new branch
    git branch foo_branch  ~  create a new branch
    git branch

switch branch
    git checkout foo_branch
    git branch

merge branch (into master)
    git checkout master
    git merge foo_branch
   
local branch --> github
    git checkout foo_branch
    git commit -am 'foo branch contents'
    git push --set-upstream origin foo_branch

remote
    git fetch
    git merge origin/master

    OR:
    git pull


