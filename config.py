# -*- coding: utf-8 -*-
import os

'''
    Used for finding environment variables through configuration
    if a default is not given, the site will raise an exception
'''
def get_env_variable(var_name, default=-1):
    try:
        return os.environ[var_name]
    except KeyError:
        if default != -1:
            return default
        error_msg = "Set the %s os.environment variable" % var_name
        raise Exception(error_msg)

''' Default debugging to False '''
DEBUG = not get_env_variable("DATAUSA_PRODUCTION", False)
