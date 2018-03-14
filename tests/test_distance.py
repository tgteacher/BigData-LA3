import subprocess, os

def test_distance():
    command="python ./answers/distance2.py ./data/plants.data qc on output-qc-on.txt"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=="1708"+os.linesep)

    command="python ./answers/distance2.py ./data/plants.data ca az"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=="10718"+os.linesep)


