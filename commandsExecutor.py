import random
import os
import time
import sys

class command:
    rate = None;
    intf = None;
    command = None;
    delcommand = None;
    __executed = None;

    def __init__(self, rate=None, intf = "eth0"):
        if rate == None:
            self.rate = random.randint(10,90);
        else:
            self.rate = rate;
        self.intf = intf;
        self.__executed = False;

    def __del__(self):
        if self.__executed:
            self.remove();

    def __exit__(self):
        if self.__executed:
            self.remove();

    def execute(self):
        if(self.command):
            os.system(self.command);
            self.__executed = True;
    def remove(self):
        if(self.delcommand):
            os.system(self.delcommand)
            self.__executed = False;

    def getCommand(self):
        return self.command

class corruptionCommand(command):
    def __init__(self, rate = None):
        super().__init__(rate = rate)

        self.command = "sudo tc qdisc add dev {0} root netem corrupt {1}%".format(self.intf, self.rate)
        self.delcommand = "sudo tc qdisc del dev {0} root netem corrupt {1}%".format(self.intf, self.rate)

class duplicationCommand(command):
    def __init__(self, rate = None):
        super().__init__(rate = rate)
        self.command = "sudo tc qdisc add dev {0} root netem duplicate {1}%".format(self.intf, self.rate)
        self.delcommand = "sudo tc qdisc del dev {0} root netem duplicate {1}%".format(self.intf, self.rate)


class packetLossCommand(command):
    def __init__(self, rate = None):
        super().__init__(rate = rate)

        self.command = "sudo tc qdisc add dev {0} root netem loss {1}%".format(self.intf, self.rate)
        self.delcommand = "sudo tc qdisc del dev {0} root netem loss {1}%".format(self.intf, self.rate)

class limitTransferRateCommand(command):
    def __init__(self, rate = None):
        super().__init__(rate = rate)

        self.command = "sudo tc qdisc add dev {0} root netem rate {1}Mbit".format(self.intf, self.rate)
        self.delcommand = "sudo tc qdisc del dev {0} root netem rate {1}Mbit".format(self.intf, self.rate)

class limitTransferRateCommand(command):
    def __init__(self, rate = None):
        super().__init__(rate = rate)

        self.command = "sudo tc qdisc add dev {0} root netem delay {1}ms 50ms distribution normal".format(self.intf, self.rate)
        self.delcommand = "sudo tc qdisc del dev {0} root netem delay {1}ms 50ms distribution normal".format(self.intf, self.rate)




