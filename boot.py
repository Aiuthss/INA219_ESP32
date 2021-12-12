import network
import ujson

def connect_best_lan():
    f = open('AP.json', 'r')
    x = ujson.load(f)
    f.close()

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print('network interface activated')
    nets = wlan.scan()
    RSSI = {}
    for i in nets:
        RSSI[i[0].decode('utf-8')] = i[3]

    max_rssi = -10000
    best_SSID = ''
    pwd = ''
    for i in x:
        rssi = RSSI.get(i['SSID'], -10000)
        if rssi > max_rssi:
            best_SSID = i['SSID']
            pwd = i['password']
            max_rssi = rssi
    if len(best_SSID) != 0:
        wlan.connect(best_SSID, pwd)
        while not wlan.isconnected():
            pass
        print('network config:', best_SSID, wlan.ifconfig())
    return wlan

def main():
    connect_best_lan()

if __name__ == "__main__":
    main()