import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

"""
print(os.path.dirname(__file__))                                        # C:\workspace\jumptoflask03\config
print(os.path.dirname(os.path.dirname(__file__)))                       # C:\workspace\jumptoflask03
print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))      # C:\workspace
"""