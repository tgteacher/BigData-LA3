import subprocess, os

def test_kmeans():
    file_name = "test-kmeans-4-1234.txt"
    command="python ./answers/kmeans.py ./data/plants.data 4 1234 {}".format(file_name)
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(open(file_name,"r").read()==open("tests/test-kmeans-undisclosed.txt","r").read())
