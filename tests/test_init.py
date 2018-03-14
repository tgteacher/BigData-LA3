import subprocess, os

def test_init():
    command="python ./answers/init.py 3 124"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/init.txt","r").read())
