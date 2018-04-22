from transfer_json import *
from crypt import *


def main():
    private_key, public_key = generate_keys()
    a = send_json('asd'.encode('utf8'), public_key)
    print(a)
    b = get_json(a, private_key)


if __name__ == "__main__":
    main()
