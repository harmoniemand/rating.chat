import os
from configparser import ConfigParser
import ast
import copy
import pickle


class Profile(object):
    @staticmethod
    def get_path(chat_id):
        return os.path.join(os.path.normpath("."), "{}.pickle".format(chat_id))

    @classmethod
    def save(cls,profile,chat_id):
        return cls._dump_pickle(chat_id,profile)

    @classmethod
    def save1(cls, profile, chat_id):
        parser = ConfigParser()
        parser = cls._set(parser=parser, profile=profile)
        with open(cls.get_path(chat_id=chat_id), 'w') as configfile:
            parser.write(configfile)
        print("Created new config file")

    @classmethod
    def load(cls, chat_id):
        return cls._load_pickle(chat_id)

    @classmethod
    def load1(cls, chat_id):
        parser = ConfigParser()
        parser.read(cls.get_path(chat_id=chat_id))
        profile = cls._from_file(parser)
        return profile

    @classmethod
    def _from_file(cls, config):
        old_profile = cls._convert(config)

        profile = {}
        for k in old_profile:
            profile[k] = {}

        for k, v in old_profile['basic'].items():
            profile['basic'][str(k)] = old_profile['basic'][k]

        profile['data']['accounts'] = old_profile['data']['accounts']
        for k, v in old_profile['progress'].items():
            profile['progress'][str(k)] = old_profile['progress'][k]

        profile['parent']['profile'] = copy.deepcopy(old_profile)
        return profile

    @classmethod
    def _convert(cls, config):
        profile = {}
        for k in config:
            if k is not 'DEFAULT':
                profile[k] = {}

        for k, v in config['basic'].items():
            profile['basic'][str(k)] = config['basic'].getint(k)

        profile['data']['accounts'] = ast.literal_eval(config['data']['accounts'])
        for k, v in config['progress'].items():
            profile['progress'][str(k)] = config['progress'].getint(k)

        profile['parent']['profile'] = copy.deepcopy(ast.literal_eval(config['parent']['profile']))
        return profile

    @classmethod
    def create(cls, chat_id):
        cls._delete_old_profile(chat_id=chat_id)
        # create new profile
        return cls._default(chat_id)

    @classmethod
    def _set(cls, parser, profile):
        for section, options in profile.items():
            parser.add_section(section)
            for k, v in options.items():
                parser.set(str(section), str(k), str(v))

        # parser.set('parent', 'init', str(False))

        return parser

    @classmethod
    def _delete_old_profile(cls, chat_id):
        if os.path.exists(cls.get_path(chat_id=chat_id)):
            # delete old profile
            os.remove(cls.get_path(chat_id=chat_id))

    @classmethod
    def _dump_pickle(cls,chat_id, confing):
        with open(cls.get_path(chat_id) ,"wb") as f:
            pickle.dump(confing, f)

    @classmethod
    def _load_pickle(cls, chat_id):
        with open(cls.get_path(chat_id), "rb") as f:
            return pickle.load(f)

    @classmethod
    def _default(cls, chat_id):
        config = {
            'basic': {
                'chat_id' : chat_id,
                'message_id': 0,
                'name' : '',
                'age_group': 0,
                'origin': 0,
                'sex': 0,
                'place_of_residence': 0
            },
            'data': {
                'accounts': []
            },
            'parent': {
                #'init': False,
                'profile': None
            },
            'progress': {
                'stage_id': 0,
                'event_id': 'start',
            },

                'event_list': {
                }

        }
        return config
