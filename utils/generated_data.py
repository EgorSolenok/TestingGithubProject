from faker import Faker


class GeneratedData(object):
    LAST_GENERATED_NAME = ''

    @staticmethod
    def generate_new_name():
        new_fake_name = Faker().domain_name()
        GeneratedData.LAST_GENERATED_NAME = new_fake_name
        return new_fake_name
