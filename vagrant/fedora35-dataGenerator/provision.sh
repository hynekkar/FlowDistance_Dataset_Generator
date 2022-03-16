#!/bin/bash
#exit 0 
  yum -y install python3-pip
  yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
  yum -y install yum-plugin-copr
  yum -y copr enable @CESNET/NEMEA
  yum -y install wget
  yum -y install curl
  yum -y install net-tools
  yum -y install gcc
  yum -y install gcc-c++
  yum -y install htop
  yum -y install git
  yum -y install nemea
  yum -y install ipfixprobe
  yum -y install autoconf
  yum -y install automake
  yum -y install libtool
  yum -y install libpcap-devel
  yum -y install libtrap-devel.x86_64
  yum -y install unirec.x86_64
  yum -y install kernel-modules-extra
  yum -y install tcpdump
  yum -y install wireshark
  usermod -a -G wireshark vagrant

