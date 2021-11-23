import os.path
import encrypt
import pickle

path = os.path.realpath(__file__)[:-8]
login_file_name = "login"


def confirm_input(_input):
    """
    Asks the user to confirm the given parameter. Re-runs the method until the user's response is either 'y' or 'n'.
    :param _input: The input the user has to confirm
    :return: True if the user confirmed the input, False if the user did not confirm the input
    """
    choice = input(f"Do you confirm {_input} ? (y/n) >> ")
    return confirm(choice)


def confirm(_input):
    if _input.strip().lower() == "y":
        return True
    elif _input.strip().lower() == "n":
        return False
    else:
        print("Answer unreadable, please try again.")
        return confirm_input(_input)


def check_matricule_format(_input):
    """
    Checks if the parameter is a correctly formatted matricule (6 characters in length and only contains numbers)
    :param _input: The input to check the format of
    :return: True if the input is a correctly formatted matricule
    """
    return len(_input) == 6 and _input.isnumeric()


def input_mat():
    """
    Asks for matricule, then checks if the matricule is correctly formatted. If so, asks for confirmation and returns
    the matricule if the user confirms its input. If the matricule is not correctly formatted, or if the user does not
    confirm its input, re-run the method.
    :return: The matricule (String) if correctly formatted and confirmed by the user
    """
    _mat = input("Please enter your UMons matricule >> ")

    if not check_matricule_format(_mat):
        print("Incorrect matricule format.")
        return input_mat()

    if not confirm_input(_mat):
        return input_mat()

    return _mat


def input_password():
    """
    Asks for password, asks for confirmation and returns the password if the user confirms its input.
    If the matricule is not correctly formatted, or if the user does not
    confirm its input, re-run the method.
    :return: The matricule (String) if correctly formatted and confirmed by the user
    """
    _pswd = input("Please enter your UMons password >> ")

    if not confirm_input(_pswd):
        return input_password()

    return _pswd


def final_confirmation(_mat, _pswd):
    print("===================================")
    print("Here are your UMons informations :")
    print(f"Matricule   : {_mat}")
    print(f"E-mail      : {_mat}@umons.ac.be")
    print(f"Password    : {_pswd}")
    # TODO : bug here if we have a wrong input for confirmation
    if not confirm(input("Are these informations correct ? (y/n) >> ")):
        print("We will re-run the wizard in order to change your information.")
        setup()
    return True


def setup():
    _mat = input_mat()
    _pswd = input_password()
    final_confirmation(_mat, _pswd)
    return _mat, _pswd


def encrypt_login(mat_, pswd_, file):
    with open(file, "wb") as f:
        f.truncate()
        pickle.dump([mat_, pswd_], f)


def retrieve_login(file):
    with open(file, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    print("Welcome to the MyUMonsSchedule setup wizard.")
    mat, pswd = setup()

    # how to generate public and private keys
    # private_key = encrypt.generate_private_key()
    # public_key = encrypt.generate_public_key(private_key)
    #
    # how to save public and private keys to files
    # encrypt.save_public_key("./keys/public_key.pem", public_key)
    # encrypt.save_private_key("./keys/private_key.pem", private_key)

    public_key = encrypt.read_public_key("./keys/public_key.pem")
    private_key = encrypt.read_private_key("./keys/private_key.pem")

    encrypted_mat = encrypt.encrypt(mat.encode(), public_key)
    encrypted_pswd = encrypt.encrypt(pswd.encode(), public_key)

    encrypt_login(encrypted_mat, encrypted_pswd, "./config/login.idd")

    # how to get encrypted mat and encrypted pswd from the login.idd file
    # read_mat, read_pswd = retrieve_login("./config/login.idd")
    #
    # how to get decrypted mat and decrypted pswd from the login.idd file
    # read_data = retrieve_login("./config/login.idd")
    # read_mat, read_pswd = encrypt.decrypt(read_data[0], private_key), encrypt.decrypt(read_data[1], private_key)
