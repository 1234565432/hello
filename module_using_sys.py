import sys
print('the command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nthe python path is', sys.path, '\n')
if __name__ == '__main__':
    print('independent')
else:
    print('imported,the name is', __name__)
print('done')
