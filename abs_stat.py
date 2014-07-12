import urllib
import urllib2
import json

def abs_get(get_dict):
    base = "http://stat.abs.gov.au/itt/query.jsp?"
    get_dict['format'] = 'json'
    args = urllib.urlencode(get_dict)
    f = urllib2.urlopen(base + args)
    data = json.load(f)
    f.close()
    return data

class abs_api_error(Exception):
    pass

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
            raise abs_api_error('No REGION code found')
        abs_data[region] = float(a['observations'][0]['Value'])
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
def get_pop_data():
    d = dict()
    add_sa2(d)
    d['method'] = 'GetGenericData'
    d['datasetid'] = 'ABS_CENSUS2011_B03'
    d['and'] += ',MEASURE.TT,POUR.TOT'
    return abs_get_parse(d)

# median age of persons by SA2
def get_age_data():
    d = dict()
    add_sa2(d)
    d['method'] = 'GetGenericData'
    d['datasetid'] = 'ABS_CENSUS2011_B02'
    d['and'] += ',MEASURE.MAGE'
    return abs_get_parse(d)

# median person income of persons per week by SA2
def get_income_data():
    d = dict()
    add_sa2(d)
    d['method'] = 'GetGenericData'
    d['datasetid'] = 'ABS_CENSUS2011_B02'
    d['and'] += ',MEASURE.MIPI'
    return abs_get_parse(d)

# average persons per household by SA2
def get_household_data():
    d = dict()
    add_sa2(d)
    d['method'] = 'GetGenericData'
    d['datasetid'] = 'ABS_CENSUS2011_B02'
    d['and'] += ',MEASURE.AHS'
    return abs_get_parse(d)

def get_data_funcs():
    return [('population', get_pop_data), ('age', get_age_data), 
        ('income', get_income_data), ('household', get_household_data)]
