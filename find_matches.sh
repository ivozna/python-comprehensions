path=$1
files=($path/*.txt)
echo $dir_name
python .\\find_matches\\sentences.py ${files[@]} >> result.txt
