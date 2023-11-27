import random
from dane import USER_LIST
def gui(USER_LIST) -> None:
    while True:
      print(f'MENU: \n'
            f'ADD \n' 
            f'REMOVE \n'
            f'BROWSE \n'
            f'UPDATE \n'
            f'EXIT \n')
      odp = input(f'PICK A FUNCTION')

      match odp:
       case "ADD":
        add_user_to(USER_LIST)
       case "REMOVE":
        remove_user_from(USER_LIST)
       case "BROWSE":
        browse_users(USER_LIST)
       case "UPDATE":
        update_usser(USER_LIST)
       case "EXIT":
        print('MAPBOOK EXITED SUCCESSFULLY!')
        break

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

def update_usser(USER_LIST:list[dict,dict])->None: # 2 razy dict znaczy że obiektów jest 2 lub więcej
    nick_of_user = input('PLEASE STATE A NAME OF THE USER TO MODIFY')
    for user in USER_LIST:
        if user['nickname']==nick_of_user:
            print('FOUND')
            user['name']=input('STATE A NEW NAME: ')
            user['nickname']=input('STATE A NEW NICKNAME: ')
            user['posts']=int(input('STATE A NUMBER OF POSTS: '))

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
