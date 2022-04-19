from os.path import dirname, realpath, join
from utils.jlib import JsonManager
from getpass import getpass
from textwrap import dedent

class JLogin(JsonManager):
    def __init__(self):
        self.root = dirname(realpath(__file__))
        self.path_data = join(self.root + '/data/data.json')

    def sign_in(self):
        # data = JsonManager().read_json(self.path_data)
        print('### Sign in ###')
        username = input('Enter your username: ')
        senha = getpass('Enter your password: ')
        senha_verify = getpass('Repeat your password: ')

        while senha != senha_verify:
            print('Password do not match!')
            senha = getpass('Enter your password: ')
            senha_verify = getpass('Repeat your password: ')

        JsonManager().create_json(self.path_data, username, senha)
        print('Registration done!')

    def home(self, data):

        opc = '0'
        while opc != '2':

            print(dedent('''
            Menu:

            1 - Alterar Login.
            2 - Sair

            Escolhar uma opção: 
            '''))

            opc = input('> ')

            if opc == '1':
                self.update_login(data)
                break
            elif opc == '2':
                break
            else:
                print('Option invalid!')

    def update_login(self, data):
        print('### Update Login ###')

        username = input('Enter your username: ')
        old_password = getpass('Enter your old password: ')
        while (username != data['username']) or (old_password != data['password']):
            print('Username or Password Invalid!')
            username = input('Enter your username: ')
            old_password = getpass('Enter your old password: ')

        password_new = getpass('Enter your new password: ')
        password_new_repeat = getpass('Repeat your new password: ')

        while password_new != password_new_repeat:
            print('New password do not match!')
            password_new = getpass('Enter your new password: ')
            password_new_repeat = getpass('Repeat your new password: ')

        data['username'] = username
        data['password'] = password_new

        JsonManager().update_json(self.path_data, data)
        print('Update successfully!')


    def logging_in(self, data):
        print('### Logging in ###')

        username = input('Enter your username: ')
        while username != data['username']:
            print('Username Invalid!')
            username = input('Enter your username: ')

        senha = getpass('Enter your password: ')
        while senha != data['password']:
            print('Username Invalid!')
            senha = getpass('Enter your password: ')

        print('Logado!')
        self.home(data)


    def main(self):

        data = JsonManager().read_json(self.path_data)
        if data:
            try:
                self.logging_in(data)
            except KeyboardInterrupt:
                print('\nCancelado!')
        else:
            self.sign_in()

if __name__ == '__main__':
    jl = JLogin()
    jl.main()



