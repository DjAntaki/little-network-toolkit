
#declare -a arr={"csv_to_nx","nx_to_csv","nx_to_gif","renderer"}

#for i in "${arr[@]]";
for i in "csv_to_nx" "nx_to_csv" "nx_to_gif" "renderer"
do
    location="./lntk/scripts/${i}.py"
    echo $location
    chmod a+x $location
    cp $location /usr/local/bin/lntk-${i}
#    cp $location /usr/local/bin/
#    mv /usr/local/bin/${i}.py /usr/local/bin/lntk-${i}
done

#To add as python library
#export PYTHONPATH="$PYTHONPATH:/path_to_/little-network-toolkit/lntk/"
