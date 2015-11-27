def hello_from_a_package():
    print('Hello from a package!')


def _secret_hello_from_a_package():
    print('Secret Hello!')


def calls_secret_hello():
    _secret_hello_from_a_package()
