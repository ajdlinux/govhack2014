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