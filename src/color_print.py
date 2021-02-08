from colorama import init, Fore, Back, Style
import time


class Colored(object):
    # 前景色:红色 背景色:默认
    def red(self, s):
        return Fore.LIGHTRED_EX + s + Fore.RESET

    # 前景色:绿色 背景色:默认
    def green(self, s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET

    # 前景色:黄色 背景色:默认
    def yellow(self, s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET

    # 前景色:蓝色 背景色:默认
    def blue(self, s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET

    # 前景色:白色 背景色:默认
    def white(self,s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET

    # 前景色:洋红色 背景色:默认
    def magenta(self, s):
        return Fore.LIGHTMAGENTA_EX + s + Fore.RESET

    # 前景色:青色 背景色:默认
    def cyan(self, s):
        return Fore.LIGHTCYAN_EX + s + Fore.RESET


color = Colored()

def print_flush(info):
    print(
        color.white("[")
        + color.blue(time.strftime("%H:%M:%S"))
        + color.white("]")
        + color.white("[")
        + color.green("INFO")
        + color.white("] ")
        + info, end="\r", flush=True
    )



def print_flush_two(info):
    print(
        "\r",
        color.white("[")
        + color.blue(time.strftime("%H:%M:%S"))
        + color.white("]")
        + color.white("[")
        + color.green("INFO")
        + color.white("] ")
        + info, end=""
    )


def print_info(info):
    print(
        color.blue(time.strftime("%Y-%m-%d") + ' ')
        + color.blue(time.strftime("%H:%M:%S"))
        + color.white(" [")
        + color.green("INFO")
        + color.white("]")
        + color.white(' - ')
        + color.green(info)
    )


def print_error(info):
    print(
        color.blue(time.strftime("%Y-%m-%d") + ' ')
        + color.blue(time.strftime("%H:%M:%S"))
        + color.white(" [")
        + color.red("ERRO")
        + color.white("]")
        + color.white(' - ')
        + color.red(info)
    )


def print_warn(info):
    print(
        color.blue(time.strftime("%Y-%m-%d") + ' ')
        + color.blue(time.strftime("%H:%M:%S"))
        + color.white(" [")
        + color.yellow("WARN")
        + color.white("]")
        + color.white(' - ')
        + color.yellow(info)
    )


def print_input(info):
    result = input(
        color.blue(time.strftime("%Y-%m-%d") + ' ')
        + color.blue(time.strftime("%H:%M:%S"))
        + color.white(" [")
        + color.green("INFOR")
        + color.white("]")
        + color.white(' - ')
        + color.green(info)
    )
    return result


def print_msg():
    print(color.cyan('\nThis is an integrated information collection tool'))
    msg1 = ''' _          __                                            
(_) _ __   / _|  ___   ___   ___  __ _  _ __    ___  _ __ '''
    print(color.cyan(msg1))
    msg2 = '''| || '_ \ | |_  / _ \ / __| / __|/ _` || '_ \  / _ \| '__|      Version: 0.2'''
    print(color.yellow(msg2))
    msg3 = '''| || | | ||  _|| (_) |\__ \| (__| (_| || | | ||  __/| |         Author:CMACCKK'''
    print(color.magenta(msg3))
    msg4 = '''|_||_| |_||_|   \___/ |___/ \___|\__,_||_| |_| \___||_|         Email: emailforgty@163.com
'''
    print(color.blue(msg4))
    msg5 = 'Thanks for: PROTECT Elinpf mooneee 0xss kuaiyulong liszero godlike008\n'
    print(color.red(msg5))

