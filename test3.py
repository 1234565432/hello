import os
def test3():
 file_list=os.listdir(r'E:\PPT')
 print(file_list)
 saved_patch=os.getcwd()
 print('current workingdirectory is'+saved_patch)
 os.chdir(r'E:\PPT')
   for file_name in file_list:
     print('old name'+file_name)
     print('new name'+filename.tranalate(None,'0123456789'))
     os.renames(file_name,file_name.translate(None,'0123456789'))
   os.chdir(saved_patch)
test3()