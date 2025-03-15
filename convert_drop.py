import items
from mailing import parse_packet

def convert_drop(arr):
    msg = ""
    i = 0
    for i in arr:
        parsed_drop = parse_packet(i)
        str_byte = "".join(parsed_drop[2:len(parsed_drop)])
        if str_byte in items.spring_data.keys():
            msg += f'{items.spring_data[str_byte]} '
        else: msg += "NO_DATA "
    
    return msg
        