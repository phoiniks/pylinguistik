#!/usr/bin/python3
from sys import argv
import re


def ngrammer(serialisierter_text, n):

    """ngrammer erwartet einen serialisierten Text,
    d.h. eine Liste von Wörtern in genau der Reihenfolge
    wie sie im ursprünglichen Text vorliegt."""
    
    try:
        n = int(n)
    except ValueError as te:
        print(te)
        print("Bitte nur ganzzahlige Werte eingeben!")
        return
    
    for idx in range(0, len(serialisierter_text)):
        if idx <= len(serialisierter_text) - n:
            yield serialisierter_text[idx:idx + n]
        else:
            return
