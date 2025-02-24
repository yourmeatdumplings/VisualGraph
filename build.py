import os

if __name__ == '__main__':
    os.system(
        'pyinstaller -F run.py -n VisualGraph -w'
    )