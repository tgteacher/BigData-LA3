import subprocess, os

def test_interests():
    command="python ./answers/interests.py ./data/plants.data 17 0.2 0.4"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/interests_undisclosed.txt","r").read())
