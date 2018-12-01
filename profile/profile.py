import os
import configparser
import ast


class Profile(object):
    @staticmethod
    def get_path(chat_id):
        return os.path.join(os.path.normpath("."), "{}.ini".format(chat_id))

    def __init__(self, config, chat_id):
        self.config = config
        self.chat_id = chat_id

    def save(self):

        with open(self.__class__.get_path(chat_id=self.chat_id), 'w') as configfile:
            self.config.write(configfile)
        print("Created new config file")

    @classmethod
    def load_profile(cls, chat_id):
        config = configparser.ConfigParser()
        config.read(cls.get_path(chat_id=chat_id))
        config = cls._from_file(config)
        return config

    @classmethod
    def _from_file(cls, config):
        for k, v in config['basic'].items():
            config['basic'][k] = config['basic'].getint(v)

        config['data']['accounts'] = ast.literal_eval(config['data']['accounts'])
        for k, v in config['progress'].items():
            config['progress'][k] = config['progress'].getint(v)

        init = config['parent'].getboolean('init')
        if not init:
            config['parent']['init'] = True
            config['parent']['profile'] = config

        return config

    @classmethod
    def create(cls, chat_id):
        cls._delete_old_profile(chat_id=chat_id)
        # create new profile
        config = configparser.ConfigParser()
        config = cls._set(config, cls._default())
        return cls(config=config, chat_id=chat_id)

    @classmethod
    def _set(cls, config, profile):
        for section, options in profile.items():
            config[section] = {}
            print(section)
            for k, v in options.items():
                config[section][k] = v

        return config

    @classmethod
    def _delete_old_profile(cls, chat_id):
        if os.path.exists(cls.get_path(chat_id=chat_id)):
            # delete old profile
            os.remove(cls.get_path(chat_id=chat_id))

    @classmethod
    def _default(cls):
        config = {
            'basic': {
                'message_id': 0,
                'age_group': 0,
                'origin': 0,
                'sex': 0,
                'place_of_residence': 0
            },
            'data': {
                'accounts': []
            },
            'parent': {
                'init': False,
                'profile': None
            },
            'progress': {
                'stage_id': 0,
                'story_id': 0,
                'event_id': 0
            }
        }
        return config
