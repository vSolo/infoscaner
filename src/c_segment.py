from src.color_print import *
import requests
import re
from prettytable import PrettyTable
from src.get_user_agent import *
import json
from pprint import pprint
from src.config import *
from src.other_func import get_json_info


def c_segment_search(c_segment_url, write=False, output=None):
    ip_list = PrettyTable(['Searching', 'Result'])
    print_info('查询旁站和C段')
    url = 'http://webscan.cc/site_'
    result_url = url + c_segment_url + '/'
    # print(result_url)
    response = requests.get(result_url, headers=get_user_agent(), verify=False).text
    domain_ip_re = r'<h1>(.*?)</h1>'
    domain_ip = re.findall(domain_ip_re, response, re.S)[0]
    company_re = r'<h2>(.*?)</h2>'
    company = re.findall(company_re, response, re.S)[0]
    container_re = r'<td><p>(.*?)</p></td>'
    container = re.findall(container_re, response, re.S)[1]
    if write == False:
        ip_list.add_row(['IP地址', domain_ip])
        ip_list.add_row(['公司', company])
        ip_list.add_row(['站点容器', container])
        title_re = r'<li class="J_link"><span>(.*?)</span>'
        title = re.findall(title_re, response)
        domain_result_re = r'target="_blank">(.*?)</a></li>'
        domain_result = re.findall(domain_result_re, response)
        # print(title)
        # print(domain_result)
        print_info('输出站点信息表')
        time.sleep(0.5)
        print(ip_list)
        same_table = PrettyTable(['title', 'url'])
        for i in range(len(title)):
            list_domain = []
            list_domain.append(title[i])
            list_domain.append(domain_result[i])
            # print(list_domain)
            same_table.add_row(list_domain)
        print_info('同服IP站点列表')
        time.sleep(0.5)
        print(same_table)
    else:
        f = open(output, 'w')
        f.write(c_segment_url + '\n\n')
        f.write('IP地址  ' + domain_ip + '\n')
        f.write('公司  ' + company + '\n')
        f.write('站点容器  ' + container + '\n\n\n')
        title_re = r'<li class="J_link"><span>(.*?)</span>'
        title = re.findall(title_re, response)
        domain_result_re = r'target="_blank">(.*?)</a></li>'
        domain_result = re.findall(domain_result_re, response)
        for i in range(len(title)):
            f.write(title[i] + '  ' + domain_result[i] + '\n')
        print_info('成功获取C段和旁站信息')
        print_info('保存路径为 ' + color.yellow(output))
        f.close()


def get_access_token(username, password):
    data = {
        'username': username,
        'password': password
    }
    json_data = json.dumps(data)
    try:
        r = requests.post(url=login_url, data=json_data)
        r_decoded = json.loads(r.text)
        access_token = r_decoded['access_token']
        return access_token
    except Exception as e:
        print_error('username or password is wrong, please try again')
        return



def Zoomeye_search_Cseg(access_token, search_grammar, output=None):
    headers = {
        'Authorization': 'JWT ' + access_token
    }
    url = 'https://api.zoomeye.org/host/search?query={SEARCH_GRAMMAR}'.format(SEARCH_GRAMMAR=search_grammar)
    response = requests.get(url=url, headers=headers).content.decode('utf-8')
    c_seg_json = json.loads(response)
    # pprint(c_seg_json)
    if output == None:
        Search_table = PrettyTable(['扫描信息', 'result'])
        Search_table.add_row(['扫描结果', c_seg_json['total']])
        Search_table.add_row(['可获取的结果', c_seg_json['available']])
        Search_table.add_row(['facets', c_seg_json['facets']])
        print(Search_table)
        for info in c_seg_json['matches']:
            # pprint(info)
            Table = PrettyTable(['Geoinfo', 'result'])
            print_info('获取' + info['ip'] + '端口为' + str(info['portinfo']['port']) + '的信息')
            try:

                Table.add_row(['IP', info['ip']])
            except:
                pass
            try:
                Table.add_row(['城市', get_json_info(info['geoinfo']['city']['names'])])
            except:
                pass
            try:
                Table.add_row(['时间', info['timestamp']])
            except:
                pass
            try:
                Table.add_row(['rdns_new', info['rdns_new']])
            except:
                pass
            try:
                Table.add_row(['protocol', get_json_info(info['protocol'])])
            except:
                pass
            try:
                Table.add_row(['app', info['portinfo']['app']])
            except:
                pass
            try:
                Table.add_row(['device', info['portinfo']['device']])
            except:
                pass
            try:
                Table.add_row(['extrainfo', info['portinfo']['extrainfo']])
            except:
                pass
            try:
                Table.add_row(['hostname', info['portinfo']['hostname']])
            except:
                pass
            try:
                Table.add_row(['os', info['portinfo']['os']])
            except:
                pass
            try:
                Table.add_row(['port', info['portinfo']['port']])
            except:
                pass
            try:
                Table.add_row(['service', info['portinfo']['service']])
            except:
                pass
            try:
                Table.add_row(['title', info['portinfo']['title']])
            except:
                pass
            try:
                Table.add_row(['version', info['portinfo']['version']])
            except:
                pass
            print(Table)
            time.sleep(1)
        print_info('信息输出完毕')
    else:
        print_info('准备将查询信息写入到' + color.yellow(output))
        try:
            f = open(output, 'w')
            f.write(response)
            f.close()
        except:
            print_error('写入文件路径错误，请检查路径')

