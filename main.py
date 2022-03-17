
import urllib.request
import time
import argparse
import sys
import os
from datetime import datetime

sys.path.insert(0, './libs')
from commandsExecutor import *
from tcpdumpHandler import *


corruptionValues = [0, 5, 10, 50, 80]
duplicationValues = [0, 5, 10, 50, 80]
lossValues = [0, 5, 10, 50, 80]
transferRateValues = [1, 2, 3, 10, 20]
delayValues = [50, 200, 300, 500]


def fetch(comm, url, content_file_name):
    comm.execute()
    time.sleep(1);
    try:
        page = urllib.request.urlopen(url)
    except Exception as e:
        print(e)
        comm.remove()
        time.sleep(1);
        return
    comm.remove()

    date = datetime.now().strftime("%Y%m%d-%H%M%S")
    content_file_name = content_file_name + date + ".html"
    try:
        os.makedirs(os.path.dirname(content_file_name), exist_ok=True)
        f = open(content_file_name, "wb")
        f.write(page.read())
        f.close();
    except:
        print("Could not write downloaded content.")
        sys.exit(1)
    time.sleep(1);

def generateCorruptionData(values, url, content_file_name):
    for value in values:
        comm = corruptionCommand(value);
        fetch(comm, url, content_file_name);


def generateDuplicationValues(values, url, content_file_name):
    for value in values:
        comm = duplicationCommand(value);
        fetch(comm, url, content_file_name);

def generateLossValues(values, url, content_file_name):
    for value in values:
        comm = packetLossCommand(value);
        fetch(comm, url, content_file_name);

def generateTransferRateValues(values, url, content_file_name):
    for value in values:
        comm = limitTransferRateCommand(value);
        fetch(comm, url, content_file_name);

def generateDelayValues(values, url, content_file_name):
    for value in values:
        comm = delayCommand(value);
        fetch(comm, url, content_file_name);



## MAIN

parser = argparse.ArgumentParser(description='Generate dataset for flow distance research')
parser.add_argument('-i', '--input', help='Path to file with input url', required=True)
parser.add_argument('-o', '--output', help='Output directory for packet captures', required=True)
parser.add_argument('-c', '--content', help='Output directory for downloaded content', required=True)

args = parser.parse_args()

with open(args.input, newline='') as file:
    for line in file:
        url = line.strip()
        file_name = str(url).replace("https://","").replace("http://","");
        content_path = str(args.content) + "/" + file_name+ "/"
        cap = tcpdump_handler( args.output + "/" + file_name + ".pcap")
        cap.start_capture()

        generateCorruptionData(corruptionValues,url,content_path)
        generateDuplicationValues(duplicationValues, url,content_path)
        generateDelayValues(delayValues,url,content_path)
        generateLossValues(lossValues,url,content_path)
        generateTransferRateValues(transferRateValues,url, content_path)

        cap.stop_capture()
