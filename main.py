
import urllib.request
import time
import argparse
import sys

sys.path.insert(0, './libs')
from commandsExecutor import *
from tcpdumpHandler import *


corruptionValues = [0, 5, 10, 50, 80]
duplicationValues = [0, 5, 10, 50, 80]
lossValues = [0, 5, 10, 50, 80]
transferRateValues = [1, 2, 3, 10, 20]
delayValues = [50, 200, 300, 500]


def fetch(comm, url):
    comm.execute()
    time.sleep(1);
    try:
        page = urllib.request.urlopen(url)
    except:
        comm.remove()
        time.sleep(1);
        return
    comm.remove()
    time.sleep(1);

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



## MAIN

parser = argparse.ArgumentParser(description='Generate dataset for flow distance research')
parser.add_argument('-i', '--input', help='Path to file with input url', required=True)
parser.add_argument('-o', '--output', help='Output directory for packet captures', required=True)

args = parser.parse_args()

with open(args.input, newline='') as file:
    for line in file:
        url = line.strip()
        cap = tcpdump_handler( args.output + "/" + str(url).replace("https://","").replace("http://","") + ".pcap")
        cap.start_capture()

        generateCorruptionData(corruptionValues,url)
        generateDuplicationValues(duplicationValues, url)
        generateDelayValues(delayValues,url)
        generateLossValues(lossValues,url)
        generateTransferRateValues(transferRateValues,url)

        cap.stop_capture()


#dup = duplicationCommand(10);




#print(dup.getCommand());