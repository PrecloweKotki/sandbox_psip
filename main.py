from dane import USER_LIST

print(f'THIS IS A MAPBOOK PROFILE OF {USER_LIST[0]["nickname"]}.')
for user in USER_LIST:
    print(f'YOUR FRIEND {user["nickname"]} HAS POSTED {user["posts"]} POSTS')