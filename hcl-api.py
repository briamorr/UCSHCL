from time import sleep
import requests

results = []
resp = requests.post('https://ucshcltool.cloudapps.cisco.com/public/rest/osvendor/loadOsVendors',
                     headers={'Content-Type': 'application/x-www-form-urlencoded'})

for r in resp.json():
    if "Microsoft" not in r['OSVENDOR'] and "VMware" not in r['OSVENDOR']:
        payload = "treeIdVendor=" + str(r['T_ID'])
        resp = requests.post('https://ucshcltool.cloudapps.cisco.com/public/rest/osvendor/loadOsVersions', data=payload,
                             headers={'Content-Type': 'application/x-www-form-urlencoded'})

        for s in resp.json():
            payload = "treeIdOSVersion=" + str(s['T_ID'])
            resp = requests.post('https://ucshcltool.cloudapps.cisco.com/public/rest/osvendor/loadServerTypes',
                                 data=payload, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            sleep(0.05)

            for y in resp.json():
                if "C-Series" in y['RELEASE'] or "B-Series" in y['RELEASE']:
                    payload = "treeIdRelease=" + str(y['T_ID'])
                    resp = requests.post('https://ucshcltool.cloudapps.cisco.com/public/rest/osvendor/loadServerModels',
                                         data=payload, headers={'Content-Type': 'application/x-www-form-urlencoded'})
                    sleep(0.05)

                    for z in resp.json():
                        if "M4" in z['SERVER_MODEL'] or "M5" in z['SERVER_MODEL']:
                            print((z['SERVER_MODEL'] + " " + s['OSVERSION']))

