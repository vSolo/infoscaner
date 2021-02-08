import subprocess
from src.color_print import *
from src.read_file import *
import requests
from multiprocessing import Pool
from tqdm import tqdm
from src.get_user_agent import *



def oneforall(target):
    ONEFORALL_OUTPUT_PATH = './output/oneforall.txt'
    CMD_STR = "python3 ./OneForAll-master/oneforall.py --target {target} --path={ONEFORALL_OUTPUT_PATH} run".format(
        ONEFORALL_OUTPUT_PATH=ONEFORALL_OUTPUT_PATH, target=target)
    print_info('使用OneForAll扫描  Command: ' + color.yellow(CMD_STR))
    CMD = CMD_STR.split(' ')
    rsp = subprocess.Popen(CMD)
    rsp.communicate()


def get_oneforall_info(info):  # 对oneforall查询到的子域名去重
    l = []
    for i in info:
        tmp = i.strip().split(',')
        l.append(tmp[5])
    result = set(l)
    return_list = list(result)
    return return_list


def get_subdomain(url, output=None):
    oneforall(url)  # Oneforall扫描
    info = read_file('./output/oneforall.txt')
    oneforall_url = get_oneforall_info(info)  # 子域名列表
    print_info('对子域名可访问性进行扫描')
    alive_url = judge_get_addressable_url(oneforall_url)
    if output == None:
        Table = PrettyTable(['Subdomain'])
        for subdomain_url in alive_url:
            Table.add_row([subdomain_url])
        print(Table)
    else:
        f = open(output, 'w')
        for subdomain_url in alive_url:
            f.write(subdomain_url + '\n')
        f.close()



def request_get_url(pool_get_url):  # 判断url是否可以访问
    try:
        r = requests.request(method='GET', url=pool_get_url, headers=get_user_agent(), timeout=(3, 7)).status_code
        if r == 200:
            return 1, pool_get_url
        else:
            return 0, pool_get_url
    except:
        return 0, pool_get_url,


def judge_get_addressable_url(sub_list):  # 判断GET可访问的域名
    scan_url_list = []
    alive_url = []
    for line in sub_list:
        if line.startswith('https://'):
            tmp_url = line.replace('https://', 'http://')
        elif line.startswith('http://'):
            tmp_url = line
        else:
            tmp_url = 'http://' + line
        scan_url_list.append(tmp_url)
    # print(scan_url_list)
    thread_count = 10
    print_info('使用 ' + str(thread_count) + ' 线程')
    with Pool(10) as p:
        pool_result = list(tqdm(p.imap(request_get_url, scan_url_list), total=len(scan_url_list)))
    for result in pool_result:
        if result[0] == 1:
            alive_url.append(str(result[1]).replace('http://', ''))
    return alive_url


