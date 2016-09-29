import vk
import getpass
import urllib


APP_ID = 5648299 

def create_connect():
    print(urllib.request.urlopen("https://vk.com"))

def get_user_login():
    return input("Please, enter your login:")


def get_user_password():
    return getpass.getpass("Your password:\n")

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    all_friends = api.friends.get(fields='name', order='name')
    friends = []

    for friend in all_friends:
        if friend['online']==1:
            friends.append(friend['first_name'] + " " + friend['last_name'])
    return friends

def output_friends_to_console(friends_online):
    if not friends_online:
        print("Error:no online")
    print(friends_online)

if __name__ == '__main__':
    create_connect()
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
