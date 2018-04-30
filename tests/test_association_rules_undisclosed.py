import subprocess, os

def test_association_rules():
    command="python ./answers/association_rules.py ./data/plants.data 17 0.2 0.4"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/association_rules_undisclosed.txt","r").read())


