
import requests, json
from pybrid.conn import check_response


def get_device_info(auth):
    base_url = "http://" + str(auth.ipaddress)
    data_url = "/info"
    data = pybrid.conn.get_data(auth, base_url, data_url)
    return data


def set_device_status(auth, mode):
    modes = {"off" : 0,
             'smart' : 1,
             'auto' : 2,
             'boost' : 3,
             'night' : 4}
    base_url = "http://" + str(auth.ipaddress)
    data_url = "/settings"
    f_url = base_url+data_url
    data = {"mode" : modes[mode]}
    response = requests.post(f_url, headers=auth.headers, json=data)
    check_response(response)
    return json.loads(response.text)




