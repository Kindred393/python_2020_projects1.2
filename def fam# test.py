def famNum():
    while True:
        print("How many members in your family?")
        response = input()
        if len(response) < 1:
            return response
        elif len(response) > 10:
            return response
        else:
            continue

        
print(famNum)
