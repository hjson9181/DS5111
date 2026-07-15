ls
uname -a
ssh-keygen -t ed25519 -C "umw7eg@virginia.edu"
ls
cd .ssh
ls
cat id_ed25519
cat id_ed25519.pub
ssh -T git@github.com
pwd
ls
nano config
cat config
cd ..
ssh -T git@github.com
cd .ssh
nano
nano config
cd ..
pwd
ssh -T git@github.com
ll
sudo apt install python3.14-venv -y
sudo apt update
sudo apt install make -y
sudo apt install python3.14-venv -y
sudo apt install tree
nano init.sh
chmod +x init.sh
bash init.sh
tree
nano init_git_creds.sh
chmod +x init_git_creds.sh
bash init_git_creds.sh 
git clone git@github.com:/2508_DS5111_.git
ls -la ~/.ssh/
cat ~/.ssh/config
nano ~/.ssh/config
ssh -T git@github.com
git clone git@github.com:2508_DS511_umw7eg.git
git clone git@github.com:2508_DS5111_umw7eg.git
git clone git@github.com:2508_DS5111_.git
git clone git@github.com:2508_DS5111_umw7eg.git
git clone git@github.com:hjson9181/DS5111.git
git clone git@github.com:2508_DS5111_dpy8wq.git
git clone git@github.com:/2508_DS5111_.git
ls
cd ~/.ssh
ls
ls -lart
nano ~/.bashrc
source ~/.bashrc
cd
pwd
git clone git@github.com:hjson9181/DS5111.git
ls
rm -rf DS5111/
git clone git@github.com:hjson9181/DS5111.git
cd DS5111
mkdir scripts
cd scripts
mv ~/init.sh .
mv ~/init_git_creds.sh .
cd ..
git add .
git commit -m "saving our two init files"
source ~/.bashrc 
reboot now
sudo reboot now
cd DS5111
git push
makefile --version
make --version
nano makefile
nano requirements.txt
make
nano makefile
make
make update
. env/bin/activate
git add .
git commit -m "added a makefile"
git push
nano README.md
ls
cd DS5111/
git status
vi ~/.bashrc 
git add README.md && git commit -m "Update README.md" && git push
git add .
cd .. 
pwd
cd ~/.ssh
pwd
git add .
cd DS5111
cd ..
pwd
cd DS5111
git add .
git commit -m "adding README.md"
git push
cd
pwd
ls
mkdir playmake
cd playmake
nano makefile
cd
pwd
ls
nano playmake
make job1
make
ls
cat y
nano y
rm y
ls
nano playmake
pwd
ls
cd DS5111
ls
git branch
find ~ -name "clean_ids.py"
find ~ -type d -name ".git"
exit
cat ~/.bashrc 
pip list --outdates
pip list --outdated
pip install --upgrade pandas numpy pylint
sudo apt install python3-pip
pip list --outdated
pip install --upgrade pandas
pip install --upgrade pandas numpy pylint --break-system-packages
pylint --help
sudo apt install pylink
sudo apt install pylint
pylint --help
pylint
pylint bin/clean_ids.py
pwd
ls
cd DS5111
ls
cat requirements.txt
nano requirements.txt 
pylint
pylint bin/clean_ids.py
cd ..
pwd
cd DS5111
ls
cd scripts
ls
cd ..
ls
cd ..
pwd
git --version
cd
pwd
git clone git@github.com:hjson9181/DS5111.git
git status
git pull
cd DS5111
git init
git remote add origin git@github.com:hjson9181/DS5111.git
git pull origin main
rm -rf DS5111
git clone git@github.com:hjson9181/DS5111.git
cd DS5111
git status
ls
cd ..
pwd
cd DS5111
ls
cd DS5111
ls
cd scripts
ls
cd ..
rm -rf DS5111
ls
cd scripts
ls
pylint bin/clean_ids.py
ls
git status
git add .
git commit -m "added pylint"
git push
cd ..
pwd
ls
pylint --generate-rcfile >> pylintrc
ls
nano pylintrc
lint:
make lint
pylint --generate-rcfile >> pylintrc
grep -n "indent-string" pylintrc
pylint bin/clean_ids.py
pwd
ls
cd DS5111
ls
scripts
cd scripts
ls
cd DS5111
pwd
ls
git pull
git branch
pwd
git checkout main
git pull origin main
ls 
cd scripts
ls
cd ..
ls
mv scripts bin
ls
git add .
git commit -m "renamed scripts folder to bin" 
git push
ls
nano requirements.txt 
make update
ls
cd DS5111
ls
mkdir tests
cd tests
touch test_clean_ids.py
cd ..
ls
touch pytest.init
mv pytest.init pytest.ini
ls
[pytest]
pythonpath = .
import bin.clean_ids
sudo apt install imagemagick-7.q16
import bin.clean_ids
python3
python3 bin/clean_ids.py
ls
pythonpath = .
pytest pythonpath = .
nano pytest.ini
import bin.clean_ids
cd tests
ls
cd ..
cd tests
ls
nano test_clean_ids.py 
pytest -vv tests
pwd
ls
cd ..
pytest -vv tests
sudo apt install python3-pytest
pytest -vv tests
ls
nano makefile
make lint
make test
ls
nano makefile
make test 
git status
git add .
git commit -m "added pytest and linter"
git push
git revert <commit-hash>
git branch feature/LAB03_pytest_and_linter
ls
cd DS5111
ls
git status
git branch feature/LAB03_pytest_and_linter
git reset --hard HEAD-1
git reset --hard HEAD~1
git push --force-with-lease origin main
git push origin feature/LAB03_pytest_and_linter 
git branch -m feature/LAB03_pytest_and_linter LAB03_pytest_and_linter
git push origin -u LAB03_pytest_and_linter
git push origin --delete feature/LAB03_pytest_and_linter
pwd
mkdir .github/workflows
ls
cd DS5111
LS 
ls
mkdir .github/workflows
git branch
mkdir -p .github/workflows
git checkout -b "adding_ci_yml"
git add ci.yml
git branch
git status
git push --set-upstream origin adding_ci_yml
pwd
wget https://raw.githubusercontent.com/EfrainOlivaresUVA/2605_DS5111_materials/refs/heads/main/scripts/ci.yml
git add ci.yml
git commit -m "adding ci.yml"
git push
mv ci_yml ~/bin
python --version
git status
git branch
git sttus
git status
pwd
ls
cd DS5111
ls
git branch
ls
nano ci.yml
ls
git add .
git commit -m "uncommented the last few lines"
git push
git branch
mv main
git main 
git switch main
mkdir -p .github/workflows
cd .github/workflows
wget https://raw.githubusercontent.com/EfrainOlivaresUVA/2605_DS5111_materials/refs/heads/main/scripts/ci.yml
git add .
git commit -m "added ci.yml in main branch"
git push
pwd
cd DS5111
ls
nano makefile
nano bin
cd bin
ls
cd ..
ls
nano env
nano requirements.txt 
cd bin
ls
nano clean_ids.py 
ls
cd ..
ls
git branch
git switch LAB03_pytest_and_linter
ls
nano makefile
cd tests
ls
nano test_clean_ids.py 
pytest -vv tests
nano test_clean_ids.py 
ls
cd ..
l
ls
pytest -vv tests
nano test_clean_ids.py 
ls
nano makefile
make test
ls 
cd tests
ls
cd test_clean_ids.py
nano test_clean_ids.py 
cd ..
ls
cd bin
ls
nano clean_ids.py 
python3 clean_ids.py
nano clean_ids.py 
python3 clean_ids.py
nano clean_ids.py 
python3 clean_ids.py
nano clean_ids.py 
python3 clean_ids.py
nano clean_ids.py 
python3 clean_ids.py
pwd
git branch
ls
cd DS5111/
LS
ls
git branch
cd bin
ls
cd ..
cd tests
ls
pwd
cd DS5111
ls
pylint bin/clean_ids.py
sed -i 's/[[:space:]]*$//' bin/clean_ids.py
pylint bin/clean_ids.py
echo "" >> bin/clean_ids.py
pylint bin/clean_ids.py
perl -i -pe 'chomp if eof' bin/clean_ids.py
pylint bin/clean_ids.py
sed -n '33,38p' bin/clean_ids.py | cat -A
pylint bin/clean_ids.py
pwd
cd DS5111
ls
cd tests
ls
pylint test_clean_ids.py 
sed -i 's/[[:space:]]*$//' test_clean_ids.py
grep -Pn '\s+$' test_clean_ids.py && echo "FOUND" || echo "CLEAN"
pylint test_clean_ids.py 
pylint --generate-rcfile > .pylintrc
init-hook='import sys; sys.path.insert(0, ".")'
pylint --init-hook='import sys; sys.path.insert(0, ".")' test_clean_ids.py
pylint test_clean_ids.py 
python version
python3 version
pwd
python3 --version
pylint test_clean_ids.py 
pwd
ls
cd DS5111
ls
pylint test_clean_ids.py 
cd tests
ls
pylint test_clean_ids.py 
sed -i 's/[[:space:]]*$//' test_clean_ids.py
pylint test_clean_ids.py 
echo "" >> test_clean_ids.py 
pylint test_clean_ids.py 
sed -i 's/[[:space:]]*$//' test_clean_ids.py
pylint test_clean_ids.py 
sed -i 's/[[:space:]]*$//' test_clean_ids.py
pylint test_clean_ids.py 
pwd
ls
cd DS5111
ls
cd tests
pylint test_clean_ids.py 
pwd
cd DS5111
ls
cd tests
ls
pylint test_clean_ids.py 
git status
git add .
git status
git branch
git add . 
git commit -m "added more tests in script"
git push
git status
git add .
git commit -m "pytest.mark.skip placerholder added"
git push
pylint test_clean_ids.py 
sed -i 's/[[:space:]]*$//' test_clean_ids.py
pylint test_clean_ids.py 
cd ..
cat .gitignore
git status
pwd
cd DS5111
ls
cd tests
pytest test_extract_transcripts.py -v
export WEBSHARE_USER="gwmpvptd"
export WEBSHARE_PASSWORD="7eyh69wtglfm"
pytest test_extract_transcripts.py -v
cd ..
pip list | grep youtube
pytest test_extract_transcripts.py -v
cd tests
pytest test_extract_transcripts.py -v
. env/bin/activate
pip install youtube-transcript-api python-dotenv
. env/bin/activate
cd ..
. env/bin/activate
pip install youtube-transcript-api python-dotenv
which pip
ls
pytest tests/test_extract_transcripts.py 
git branch
git branch LAB04_extract_transcript
git branch
git switch LAB04_extract_transcript 
git status
git add .
git commit -m "added tests for extract_transcripts.py"
git push
git branch
git switch main
git branch
mkdir .github/workflows
cd .github/workflows
ls
git branch
pwd
cd DS5111
pwd
git branch
git switch LAB04_extract_transcript 
git branch
git switch LAB04_extract_transcript 
git status
git branch
git status
git switch LAB04_extract_transcript 
cd .github
git branch
git add .
git commit -m "extract_transcripts and tests are done"
git push
git push --set-upstream origin LAB04_extract_transcript
git push
cat .github/workflows/*.yml
git checkout LAB04_extract_transcript
git checkout main -- .github/workflows/pytest.yml
git checkout main -- .github/workflows/ci.yml
git add .github/workflows/ci.yml
git commit -m "brought ci.yml to LAB04 branch from main branch"
git push
git status
git add .
git commit -m "added LAB04 branch in ci.yml"
git push
pytest test/test_extract_transcripts.py
pytest tests/test_extract_transcripts.py
. env/bin/activate
pytest -vvx tests/
cat bin/clean_ids.py
pytest -vvx tests/
cd ..
cd .ssh
ls
config
cd ..
pwd
~/.ssh/config
ssh uva-ec2
tmux new -s JUP
. env/bin/activate
ssh uva-ec2
ls
cd DS5111/
ls
git branch
git switch LAB03_pytest_and_linter 
git status
git add .
git commit -m "updating test script"
git push
git pull origin LAB04_extract_transcript --rebase
git add .
git rebase --continue
git push origin LAB04_extract_transcript 
git status
git switch LAB03_pytest_and_linter 
ls
nano makefile
git add .
git commit -m "updated makefile with test: litn"
git push
ls
cd tests
ls
nano test_clean_ids.py
ls
git status
cd DS5111
git status
ls
nano requirements.txt 
ls
cd DS5111
git status
ls
nano requirements.txt
git status
make update
ls
cd DS5111
ls
make update
cd bin
ls
nano enrich_transcripts.py
cat extract_transcripts.py 
ls
nano enrich_transcripts.py 
nano extract_transcripts.py 
cat extract_transcripts.py 
git status
cd ..
exit
tmux new -s JUP
git status
cd DS5111
git status
ls
nano requirements.txt
cd bin
ls
git switch main
git add .
git commit -m "added genai to requirements.txt"
git push
git pull
git push
git status
git add .
git commit -m "updated requirements.txt"
git pull --no-rebase
git push
cd .. 
git status 
git pull
ls
nano requirements.txt 
cat requirements.txt 
git add .
git commit -m "add genai into req.txt"
git push
git pull
git pull --no-rebase
nano requirements.txt 
git add requirements.txt 
git commit
git push
pwd
cd DS5111
ls
echo "dQw4w9WgXcQ" | python bin/extract_transcripts.py
echo "dQw4w9WgXcQ" | python3 bin/extract_transcripts.py
. env/bin/activate
echo "dQw4w9WgXcQ" | python3 bin/extract_transcripts.py
.env
git status
git check-ignore .env
cat bin/enrich_transcripts.py
git log -p -- bin/extract_transcripts.py | grep -i "gwmpvptd\|7eyh69wtglfm"
ls
cd DS5111
cat mock_transcripts.jsonl
cat mock_transcripts.jsonl | python -u 
cat mock_transcripts.jsonl | python3 -u 
bin/enrich_transcripts.py
ls
cd playmake
ls
cd ..
cd DS5111
ls -la
cat .env
cd ..
cat .env
ls -la | grep -i env
pwd
ls -la
pwd
cd DS5111
ls -la | grep -i env
cat .env.example
cat .env
ls
cd DDS5111
cd DS5111
ls
cat mock_transcripts.jsonl | python3 -u bin/enrich_transcripts.py
. env/bin/activate
pip install python-dotenv google-genai
pip list | grep -i -E "dotenv|genai"
ls requirements.txt
pip install -r requirements.txt
cat mock_transcripts.jsonl | python3 -u bin/enrich_transcripts.py
cat e.v
cat .env
echo "GEMINI_API_KEY =AIzaSyBZEjX2kO6bWu98tBnsE8rc8Av3pODom2k > .env


echo "GEMINI_API_KEY=AIzaSyBZEjX2kO6bWu98tBnsE8rc8Av3pODom2k > .env


echo "GEMINI_API_KEY=AIzaSyBZEjX2kO6bWu98tBnsE8rc8Av3pODom2k" > .env
cat mock_transcripts.jsonl | python3 -u bin/enrich_transcripts.py
git status
cat .gitignore | grep -i env
cd env
cat .gitignore | grep -i env
cd ..
pwd
cat .gitignore | grep -i env
echo '.env' >> .gitignore
cat .gitignore | grep -i env
ls
cat .env
git status
git add.
git add .
git commit -m "added enrichment files"
git push
make test_enrich
ls
cd DS5111
ls
ls .env
ls .gitignore
nano .gitignore
nano .env
ls .gitignore/.env
quit
exit
pwd
ls
cd DS5111/
ls
make lint
git add .
git commit -m "feat: implement abstract base class interface"
git commit -m "feat: implement concrete gemini strategy"
git add .
git commit -m "feat: implement concrete gemini strategy"
PWD
pwd
cd DS5111
ls
git status
git commit -m "feat: implement orchestrator with dependency injection"
make test
cat pytest.ini
ls -la ~/DS5111
ls -la ~/DS5111/tests
make test
git commit -m "test: add mock testing for pipeline orchestrator"
