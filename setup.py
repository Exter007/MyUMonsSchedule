import hashlib
import os.path

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
        input_mat()

    if not confirm_input(_mat):
        input_mat()

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
        input_password()

    return _pswd


def final_confirmation(_mat, _pswd):
    print("===================================")
    print("Here are your UMons informations :")
    print(f"Matricule   : {_mat}")
    print(f"E-mail      : {_mat}@umons.ac.be")
    print(f"Password    : {_pswd}")
    if not confirm(input("Are these informations correct ? (y/n) >> ")):
        print("We will re-run the wizard in order to change your information.")
        setup()


def setup():
    _mat = input_mat()
    _pswd = input_password()
    final_confirmation(_mat, _pswd)
    return _mat, _pswd


if __name__ == "__main__":
    print("Welcome to the MyUMonsSchedule setup wizard.")
    print(cwd)
    mat, pswd = setup()
    encrypted_pswd = hashlib.sha256(pswd.encode()).hexdigest()

    with open("config/login.txt", "w+") as config_file:
        config_file.truncate()
        # config_file.write(encrypted_pswd)
        config_file.write(f"{mat}@umons.ac.be\n{pswd}")
