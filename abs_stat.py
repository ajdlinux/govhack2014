import os
import urllib
import urllib2
import json
import csv
from settings import *
from db import *

class ABSAPIError(Exception):
    pass

def abs_get(get_dict):
    base = "http://stat.abs.gov.au/itt/query.jsp?"
    get_dict['format'] = 'json'
    args = urllib.urlencode(get_dict)
    if not os.path.exists('cache/%s' % args):
        print "Retrieving from: %s" % (base+args)
        f = urllib2.urlopen(base + args)
        cache_file = open('cache/%s' % args, 'w')
        cache_file.write(f.read())
        f.close()
        cache_file.close()
    f = open('cache/%s' % args)
    data = json.load(f)
    f.close()
    return data

def abs_get_csv(table, field):
    with open(os.path.join(ABS_CSV_PATH, "2011Census_%s_ACT_SA2_short.csv" % table)) \
         as f:
        r = csv.DictReader(f)
        result = {int(row['region_id']): float(row[field]) for row in r}
    for exclusion in ABS_EXCLUSION:
        try:
            del result[exclusion]
        except:
            pass
    return result

# call query and return as dict from region (int) to observation (float)
def abs_get_parse(get_dict):
    raw = abs_get(get_dict)
    abs_data = dict()
    for a in raw['series']:
        region = -1
        for b in a['concepts']:
            if b['name'] == 'REGION':
                region = int(b['Value'])
                break
        if region == -1:
            print 'Failed to find REGION code'
            raise ABSAPIError('No REGION code found')
        abs_data[region] = float(a['observations'][0]['Value'])
    for exclusion in ABS_EXCLUSION:
        try:
            del abs_data[exclusion]
        except:
            pass
    return abs_data

def get_concepts(datasetid):
    return abs_get({'method' : 'GetDatasetConcepts', 'datasetid' : datasetid})['concepts']

def get_codes(datasetid, concept):
    return abs_get({'method' : 'GetCodeListValue', 'datasetid' : datasetid, 'concept' : concept})['codes']

def get_all_codes(datasetid):
    concepts = get_concepts(datasetid)
    codes = {}
    for concept in concepts:
        codes[concept] = get_codes(datasetid, concept)
    return codes

def pretty_print(data):
    print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

def add_sa2(dict):
    dict['or'] = 'REGION'
    if 'and' in dict:
        dict['and'] += ','
    else:
        dict['and'] = ''
    dict['and'] += 'STATE.8,REGIONTYPE.SA2'

# usual place of residence (probably)
def get_population_data():
    if ABS_CSV:
        return abs_get_csv('B03', 'Total_Total')
    else:
        d = dict()
        add_sa2(d)
        d['method'] = 'GetGenericData'
        d['datasetid'] = 'ABS_CENSUS2011_B03'
        d['and'] += ',MEASURE.TT,POUR.TOT'
        return abs_get_parse(d)

# usual place of residence as density
def get_population_density():
    counts = get_population_data()
    db = DB()
    cur = db.cursor()
    cur.execute("select sa2_main, area_sqkm from sa2 where sa2_main like '8%'")
    density = {}
    for row in cur:
        region = int(row[0])
        if row[1] is not None and region in counts:
            density[region] = counts[region] / float(row[1])
    return density

# median age of persons by SA2
def get_age_data():
    if ABS_CSV:
        return abs_get_csv('B02', 'Median_age_persons')
    else:
        d = dict()
        add_sa2(d)
        d['method'] = 'GetGenericData'
        d['datasetid'] = 'ABS_CENSUS2011_B02'
        d['and'] += ',MEASURE.MAGE'
        return abs_get_parse(d)

# median person income of persons per week by SA2
def get_income_data():
    if ABS_CSV:
        return abs_get_csv('B02', 'Median_Tot_prsnl_inc_weekly')
    else:
        d = dict()
        add_sa2(d)
        d['method'] = 'GetGenericData'
        d['datasetid'] = 'ABS_CENSUS2011_B02'
        d['and'] += ',MEASURE.MIPI'
        return abs_get_parse(d)

# average persons per household by SA2
def get_household_data():
    if ABS_CSV:
        return abs_get_csv('B02', 'Average_household_size')
    else:
        d = dict()
        add_sa2(d)
        d['method'] = 'GetGenericData'
        d['datasetid'] = 'ABS_CENSUS2011_B02'
        d['and'] += ',MEASURE.AHS'
        return abs_get_parse(d)

# distance to closest school by SA2
def get_schools_data():
    db = DB()
    cur = db.cursor()
    cur.execute("select sa2_main, school_distance from sa2 where sa2_main like '8%';")
    result = {}
    for row in cur:
        try:
            result[int(row[0])] = float(row[1])
        except:
            pass # this is best error handling
    #print result
    for exclusion in ABS_EXCLUSION:
        try:
            del abs_data[exclusion]
        except:
            pass
    return result

# distance to closest hospital by SA2
def get_hospitals_data():
    db = DB()
    cur = db.cursor()
    cur.execute("select sa2_main, hospital_distance from sa2 where sa2_main like '8%';")
    result = {}
    for row in cur:
        try:
            result[int(row[0])] = float(row[1])
        except:
            pass # this is best error handling
    #print result
    for exclusion in ABS_EXCLUSION:
        try:
            del abs_data[exclusion]
        except:
            pass
    return result


data_funcs = {'population': get_population_density,
              'age': get_age_data,
              'income': get_income_data,
              'household': get_household_data,
              'schools': get_schools_data,
              'hospitals': get_hospitals_data}

def get_scores(params):
    scores = {}
    for dataset, value_rating, weighting in params:
        values = data_funcs[dataset]()
        
        # Normalise
        value_max = max(values.values())
        value_min = min(values.values())
        values = {k: (v - value_min) / (value_max - value_min) for k, v in values.items()}
        for k, v in values.items():
            scores[k] = scores.get(k, 0.0) + \
                        (1 - (1.0 - abs(v - value_rating / 6.0)) \
                         if dataset in VALUE_REVERSE else \
                         (1.0 - abs(v - value_rating / 6.0))) * weighting
    for exclusion in ABS_EXCLUSION:
        try:
            del scores[exclusion]
        except:
            pass
    return scores # we don't bother normalising, that can be done later
