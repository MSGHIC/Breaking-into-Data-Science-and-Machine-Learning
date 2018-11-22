# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:36:21 2018

@author: MSG
"""

"""Returns 2 character country code"""

#Pygal uses two-letter codes
from pygal.maps.world import COUNTRIES
"""Pygal’s country codes are stored in a module called i18n, short for
internationalization. The dictionary COUNTRIES contains the two-letter country
codes as keys and the country names as values. """


def get_country_code(Country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == Country_name:
            return code
    #if country not found , return none
    return None
