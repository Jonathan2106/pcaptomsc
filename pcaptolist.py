#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
    pcaptolist
    ~~~~~~~~~~~~~~~~~~~~
    Allow PCAP capture formated to list-of-dictionary for further process.

    See the README file for details.
    :author: Jonathan <m10802821@gapps.ntust.edu.tw>.
    :license: MIT, see LICENSE for details.
"""

import sys
from subprocess import Popen, PIPE

def pcaptolist(tshark_path, input_file):
    res = []

    pipe = Popen(tshark_path+" -r "+ input_file + " -T tabs", stdout=PIPE)
    text = pipe.communicate()[0]
    
    lists = str(text,'utf-8').split('\r\n')

    for i in lists:
        temp =  i.strip().split('\t')
        if len(temp) > 7:
            source = temp[2].strip()
            if source == "":
                source = "-"
            destination = temp[4].strip()
            if destination == "":
                destination = "-"
            protocol = temp[5].strip()
            info = " ".join(temp[7:])

            el = {
                "source": source,
                "destination" : destination,
                "protocol" : protocol,
                "info" : info
            }
            res.append(el)

    return res