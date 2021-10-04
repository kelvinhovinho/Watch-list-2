from logging import debug


class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    production configuration child class
    Args:
        config: the parent configuration clas with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration cettings
    '''
    DEBUG = True