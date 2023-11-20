import random
from dane import USER_LIST
def gui(USER_LIST) -> None:
    while True:
      print(f'MENU: \n'
            f'ADD \n' 
            f'REMOVE \n'
            f'BROWSE \n'
            f'EXIT \n')
      odp = input(f'PICK A FUNCTION')

      match odp:
       case " ADD":
        add_user_to(USER_LIST)
       case " REMOVE":
        remove_user_from(USER_LIST)
       case " BROWSE":
        browse_users(USER_LIST)
       case " EXIT":
        print('MAPBOOK EXITED SUCCESSFULLY!')

def browse_users(USER_LIST: list) -> None:
    print("GREETINGS")
    print(f'THIS IS A MAPBOOK PROFILE OF {USER_LIST[0]["nickname"]}.')
    for user in USER_LIST:
        print(f'YOUR FRIEND {user["nickname"]} HAS POSTED {user["posts"]} POSTS')
def add_user_to(USER_LIST:list) -> None:
 while True:
    name = input("PLEASE INPUT THE NAME")
    nickname = input("PLEASE INPUT THE NICKNAME")
    post = random.randrange(1, 150)
    USER_LIST.append({'name': name, 'nickname': nickname, "posts": post})
    res = input("WOULD YOU LIKE TO INPUT ANOTHER ACCOUNT? YES/NO:")
    if res == "YES":
        add_user_to(USER_LIST)
    elif res == "NO":
        print("ALRIGHT")
    break
def remove_user_from(USER_LIST:list) -> None:
 while True:
    tmp_list = []
    name = input("PLEASE STATE THE NAME TO REMOVE:")
    for user in USER_LIST:
     if user["name"] == name:
        tmp_list.append(user)
        for user_to_be_removed in tmp_list:
            print(f'USERS FOUND:{user_to_be_removed}')
            print("0: REMOVE ALL USERS")
            number = int(input(f'SELECT AN ACCOUNT TO BE REMOVED: '))
            if number == 0:
                for user in tmp_list:
                    if user["name"] == name:
                        USER_LIST.remove(user)
                        print("ALL USERS HAVE BEEN SUCCESSFULLY REMOVED")
            else:
             print(number)
             print(tmp_list[number-1])
             USER_LIST.remove(tmp_list[number-1])

    res = input("WOULD YOU LIKE TO REMOVE ANOTHER ACCOUNT? YES/NO:")
    if res == "YES":
        remove_user_from(USER_LIST)
    elif res == "NO":
        print("ALRIGHT")
    break
