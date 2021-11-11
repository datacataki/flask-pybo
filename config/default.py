import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR) # C:/projects/myproject

# 기존 config.py파일의 위치는 C:/projects/myproject에서 default.py파일의 위치가 C:/projects/myproject/config로 디렉터리의 깊이가
# 1만큼 더 늘어났으므로, os.path.dirname을 한번 더 사용해서 BASE_DIR을 설정함

# BASE_DIR_prev = os.path.dirname(__file__)
# print(BASE_DIR_prev) #C:/projects/myproject/config

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# print(PROJECT_ROOT) # C:\projects\myproject\config