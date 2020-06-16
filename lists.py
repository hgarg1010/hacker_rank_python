
list_container = []

n = int(input())
for i in range(n):
    data = input().split(" ")
    command_len = len(data)
    command_name = data[0]
    
    if command_len == 1:
        # print command
        if command_name == "print":
            print(list_container)
        elif command_name == "sort":
            list_container.sort()
        elif command_name == "reverse":
            list_container = list_container[::-1]
        else:
            #pop
            list_container.pop()


    elif command_len == 2:
        # remove append
        if command_name == "remove":
            list_container.remove(int(data[1]))
        else:
            #append
            list_container.append(int(data[1]))

    elif command_len == 3:
        # insert
        list_container.insert(int(data[1]),int(data[2]))
