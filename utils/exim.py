# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv


def save_socialdata_as_list(social_data, fieldname, filepath):
    with open(filepath, 'wb') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[fieldname])
        writer.writeheader()
        for entity in social_data:
            writer.writerow({fieldname: entity.encode('utf-8')})
