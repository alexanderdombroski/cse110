friend = ""
friend_list = []
while friend.lower() != "end":
    friend = input("Type a name of a friend: ").capitalize()
    if friend.lower() != "end":
        friend_list.append(friend)

print("Your friends are:")

for name in friend_list:
    print(name)