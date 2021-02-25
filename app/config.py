class Config:
    '''
    General configaration parent class
    '''
    pass
class ProdConfig(Config):
    '''
    Production configaration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configaration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG=True