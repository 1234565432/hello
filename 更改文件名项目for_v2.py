def rename_files():
    import os, sys
    path = r'E:\test'
    dirs = os.listdir(path)
    print(dirs)
    saved_path = os.getcwd()
    print('current working directory is' + saved_path)
    os.chdir(r'E:\test')
    for index in range(len(dirs)):
        print('old name ' + dirs[index])
        os.renames(dirs[index], dirs[index].translate(None, '0123456789'))
    os.chdir(saved_path)
rename_files()

