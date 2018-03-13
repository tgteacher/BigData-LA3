import subprocess, os

def test_data_frame():
    command="python ./answers/data_frame.py ./data/plants.data 11"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/data_frame.txt","r").read())
