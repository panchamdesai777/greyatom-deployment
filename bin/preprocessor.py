# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:38:41 2020

@author: Dell
"""

import re

class PreprocessDoc:
    """
    Module for preprocessing articles
    """
    def removeSpclChar(self,text):
        """
        Remove special Characters
        
        Input:
            text: string
        Output:
            modifiedText: string
        """
        filteredText = re.sub(',|;|#|$','',text)
        return filteredText
    
    def convertToLower(self,text):
        return text.lower()
    

