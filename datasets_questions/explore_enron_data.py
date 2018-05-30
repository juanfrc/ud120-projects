#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

    ('METTS MARK', {'salary': 365788, 'to_messages': 807, 'deferral_payments': 'NaN',
    'total_payments': 1061827, 'exercised_stock_options': 'NaN', 'bonus': 600000,
    'restricted_stock': 585062, 'shared_receipt_with_poi': 702,
    'restricted_stock_deferred': 'NaN', 'total_stock_value': 585062,
    'expenses': 94299, 'loan_advances': 'NaN', 'from_messages': 29,
    'other': 1740, 'from_this_person_to_poi': 1, 'poi': False, 'director_fees': 'NaN',
    'deferred_income': 'NaN', 'long_term_incentive': 'NaN',
    'email_address': 'mark.metts@enron.com', 'from_poi_to_this_person': 38})

"""

import pickle
# import pdb

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'Size of Dataset ' + str(len(enron_data))
# pdb.set_trace()
print 'Features por person ' + str(len(enron_data.items()[0][1]))
print '# of POIs in Dataset' + str(len(enron_data.items()[0][1]))
