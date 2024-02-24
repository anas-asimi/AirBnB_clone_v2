#!/usr/bin/python3
""" string_to_dict function """


def string_to_dict(args: str):
    dictionary = {}
    for arg in args.split(" "):
        if '=' in arg:
            [key, value] = arg.split("=")
            # string
            if '"' in value:
                dictionary[key] = value.replace('"', '').replace('_', ' ')
            # float
            elif '.' in value:
                dictionary[key] = float(value)
            # int
            else:
                dictionary[key] = int(value)
    return (dictionary)

if __name__ == "__main__":
    print(string_to_dict(
        'Place city_id="0001" name="My_little_house" number_rooms=4 latitude=37.773972'))
