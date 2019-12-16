##**12.10编写教程记录**
###git本地配置：
####        git config user.name "用户名" --global
####        git config user.email "邮箱"  --global
####        ssh-keygen -t rsa -C "xxx@xxx.com" 
####        验证是否成功：ssh -T git@github.com
配置全局的用户名和邮箱，后续提交操作会显示备注信息，跟踪谁是提交和修改者
global应用于当前用户，local作用于某一个仓库，system作用于电脑所有用户
####git config --list --local(查看当前作用域配置项)
###基本流程：
####        git init  （初始化仓库）
####        git status  （查看仓库状态）
####        git add test.txt （将文件加入缓存区）
####        git commit -m "修改信息1"   （提交修改到本地仓库并备注修改信息）
####        git log （查看日志记录）
###提交修改：
####       git add -u (多个文件，只提交跟踪过的文件)
####       git add --all   git add (都是提交全部文件)
####       git add -p    （交互式修改提交）
###提交：
####        git commit -m  (将工作区的修改提交到仓库)
####        git commit -a -m (合并了add的操作)
###git diff：
####        git diff(查看工作区和暂存区的区别)
####        git diff --ached (查看暂存区和上一个提交的区别)
####        git diff HEAD（工作区和上一次提交的区别）
####        git diff <id1> <id2>  (两次提交的区别) 
###git log：
####        git log （查看全部提交）
####        git log -<number> (查看最近n次提交)
####        git log -p(展示每次提交的log和每次的改动)
####        git --start（展示每次提交的log和每次改动的简要统计）
####        git --online（展示一行简略信息）
####        git --graph（简单的图形展示）
###git show：
####        git show（展示上一次提交）
####        git show <commit-id>(展示某一次提交)
####        git show --name-only<commit-id>(展示特定提交修改的文件名)
###文件删除git rm：
####        git rm <file-name>（从工作区删除，并从仓库移除对其的跟踪）
####        git rm --cached<file-name >(只移除跟踪，保留工作区文件)
###git clean:
####        git clean(删除所有未被跟踪的文件)
####        git clean -n(打印出将会删除的文件名，不会执行删除操作)
##*撤销工作区修改：
####        git checkout <filename> （撤销一个文件）
####        git checkout . (撤销所有文件)
####        git checkout<commit-id><file-name>(恢复某个commit的指定文件到暂存区和工作区)
##*撤销暂存区修改：
####        git reset HEAD <file-name> (撤销暂存区的修改，回退到工作区)
####        git rest <commit-id> （回退到某一次提交的状态）
####        git reflog （打印最近操作所对应的commit id）

##分支**重要
###HEAD指针，指向当前仓库的版本，master 和 HEAD 都是指针，master始终指向当前分支的最新提交节点，HEAD是当前仓库版本，可以随意移动到不同节点
###查看分支：
####       git branch(列出所有分支)
####       git branch -r（列出所有远程分支）
####       git branch -a（列出本地和远程分支）
####       git branch -v（查看分支详细信息）
###新建&切换&删除分支：
####        git branch <branch name>
####        git checkout -b<branch name>(新建并切换分支)
####        git checkout <branch name>（切换分支）
####        git checkout -  （切换到上一个分支）
####        git branch -d  (删除已经合并的分支)
####        git branch -D （删除分支不论是否合并）
###分支合并：
####        git merge <branch_name>  (合并目标分支到当前分支)
###git cherry-pick（把弄错分支的提交移动到正确的地方；把其他分支的提交添加到现在的分支）:
#####        git cherry-pick<commit-id> (指定一个commit合并到当前分支)
#####        git cherry-pick<branch-name>(挑选指定的分支的最新提交)
#####        git cherry-pick<start-commit-id>...<end-commit-id>(挑选连续多个提交，左开右闭)
#####        git cherry-pick<start-commit-id>^...<end-commit-id>(左闭右闭)
###打上Tag：
####        git tag（查看所有tag）
####        git tag -l <tag-name> (筛选相应的tag)
####        git show <tag-name>  (查看指定tag)
####        git tag --point-at <commit-id>  (查看指定commit上的所有tag)
####        git show-ref --tags （查看所有tag和对应的commit）
####        git tag <tag-name>  (新建tag)
####        git tag <tag-name> <commit-id>(在指定的commit新建tag)
####        git tag -a <tag-name> -m <message> (添加一个tag和message)
####        git tag -d <tag-name> (删除tag)

###紧急加塞，使用stash
####        git stash  (将工作区和暂存区的所有修改暂存起来，工作区和暂存区上次提交一致)
####        git stash apply (取出最近的暂存)
####        git stash pop（取出暂存，并删除暂存记录）
####        git stash drop  （删除暂存）

###变基（rebase）（改变历史提交；合并分支）
####        git rebase <barnch-name> (合并分支的作用)

##*远程仓库操作
####克隆&管理远程仓库： git clone <url> <new-name>   (拉取代码，命名本地仓库)
####        git remote add <remote-name> <remote-url>  （添加远程仓库）
####        git remote -v(查看远端仓库信息)
####        git remote remove <remote-name> （删除远端仓库）
####        git remote rename <old-name> <new-name> (重命名远程仓库名字) 

###推送和更新
####        git push <remote-name>  <branch-name>  (推送分支到指定的远程仓库，第一次推送需要 -u)
####        git push <remote-name>  <tag-name> (推送tag到远程仓库)
####        git fetch（拉取更新）
####        git pull（获取远端更新，合并到本地分支）
####        git pull --rebase （使用rebase方式拉取更新）