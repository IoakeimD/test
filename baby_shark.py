def print_doo():
    return " doo" * 6


def baby_shark():
    sharks = ["Baby", "Mommy", "Daddy", "Grandma", "Grandpa"]
    for shark in sharks:
        for index in range(3):
            print(shark + " shark,%s" %(print_doo()))
        print(shark + " shark\n")
    for index in range(3):
        print("Let's go hunt,%s" %(print_doo()))
    print("Let's go hunt!\n")
    for index in range(3):
        print("Run away,%s" %(print_doo()))
    print("Run away (ah!)\n")
    for index in range(3):
        print("Safe at last,%s" %(print_doo()))
    print("Safe at last (phew)\n")
    for index in range(3):
        print("It's the end,%s" %(print_doo()))
    print("It's the end\n")


baby_shark()
