#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo '$1 == PCAPDIR, $2 == TRAPDIR, $3 == CSVDIR'
fi


TRAPDIR="$2"
CSVDIR="$3"
PCAPDIR="$1"

for pcap in ./"$PCAPDIR"/*.pcap; do
	if [ ! -f "$pcap" ]; then
		continue
	fi
	echo Processing: "$pcap";
	tname=`echo "$pcap" | sed "s/\.\/$PCAPDIR\//$TRAPDIR\//g"`;
	cname=`echo "$pcap" | sed "s/\.\/$PCAPDIR\//$CSVDIR\//g"`;
	outname=${tname%.*}
	if [ ! -d `dirname $tname` ]; then
                mkdir -p `dirname $tname`;
        fi

	if [ ! -d `dirname $cname` ]; then
		mkdir -p `dirname $cname`;
	fi	
	
	/usr/local/bin/ipfixprobe -i "pcap;file=$pcap" -p "pstats;skipdup" -p "tls" -p "bstats" -p "phists" -o "unirec;i=f:$outname.trapcap;p=(pstats,phists,bstats,tls)"	
	/usr/bin/nemea/logger -t -i f:$outname.trapcap -w ${cname%.*}.csv
done;
