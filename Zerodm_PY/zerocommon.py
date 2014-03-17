# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:28:48 2014

@author: Vespa
"""
import re
def GetRE(content,regexp):
    return re.findall(regexp, content)