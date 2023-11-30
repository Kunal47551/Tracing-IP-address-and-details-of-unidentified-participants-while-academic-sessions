import requests
import socket

def get_host_info(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f'HTTP Error: {errh}')
        print(f'API Response: {response.text}')
        return None
    except requests.exceptions.ConnectionError as errc:
        print(f'Error Connecting: {errc}')
        return None
    except requests.exceptions.Timeout as errt:
        print(f'Timeout Error: {errt}')
        return None
    except requests.exceptions.RequestException as err:
        print(f'OOps: Something Else {err}')
        return None

    data = response.json()

    if data['status'] == 'fail':
        print(f'Unable to retrieve information for IP address {ip_address}')
        print(f'API Response: {response.text}')
        return None

    return data


def get_local_ip():
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = '127.0.0.1'
    finally:
        return ip

def main():
    ip_address = get_local_ip()
    info = get_host_info(ip_address)

    if info:
        print(f'IP Address: {info["query"]}')
        print(f'City: {info["city"]}')
        print(f'Region: {info["regionName"]}')
        print(f'Country: {info["country"]}')
        print(f'ISP: {info["isp"]}')
        print(f'Timezone: {info["timezone"]}')

if __name__ == "__main__":
    main()
