
import pybrid.conn

def get_status(auth):
    base_url = "http://" + str(auth.ipaddress)
    data_url = "/status"
    data = pybrid.conn.get_data(auth, base_url, data_url)
    return data

def get_device_info(auth):
    base_url = "http://" + str(auth.ipaddress)
    data_url = "/info"
    data = pybrid.conn.get_data(auth, base_url, data_url)
    return data

def get_history(auth):
    base_url = "http://" + str(auth.ipaddress)
    data_url = "/history"
    data = pybrid.conn.get_data(auth, base_url, data_url)
    return data


Looks like 't' is time
'V' is VoCs in ppm
'T' is Temp in Celcius
'H' is Humidity in %
'C' is Co2 in ppm