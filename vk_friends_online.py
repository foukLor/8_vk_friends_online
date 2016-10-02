import vk
import getpass


APP_ID = 5648299 


def get_user_login():
    return input("Please, enter your login:")


def get_user_password():
    return getpass.getpass("Your password:\n")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    friends = api.users.get(user_ids=friends_online_ids)
    return friends

    
def output_friends_to_console(friends_online):
    if not friends_online:
        print("Error:no online")
    for friend in friends_online:
        print(friend['first_name'] + " " + friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
