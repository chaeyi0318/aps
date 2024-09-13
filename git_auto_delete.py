# 자동으로 .git 삭제하는 코드
import os
import subprocess

current_folder = os.getcwd()
print(current_folder)

# 현재 폴더의 모든 하위 폴더를 반복
for folderName, subfolder, fileNames in os.walk(current_folder):
    # print(folderName, subfolder, fileNames)
    # root directory는 제외하고
    if folderName == current_folder:continue
    folder_path = os.path.join(folderName, '.git')
    subprocess.run(['rm', '-rf', folder_path])
    print(f'{folder_path} 폴더가 삭제 되었습니다.')