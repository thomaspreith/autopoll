from pollevbot import PollBot


def main():
    user = 'My Username'
    password = 'My Password'
    host = 'PollEverywhere URL Extension e.g. "uwpsych"'
    login_type = 'pollev'

    
    with PollBot(user, password, host, login_type) as bot:
        bot.run()


if __name__ == '__main__':
    main()
