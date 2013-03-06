"""
Load IATI codelists into enums.

IATI define a farly large number of codelists. These are maintained as
CSV files, and the csv files are checked-in as part of the project.
This module build enum types for all the codelists at import time.

For more info on the enum type, see:
http://techspot.zzzeek.org/2011/01/14/the-enum-recipe/
"""

import os
import codecs
import warnings

import unicodecsv as csv
from unidecode import unidecode

from .enum import DeclEnum


def iati_url(name, version="1.0"):
    return ("http://datadev.aidinfolabs.org/data/codelist/" +
            "%s/version/%s/lang/en.csv" % (name, version))

urls = {
    "OrganisationType": iati_url("OrganisationType", version="1.0"),
    "OrganisationRole": iati_url("OrganisationRole", version="1.0"),
    "Country": iati_url("Country", version="1.01"),
    "TransactionType": iati_url("TransactionType", version="1.01"),
    "Currency": iati_url("Currency", version="1.0"),
    "Sector": iati_url("Sector", version="1.0"),
    "Vocabulary": iati_url("Vocabulary"),
}

data_dir = os.path.dirname(__file__)


def ident(name):
    "(Python) identifier for `name`"
    return ''.join(s for s in unidecode(name) if s.isalnum() or s.isspace())\
        .replace(" ", "_").lower()


def codelist_reader(itr):
    headers = next(itr)
    for line in itr:
        yield line[:2]

for name in urls.keys():
    try:
        with codecs.open(os.path.join(data_dir, "%s.csv" % name)) as cl_file:
            reader = codelist_reader(csv.reader(cl_file, encoding="utf-8"))
            enums = {ident(name): (code, name) for code, name in reader}
            globals()[name] = type(name, (DeclEnum,), enums)
    except IOError, exc:
        warnings.warn(str(exc))
