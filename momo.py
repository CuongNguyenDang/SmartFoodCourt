import json
import uuid
import hmac
import hashlib

#import requests

#parameters send to MoMo get get payUrl
def getUrl(_amount):
	endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"
	partnerCode = "MOMOTKZV20200616"
	accessKey = "yBMKEkDSHBNlCNu8"
	serectkey = "TVFKWUzFlPeM1r9nQdB1T4giVML3XHjC"
	orderInfo = "pay with MoMo"
	returnUrl = "https://momo.vn"
	notifyurl = "https://momo.vn"
	amount = str(_amount)
	orderId = str(uuid.uuid4())#"MM1540456472576"
	requestId = "MM1540456472575"#str(uuid.uuid4())
	requestType = "captureMoMoWallet"
	extraData = "abc" #pass empty value if your merchant does not have stores else merchantName=[storeName]; merchantId=[storeId] to identify a transaction map with a physical store

	#before sign HMAC SHA256 with format
	# partnerCode=$partnerCode&accessKey=$accessKey&requestId=$requestId&amount=$amount&orderId=$oderId&orderInfo=$orderInfo&returnUrl=$returnUrl&notifyUrl=$notifyUrl&extraData=$extraData

	rawSignature = "partnerCode="+partnerCode+"&accessKey="+accessKey+"&requestId="+requestId+"&amount="+amount+"&orderId="+orderId+"&orderInfo="+orderInfo+"&returnUrl="+returnUrl+"&notifyUrl="+notifyurl+"&extraData="+extraData

	#puts raw signature
	# print("--------------------RAW SIGNATURE----------------")
	# print(rawSignature)
	#signature
	h = hmac.new(bytes(serectkey,'latin-1'), bytes(rawSignature,'latin-1'), hashlib.sha256)
	signature = h.hexdigest()
	# print("--------------------SIGNATURE----------------")
	# print(signature)
	#json object send to MoMo endpoint

	data = {
			'partnerCode' : partnerCode,
			'accessKey' : accessKey,
			'requestId' : requestId,
			'amount' : amount,
			'orderId' : orderId,
			'orderInfo' : orderInfo,
			'returnUrl' : returnUrl,
			'notifyUrl' : notifyurl,
			'extraData' : extraData,
			'requestType' : requestType,
			'signature' : signature
	}
	# print("--------------------JSON REQUEST----------------\n")
	data = json.dumps(data)
	# print(data)

	# clen = len(data)
	headers = {'Content-Type': 'application/json'}#; charset=UTF-8'}#, 'Content-Length': str(clen)}
	# response = requests.put(url = endpoint,data = data,headers=headers)

	response = requests.post(endpoint,data=data,headers=headers)
	response = response.json()

	# print("--------------------JSON response----------------\n")
	# print(response)
	return response['payUrl']