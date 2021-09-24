#!/usr/bin/env python3
# converts a string to a float whilst removing all unallowed characters

def str2float(text: str) -> float:
    
    if text == "" or len(text) == 0:
        print("str2float: string is emtpy")
        return False 

    allowed_chars = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.' ]

    # for i in text:

    #     if i == ",":
    #         if comma_count >= 1:
    #             text = text.replace(i, ".", 1)
    #             print(type(print(text)))
    #             comma_count += 1

    #     if i not in allowed_chars:
    #         text = text.replace(i, "")

    # return float(text)
    for i in text:
        if i not in allowed_chars:
            text = text.replace(i, "")
    
    return float(text)
if __name__ == "__main__":
    print(str2float("21,123.23"))
