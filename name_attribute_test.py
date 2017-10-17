'''name
test'''
import sys
if __name__ == '__main__':
    print('independent')
else:
    print('be imported', __name__)
print('done')