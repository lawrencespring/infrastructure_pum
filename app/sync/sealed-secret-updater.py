#!/usr/bin/env python
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

def cloning_repo():
    #Clonning repo where this sealed secret should be placed
    print("Clonning repo")
