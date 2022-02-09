CWD=$(pwd)

pip3 install -r requirements.txt

cd plugins ; ls | xargs pip3 install -Ue ; cd $CWD

python3 -m mkdocs build