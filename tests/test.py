# from pyweidentity.weidentityClient import weidentityClient
# import random
#
# URL = "http://192.168.80.144:6001"
# # WeIdentity RestService URL
#
# weid = weidentityClient(URL)
# privKey = "0xc4a116fb87ae9b8b87842b0f46e1bbf71c37fdae1104fd6d3fd2041e23c6c68e"
# nonce = str(random.randint(1, 999999999999999999999999999999))
# create_weid = weid.create_weidentity_did(privKey, nonce)
# print(create_weid)


# from pyweidentity.weidentityService import weidentityService
#
# URL = "http://192.168.80.144:6001"
# # WeIdentity RestService URL
#
# weid = weidentityService(URL)
# create_weid = weid.create_weidentity_did()
# print(create_weid)

# {'respBody': 'did:weid:1:0x3a08be5b858bbd765a7a914a7d50be31558dd00f', 'loopback': None, 'errorCode': 0, 'errorMessage': 'success'}