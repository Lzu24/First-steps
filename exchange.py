import requests

respons = requests.get("https://api.nbp.pl/api/exchangerates/tables/a?format=json")

if respons.ok == True:
    data = respons.json()[0]
    print(data)

    table = data["table"]
    no = data["no"]
    effectiveData = data["effectiveDate"]
    print("Exchange : ", table, no, effectiveData)

    rates = data["rates"]

    for rate in rates:
        currency = rate["currency"]
        code = rate["code"]
        mid = rate["mid"]
        print(currency, "code: ", code, "value:",mid)
        