"""
Some configuration values used everywhere
"""

import os
from glob import glob

# The numerals permitted in the vehicle registration plate
NUMERALS = [
    u"০",
    u"১",
    u"২",
    u"৩",
    u"৪",
    u"৫",
    u"৬",
    u"৭",
    u"৮",
    u"৯",
]

# The letters permitted in the vehicle registration plate
# + appended some letters from district names
LETTERS = [
    u"অ",
    u"ই",
    u"উ",
    u"এ",
    u"ক",
    u"খ",
    u"গ",
    u"ঘ",
    u"ঙ",
    u"চ",
    u"ছ",
    u"জ",
    u"ঝ",
    u"ত",
    u"থ",
    u"ঢ",
    u"ড",
    u"ট",
    u"ঠ",
    u"দ",
    u"ধ",
    u"ন",
    u"প",
    u"ফ",
    u"ব",
    u"ভ",
    u"ম",
    u"য",
    u"র",
    u"ল",
    u"শ",
    u"স",
    u"হ",

    u"ণ",
    u"ষ",
    u"ঞ",
    u"ও",
]

# all city name images
CITIES = [
    file for file in glob('city' + '/**/*.bmp')
]

# Reference https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Bangladesh

# fonts - [(location, size)]
UNICODE_FONTS = [
    #("fonts/bangla.ttf", 72),
    ("fonts/siyamrupali.ttf", 38),
    ("fonts/solaimanlipi.ttf", 46),
    ("fonts/sutonnyomj.ttf", 48)
]

# dimension of each image
IMAGE_DIM = (28, 28)

# ratio between training and testing data
DATASET_RATIO = 0.85  # training data

# output directories
DIGITS_PATH = os.path.join('dataset', 'digits')
LETTERS_PATH = os.path.join('dataset', 'letters')
CITY_PATH = os.path.join('dataset', 'city')
