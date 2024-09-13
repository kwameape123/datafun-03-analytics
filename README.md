# datafun-03-analytics
## Process
```
1. Created datafun-03-analytics repository on GitHub.
2. Executed a git clone command in git bash to clone the above metioned repository.
3. Opened datafun-03-analytics in VS Code.
4. Create a virtual environment for the project.
5. Activate virtual environment for the project.
6.Create text file containing project requirements.
7. install projects depencies using requirements.txt.
8. Created a .gitignore file to list folders that git should not track.
9. Created a README.md file to explain project.
10. Used the powershell terminal in VS Code to git add files to source control, git commit changes with useful messages and git push changes to GitHub.
```
## Process In Code
### Create, Clone and Open Project Repository (Steps 1 - 3)
'''git

gitclone https://github.com/kwameape123/datafun-03-analytics

'''
'''shell

cd Documents
dir
cd datafun-03-analytics
code .

'''
### Create and Activate Virtual Environment (Steps 4-5)
'''shell

py -m venv .venv
.venv/Scripts/Activate

'''
### Create Project Requirement and .gitignore Files. Install Project Dependencies.(Steps 6-9)
'''shell

ni requirments.txt
pip -m install -r requirements.txt
ni .gitignore
ni README.md

'''
### Git Add and Commit.(Step 10)
'''shell

git add .
git commit -m add .gitinore, add process and process cmds to README.md
git push -u origin main

'''


