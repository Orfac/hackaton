from pathlib import Path

private_key = None


def auth():
    my_file = Path("private_key.txt")
    private_key = None
    if my_file.is_file():
        f = open('private_key.txt', 'r')
        private_key = f.readline()
        f.close()
    if private_key is None:
        print('Want to register? Y/N')
        ans = input()
        if ans == 'Y' or 'y':
            register()
    else:
        menu()

def register():
    pass
def menu():
    print('1) Give permission to ICO/User')
    pass