import csv
import json
import ast
from datetime import datetime

builtInCertsPath = 'BuiltInCAs.csv'
builtInCertsFile = file(builtInCertsPath, 'r')
builtInCertsOutput = 'SalesForceData.js'

def findIndexOf(string, columns):
    for i, item in enumerate(columns):
        if item == string:
            return i
    raise Error("could not find column '%s'" % string)

def getBuiltInCerts():
    output = open(builtInCertsOutput, 'w')
    reader = csv.reader(builtInCertsFile)
    salesforceJson = {}

    rows = []
    for row in reader:
        rows.append(row)
    columns = rows[0]
    trustBitsIndex = findIndexOf("Trust Bits", columns)
    auditDateIndex = findIndexOf("Standard Audit Statement Dt", columns)
    geographicFocusIndex = findIndexOf("Geographic Focus", columns)
    ownerIndex = findIndexOf("Owner", columns)
    issuerOrganizationIndex = findIndexOf("Certificate Issuer Organization", columns)

    for row in rows[1:]:
        cert = {}
        cert['trustBits'] = row[trustBitsIndex]
        cert['auditDate'] = row[auditDateIndex].strip()
        cert['geographicFocus'] = row[geographicFocusIndex]
        cert['owner'] = row[ownerIndex]
        issuerOrganization = row[issuerOrganizationIndex]
        if not salesforceJson.has_key(issuerOrganization):
            salesforceJson[issuerOrganization] = cert
        else:
            salesforceJson[issuerOrganization] = getMostRecentCert(salesforceJson[issuerOrganization], cert)
    output.write('var certManagerJsonText = ' + json.dumps(salesforceJson, indent=2, separators=(',', ': ')) + '''
var certManagerJson = certManagerJsonText;

function getJSON() {
    return certManagerJson;
}

exports.getJSON = getJSON;
''')


def getMostRecentCert(cert1, cert2):
    result = {}
    date1 = None
    date2 = None

    if not cert1['auditDate'] == '':
        date1 = datetime.strptime(cert1['auditDate'], '%Y.%m.%d')

    if not cert2['auditDate'] == '':
        date2 = datetime.strptime(cert2['auditDate'], '%Y.%m.%d')

    bits1 = [x.strip() for x in cert1['trustBits'].split(';')]
    bits2 = [x.strip() for x in cert2['trustBits'].split(';')]
    geo = cert1['geographicFocus']
    bitsUnion = union(bits1, bits2)

    if date1 == None and date2 == None:
        result['auditDate'] = ''
    elif date1 == None:
        result['auditDate'] = date2.strftime('%Y.%m.%d')
    elif date2 == None:
        result['auditDate'] = date1.strftime('%Y.%m.%d')
    else:
        result['auditDate'] = max(date1, date2).strftime('%Y.%m.%d')
    result['trustBits'] = '; '.join(bitsUnion)
    result['geographicFocus'] = geo
    result['owner'] = cert2['owner']

    return result

def union(a, b):
    return list(set(a) | set(b))

def main():
    getBuiltInCerts()

if __name__ == '__main__':
    main()
