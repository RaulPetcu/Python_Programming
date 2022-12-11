# Realizați un utilitar care să managerieze o listă de parole sub forma unui fișier, care poate fi
# actualizat (insert / update / delete), înăuntrul căruia parolele sunt criptate (cu o parolă master
# ce va trebui introdusă la deschiderea fișierului).

# INPUT:
# pwmanager.py <master_password> -<operation> <website> <username> <password>
# pwmanager.py <master_password> -add gmail.com johndoe@google.com cookie123
# pwmanager.py <master_password> -get gmail.com
# pwmanager.py <master_password> -remove gmail.com
# pwmanager.py <master_password> -update gmail.com new_password
# pwmanager.py <master_password> -list

# OUTPUT:
# pwmanager.db

from cryptography.fernet import Fernet
import os
import zipfile
import pyminizip


def command_filter(args_list):
    master_password = args_list[0]
    operation = args_list[1]
    operation_args = args_list[2:]

    # prepare encryption key
    if os.path.exists('./secure_key.zip') == False: # daca nu exista deja zip-ul
        key = Fernet.generate_key()
        f = open("key.txt", "w+")
        f.write(str(key))
        f.close()

        # create zip
        input = './key.txt'
        output = './secure_key.zip'
        com_lvl = 5
        pyminizip.compress(input, None, output, master_password, com_lvl)

        os.remove("key.txt")


    # filter operations
    if operation == "-add":
        add_operation(operation_args, master_password)
    elif operation == "-remove":
        remove_operation(operation_args)
    elif operation == "-get":
        get_operation(operation_args, master_password)
    elif operation == "-update":
        update_operation(operation_args, master_password)
    elif operation == "-list":
        list_operation(master_password)


def add_operation(op_args, master_password):
    website = op_args[0]
    username = op_args[1]
    real_passwd = op_args[2]
    encrypt_passwd = str(encrypt_password(real_passwd, master_password))
        
    # check for dupliacates
    found = 0
    line_to_find = website + ' ' + username
    with open("my_passwords.txt", "r") as f:
        lines = f.readlines()
        for file_line in lines:
            file_line_words = file_line.split()
            l = file_line_words[0] + ' ' + file_line_words[1] # website + username
            if line_to_find == l:
                print("There is already a username <%s> with a password for the website <%s>" % (
                    username, website))
                found = 1
                break
    if found == 0:
        new_line = website + ' ' + username + ' ' + encrypt_passwd
        f = open("my_passwords.txt", "a")
        f.write(new_line + "\n")
        f.close()
        print("Password successfully added")


def remove_operation(op_args):
    website = op_args[0]
    found = 0

    with open("my_passwords.txt", "r+") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines_words = lines[i].split()
            if lines_words[0] == website:  # am gasit linia de sters
                del lines[i]
                f.seek(0)
                f.truncate()
                f.writelines(lines)
                found = 1
                break

    if found == 1:
        print("Successfully removed")
    else:
        print("Website not found")


def update_operation(op_args, master_password):
    website = op_args[0]
    new_password = op_args[1]
    encrypt_new_password = str(encrypt_password(new_password, master_password))

    found = 0
    with open("my_passwords.txt", "r+") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines_words = lines[i].split()
            if lines_words[0] == website:  # am gasit linia pt update
                new_line = lines_words[0] + " " + \
                    lines_words[1] + " " + encrypt_new_password + "\n"
                lines[i] = new_line

                f.seek(0)
                f.truncate()
                f.writelines(lines)
                found = 1
                break

    if found == 1:
        print("Successfully updated password")
    else:
        print("Website not found")


def get_operation(op_args, master_password):
    website = op_args[0]

    f = open("my_passwords.txt", "r")
    while True:
        line = f.readline()

        if not line:
            break

        line_words = line.split()
        if line_words[0] == website:  # am gasit linia pe care o cautam
            enc_passwd = line_words[2][2:-1]
            real_passwd = str(decrypt_password(enc_passwd, master_password))
            username = line_words[1]
            print("For the website %s you have the username %s and password %s" % (website, username, real_passwd))
            break


def list_operation(master_password):
    with open("my_passwords.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines_words = lines[i].split()
            enc_passwd = lines_words[2][2:-1]
            real_passwd = str(decrypt_password(enc_passwd, master_password))
            print("Website: " + lines_words[0] + " Username: " +
                  lines_words[1] + " Password: " + real_passwd)


def encrypt_password(password, master_password):
    with zipfile.ZipFile('secure_key.zip') as file:
        text_file = file.open(name=file.namelist(
        )[-1], mode='r', pwd=bytes(master_password, 'utf-8'))
        key = text_file.read()

    fernet = Fernet(key[2:-1])

    return fernet.encrypt(password.encode())


def decrypt_password(password, master_password):
    with zipfile.ZipFile('secure_key.zip') as file:
        text_file = file.open(name=file.namelist(
        )[-1], mode='r', pwd=bytes(master_password, 'utf-8'))
        key = text_file.read()

    fernet = Fernet(key[2:-1])

    return fernet.decrypt(bytes(password, 'utf-8')).decode()
