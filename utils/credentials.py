from faker import Faker

class Credentials:
    """
    Data used to enter the page.
    """
    USERNAME = 'testuserintern@mail.ru'
    PASSWORD = 'db1J7SgYbeNC'
    FAKE_REPOSITORY_NAME = Faker().domain_name()
