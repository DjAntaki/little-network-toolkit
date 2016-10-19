
for i in "csv_to_nx" "nx_to_csv" "nx_to_gif" "renderer"
do
    location="./lntk/scripts/${i}.py"
    echo $location
    chmod a+x $location
    cp $location /usr/local/bin/lntk-${i}
done
