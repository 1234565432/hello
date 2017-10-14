import os
file_list=os.listdir(r'E:\PPT')
print(file_list)
saved_patch=os.getcwd()
print('current workingdirectory is'+saved_patch)
os.chdir(r'E:\PPT')
for index in range(len(file_list)) :
 print('old name'+file_list[index])
 #print('new name'+'file_list[index].tranalate(None,'0123456789'))
 os.renames(file_list[index],file_list[index].translate(None,'0123456789'))
os.chdir(saved_patch)