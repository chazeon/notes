CWD=$(pwd)

pip3 install -r requirements.txt

cd plugins

for plugin in $(ls)
do
    pip3 install -Ue ./$plugin
done

cd $CWD

python3 -m mkdocs build