while true:
    x = input().lower()
    output = ""
    for char in x:
        if char in ['a','e','i','o','u']:
            char = 'oob'
        output += char
    print(output)