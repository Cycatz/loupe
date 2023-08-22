# SPDX-License-Identifier: BSD-3-Clause
#
# Author:   Gaulthier Gain <gaulthier.gain@uliege.be>
#
# Copyright (c) 2020-2023, University of Liège. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""Allows to add manually system calls via a custom CSV file (sanitize)."""

import csv
from collections import defaultdict

COVERAGE_SUITE="coverage-suite/"
COVERAGE_BENCHMARK="coverage-benchmark/"

def addSyscalls(syscallName, covFolder, used):
    covFolder.allSyscalls.add(syscallName)
    if used:
        covFolder.covSyscalls.add(syscallName)
    else:
        covFolder.notCovSyscalls.add(syscallName)
        covFolder.manualSetSyscalls.add(syscallName)
            
def readCsvManual(covFolder):
    
    if COVERAGE_SUITE in covFolder.htmlFolder:
        colIndex = 2
    else:
        colIndex = 1
    
    try:
        csvReader = csv.reader(open(covFolder.csvFile, 'r'), delimiter=',')
        for row in csvReader:
            syscallName = row[0]
            syscallUsed = row[colIndex].upper().strip()
            addSyscalls(syscallName, covFolder, syscallUsed == "X")
    except:
        print("[Error]: cannot read the CSV file: " + covFolder.csvFile)
        pass
    