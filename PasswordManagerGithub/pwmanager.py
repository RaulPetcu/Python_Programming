# Realizați un utilitar care să managerieze o listă de parole sub forma unui fișier, care poate fi
# actualizat (insert / update / delete), înăuntrul căruia parolele sunt criptate (cu o parolă master
# ce va trebui introdusă la deschiderea fișierului).

# INPUT:
# pwmanager.py <master_password> -<operation> <website> <username> <password>
# pwmanager.py <master_password> -add gmail.com johndoe@google.com cookie123
# pwmanager.py <master_password> -get gmail.com
# pwmanager.py <master_password> -remove gmail.com
# pwmanager.py <master_password> -list

# OUTPUT:
# pwmanager.db

from functions import command_filter
import sys


def main():
    master_password = sys.argv[1]

    if master_password == "asd":
        list_of_args = [sys.argv[i] for i in range(1, len(sys.argv))]
        command_filter(list_of_args)

    else:           
        pass

main()