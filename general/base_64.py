from base64 import b64encode


def base64():
    hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    byte_string = bytes.fromhex(hex)
    flag = b64encode(byte_string).decode('utf-8')
    print(flag)
    
if __name__ == '__main__':
    base64()
    
    