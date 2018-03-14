import subprocess, os

def test_data_frame():
    command="python ./answers/data_preparation.py ./data/plants.data urtica qc"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=="1"+os.linesep)
    
    command="python ./answers/data_preparation.py ./data/plants.data 'zinnia maritima' hi"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=="1"+os.linesep)

    command="python ./answers/data_preparation.py ./data/plants.data 'zinnia maritima' hi"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=="1"+os.linesep)

    command="python ./answers/data_preparation.py ./data/plants.data 'tephrosia candida' az"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=="0"+os.linesep)

