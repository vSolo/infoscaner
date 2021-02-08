import json

def http_to_none(http_url):
    no_http_url = http_url.replace('http://', '')
    no_https_url = no_http_url.replace('https://', '')
    if no_https_url.endswith('/'):
        return_url = no_https_url[:-1]
    else:
        return_url = no_https_url
    return return_url


def get_json_info(json_data):
    result = ''
    for k, v in json_data.items():
        result += k + ': ' + v + '\n'
    return result


def list_merge(list1, list2):
    result = []
    for i in list1:
        result.append(i)
    for j in list2:
        result.append(j)
    tmp_set = set(result)
    tmp_list = list(tmp_set)
    return tmp_list