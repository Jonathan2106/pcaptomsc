#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
    pcaptolist
    ~~~~~~~~~~~~~~~~~~~~
    Allow PCAP capture formated to list-of-dictionary for further process.

    See the README file for details.
    :author: Jonathan <m10802821@gapps.ntust.edu.tw>.
    :license: TBD, see LICENSE for details.
"""

import sys
from subprocess import Popen, PIPE

def pcaptolist(tshark_path, input_file):
    res = []

    pipe = Popen(tshark_path+" -r "+ input_file, stdout=PIPE)
    text = pipe.communicate()[0]
    
    lists = str(text,'utf-8').split('\r\n')

    for i in lists:
        temp =  i.strip().split()
        if len(temp) > 7:
            el = {
                "source": temp[2],
                "destination" : temp[4],
                "protocol" : temp[5],
                "info" : " ".join(temp[7:])
            }
            res.append(el)

    return res