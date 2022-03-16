from commandsExecutor import *
import urllib.request
import csv

corruptionValues = [0, 5, 10, 50, 80]
duplicationValues = [0, 5, 10, 50, 80]
lossValues = [0, 5, 10, 50, 80]
transferRateValues = [1, 2, 3, 10, 20]
delayValues = [50, 200, 300, 500]


def fetch(comm, url):
    comm.execute()
    try:
        page = urllib.request.urlopen(url)
    except:
        comm.remove()
        pass
    comm.remove()

def generateCorruptionData(values, url):
    for value in values:
        comm = corruptionCommand(value);
        fetch(comm, url);


def generateDuplicationValues(values, url):
    for value in values:
        comm = duplicationCommand(value);
        fetch(comm, url);

def generateLossValues(values, url):
    for value in values:
        comm = packetLossCommand(value);
        fetch(comm, url);

def generateTransferRateValues(values, url):
    for value in values:
        comm = limitTransferRateCommand(value);
        fetch(comm, url);

def generateDelayValues(values, url):
    for value in values:
        comm = delayCommand(value);
        fetch(comm, url);


with open('input_url', newline='') as file:
    for line in file:
        url = line.strip()
        generateDelayValues(delayValues,url)
        sys.exit()


#dup = duplicationCommand(10);




#print(dup.getCommand());