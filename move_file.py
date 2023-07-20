import os
import shutil

from_dir = 'C:/Users/nicho/OneDrive/Desktop/Coding Class/Projects/Python/Class 102 Project/moving_files'
to_dir = 'C:/Users/nicho/OneDrive/Desktop/Coding Class/Projects/Python/Class 102 Project/document_files'

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file in list_of_files:
  name, ext = os.path.splitext(file)
  if ext == '':
    continue
  if ext in ['.txt', '.doc', '.docx', '.pdf']:
    path1 = from_dir + '/' + file
    path2 = to_dir
    path3 = to_dir + '/' + file
    if os.path.exists(path2):
      print('Moving ' + file + '...')
      shutil.move(path1, path3)
    else:
      os.makedirs(path2)
      print('Moving ' + file + '...') 
      shutil.move(path1, path3)