# 导入库
import tkinter as tk
import requests
import psutil
import netifaces

post_data = {  # 上线按钮post方法传入表单
    'user_account': ',0,' + '',
    'user_password': '',
}

# 获取本地Mac地址
def get_mac_address():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                return addr.address

# 获取当前的IP
def get_active_interface_ip():
    gateway_info = netifaces.gateways()
    # 获取默认网关的接口名称
    default_gateway_interface = gateway_info['default'][netifaces.AF_INET][1]
    # 获取默认网关接口的 IPv4 地址
    try:
        ip_address = netifaces.ifaddresses(default_gateway_interface)[netifaces.AF_INET][0]['addr']
        return ip_address
    except (KeyError, IndexError):
        return None

# Mac地址
wlan_user_mac = get_mac_address();
# Ip地址
wlan_user_ip = get_active_interface_ip();

# 地址
post_addr = f"http://10.0.10.252:801/eportal/?c=Portal&a=login&login_method=1" \
            f"&wlan_ac_ip=10.128.255.142&wlan_user_mac={wlan_user_mac}" \
            f"&wlan_user_ip={wlan_user_ip}&user_account={post_data['user_account']}" \
            f"&user_password={post_data['user_password']}"

header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': '10.0.10.252:801',
    'DNT': '1',
    'Referer': 'http://10.0.10.252/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

def click_button():
    # tinker界面上线按钮逻辑函数
    # 进行post请求
    z = requests.get(post_addr, data=post_data, headers=header)
    html = z.content.decode('utf-8')
    print(html)

def quit(x):  # 设置提示框以及退出罗辑
    print(x)
    root = tk.Tk()
    root.geometry('400x50+720+560')  # 大小、位置
    root.configure(bg='white')
    root.title('   ')
    tk.Label(root, text=x, justify='left', anchor='nw', font=('楷体', 20), fg='black', bg='white', padx=20,
             pady=10, ).pack()  # 内容的格式和位置
    # 自动退出
    if x[0:2] in ['su', '已经', '下线']:  # quit函数会根据此列表来判断时候成功运行自动关闭
        root.after(700, root.destroy)
        window.after(900, window.destroy)
        return
    root.after(400, root.destroy)


# 设置主界面
window = tk.Tk()
# 设置标题
window.title('广州理工学院校园网登录')
# 设置大小、偏移量
window.geometry('301x150+800+400')
# 设置背景颜色
window.configure(bg='white')
# 设置tinker界面按钮
tk.Button(
    window, text='上号',
    font=("得意黑", 50,),
    fg='#177cb0', bg='white',
    relief="flat",
    command=click_button).pack(expand=True, fill="both", side="left")
# 结束
window.mainloop()