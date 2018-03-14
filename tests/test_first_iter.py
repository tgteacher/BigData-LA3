import subprocess, os

def test_first_iter():
    command="python ./answers/first_iter.py ./data/plants.data 3 123"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/first_iter.txt","r").read())
