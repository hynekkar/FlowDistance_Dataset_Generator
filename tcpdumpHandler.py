import subprocess

class tcpdump_handler:
    path = None;
    tcpdumpProcess = None;
    ifc = None;
    def __init__(self, path, ifc="eth0"):
        self.path = path;
        self.ifc = ifc;

    def start_capture(self):
        self.tcpdumpProcess = subprocess.Popen(["tshark", "-i", self.ifc, "-w",self.path ,"-f", "port 443"]);

    def stop_capture(self):
        self.tcpdumpProcess.terminate()
