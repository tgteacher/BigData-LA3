import subprocess, os

def test_association_rules():
    command="python ./answers/association_rules.py ./data/plants.data 15 0.1 0.3"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/association_rules.txt","r").read())


