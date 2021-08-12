# Webscraping with Regular Expression 

```py
import re
import urllib3
import json

url = 'https://www.amazon.in/dp/B096VD213D/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B096VD213D&pd_rd_w=2axiF&pf_rd_p=3d347ba3-873a-4950-a530-1b4d5938343e&pd_rd_wg=iGw0V&pf_rd_r=0XHSVNWACNZC1GF0A3QY&pd_rd_r=14c2d3bc-7970-4f2a-aa42-9e68675642fc&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNzNFR1VWMjlFTUpHJmVuY3J5cHRlZElkPUEwNjUyNDI1Mk84NEIyM1pGRzZKMiZlbmNyeXB0ZWRBZElkPUEwNzIwMTEyMzhGTFZJODBDUkVIOCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

http = urllib3.PoolManager()
urllib3.disable_warnings()

html = http.request("GET",url)

def getText(s,e):
    ptrn = s+'(.*?)'+e
    return ptrn
#print(html.status)
#print(html.data)
#print(html.headers)

html_doc = html.data.decode("utf-8")

product_title = re.findall('<span id="productTitle" class="a-size-large product-title-word-break">(.*?)</span>',html_doc)
current_price = re.findall('<span id="priceblock_ourprice".*>(.*?)</span>',html_doc)
deal_price = re.findall('<span id="priceblock_dealprice" class="a-size-medium a-color-price priceBlockDealPriceString">(.*?)</span>',html_doc)
actp_search = getText('<span class="priceBlockStrikePriceString a-text-strike">','</span>')
you_save = re.findall('<tr id="dealprice_savings">(.*?)</tr>',html_doc)
delivery = re.findall('<div id="ddmDeliveryMessage".*>(.*?)</b>',html_doc)


actual_price = re.findall(actp_search,html_doc)


print("Product: ",product_title)
print("Current Price: ",current_price)
print("Deal Price: ",deal_price)
print("Actual Price: ",actual_price)
print("You Save: ",you_save)
print(delivery)

```
