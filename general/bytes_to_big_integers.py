from Crypto.Util.number import *

def main():
    int_val = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    flag = long_to_bytes(int_val).decode('utf-8')
    print(flag)

    ### alternate way without any library support
    # v = str(hex(int_val))[2:]
    # flag = ""
    # for i in range(0, len(v), 2):
    #     flag += chr(int(str(v[i:i+2]), 16))
    # print(flag)

if __name__ == '__main__':
    main()