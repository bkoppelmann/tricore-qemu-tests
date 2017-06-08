#!/usr/bin/env python2
"""
  Copyright (c) 2017 Bastian Koppelmann Paderborn University

 This library is free software; you can redistribute it and/or
 modify it under the terms of the GNU Lesser General Public
 License as published by the Free Software Foundation; either
 version 2 of the License, or (at your option) any later version.

 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public
 License along with this library; if not, see <http://www.gnu.org/licenses/>.
"""

import os,sys

error = 0

def printhelp():
    print "USAGE: evaluate_results.py [options] TSIMDUMP QEMUDUMP"

def findQemuLineByNum(number):
    i = 0
    for qemuline in qemudata:
        qlinenum = qemuline.strip()[0:qemuline.find("(")]
        if (number).strip() == qlinenum:
            return i
        i=i+1
    return -1

def findTsimRegA(line):
    result = list()
    for i in range(0,15):
        string = "a"+str(i)+"["
        reg_pos = line.find(string)
        if reg_pos > 0:
            reg_pos = reg_pos +2+len(str(i))
        result.append(reg_pos)

    return result

def findTsimRegD(line):
        result = list()
        for i in range(0,15):
                string = "d"+str(i)+"["
                reg_pos = line.find(string)
                if reg_pos > 0:
                        reg_pos = reg_pos +2+len(str(i))
                result.append(reg_pos)

        return result


def getQemuRegAValue(line,reg):
    string = "a"+str(reg)+"["
    startpos = line.find(string)+2+len(str(reg))
    endpos = line.find("]",startpos)
    if "[" in line[startpos:endpos]:
        print "ERROR"

    return line[startpos:endpos]

def getQemuRegDValue(line,reg):
        string = "d"+str(reg)+"["
        startpos = line.find(string)+2+len(str(reg))
        endpos = line.find("]",startpos)
        return line[startpos:endpos]


def compareRegA(tsimline,qemuline,linenum):
    global error
    i = 0
    for startpos in findTsimRegA(tsimline):
        if startpos <> -1:
            endpos = tsimline.find("]",startpos)
            qemuvalue = getQemuRegAValue(qemuline,i).strip()
            if int(tsimline[startpos:endpos].strip(),16) <> int(qemuvalue,16):
                error = error +1
                print "Error at Instruction "+str(linenum) + " a["+str(i)+"] tsim =" + tsimline[startpos:endpos].strip() + ", qemu =" + qemuvalue
        i = i+1


def compareRegD(tsimline,qemuline,linenum):
    global error
    i = 0
    for startpos in findTsimRegD(tsimline):
        if startpos <> -1:
            endpos = tsimline.find("]",startpos)
            qemuvalue = getQemuRegDValue(qemuline,i).strip()
            if int(tsimline[startpos:endpos].strip(),16) <> int(qemuvalue, 16):
                error = error +1
                print "Error at Instruction "+str(linenum) + " d["+str(i)+"] tsim =" + tsimline[startpos:endpos].strip() + ", qemu =" + qemuvalue
        i = i+1

def comparePSW(tsimline, qemuline, linenum):
    global error
    
    tsim_start_pos = tsimline.find("psw:") + 4
    psw_tsim = tsimline[tsim_start_pos:].strip()

    qemu_start_pos = qemuline.find("PSW[") + 4
    qemu_end_pos = qemuline.find("]", qemu_start_pos)
    
    psw_qemu = qemuline[qemu_start_pos:qemu_end_pos].strip()

    if int(psw_tsim,16) <> int(psw_qemu,16):
        error = error +1
        print "Error at Instruction "+str(linenum) + " PSW: tsim =" + psw_tsim + ", qemu =" + psw_qemu


if len(sys.argv) < 3:
    printhelp()
    sys.exit(0)

tsimf = open(sys.argv[1],"r")
qemuf = open(sys.argv[2],"r")

tsimdata = tsimf.readlines()
qemudata = qemuf.readlines()

tsimline = str(tsimdata[0])
for tsimline in tsimdata:
    addresspos_start = int(tsimline.find("\t"))
    addresspos_end = int(tsimline.find("\t",addresspos_start+1))

    tsimaddress = tsimline[addresspos_start+1:addresspos_end]
    tsiminst_num = tsimline[0:tsimline.find("(")]
    qemulinepos = findQemuLineByNum(tsiminst_num)
    if qemulinepos == -1:
        print "Num "+str(tsiminst_num)+" not processed"
        error=1
        continue;

    compareRegA(tsimline,qemudata[qemulinepos],tsiminst_num)
    compareRegD(tsimline,qemudata[qemulinepos],tsiminst_num)
    comparePSW(tsimline,qemudata[qemulinepos], tsiminst_num)


if error == 0:
    print "Test successfull"


