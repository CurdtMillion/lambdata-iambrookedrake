import usaddress
# Split address into multiple columns


def AddressSplit(Address):
    return usaddress.tag(Address)

if __name__ == '__main__':
    Address = input("Address Column: ")
    print(usaddress.tag(Address))
