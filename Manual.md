cd /home/epcc/proj/diabete

python /home/epcc/proj/diabete/analyzer.py

Create .gitignore

git remote add origin git@github.com:jiongjiongli/diabete.git
git remote set-url origin https://github.com/jiongjiongli/diabete.git
git config --global user.name 'jiongjiongli'
git config --global user.email 'jiongjiongai@outlook.com'

git init

git fetch origin
git pull origin master


git add .
git commit -m "first init"

git push -u origin master
