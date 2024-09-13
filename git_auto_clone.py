import os
import subprocess

current_folder = os.getcwd()
print(current_folder)

'''
    https://lab.ssafy.com/im_1998/django_hw_1_2
'''
USER_NAME = 'im_1998'
SUBJECT = input('과목을 입력해 주세요. ex)django, db, js, vue :')
DAY = input('날짜를 입력해 주세요. : ')
# SEPERATOR = 'hw'
# STAGE = '2'

for sep in ['hw', 'ws']:
    # if sep == 'hw':
    for stage in [1, 2, 3, 4, 5, 'a', 'b', 'c']:
        BASE_URL = f'https://lab.ssafy.com/{USER_NAME}/{SUBJECT}_{sep}_{DAY}_{stage}'
        subprocess.run(['git', 'clone', BASE_URL])
print(BASE_URL)
