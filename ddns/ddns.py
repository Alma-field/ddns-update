class DDNS():
    def __init__(self):
        from os import environ
        self.user_id = environ['USER_ID']
        self.password = environ['PASSWORD']

    def updateip(self):
        raise NotImplementedError('NotImplementedError')
