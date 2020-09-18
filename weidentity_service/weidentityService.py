import requests
import logging
from pprint import pprint
from Base import Base

LOG = logging.getLogger(__name__)


class weidentityService(Base):
    def __init__(self, host, port=None, version="1.0.0"):
        super(weidentityService, self).__init__(host, port, version)

    def create_weidentity_did(self, function_arg={}, transaction_arg={}):
        # 创建WeIdentity DID
        data = {
            "functionArg": function_arg,
            "transactionArg": transaction_arg,
            "functionName": "createWeId",
            "v": self.version
        }
        return self.post("/weid/api/invoke", data=data)

    def get_weidentity_did(self, weId):
        # 获取WeIdentity DID Document
        data = {
            "functionArg": {
                "weId": weId
            },
            "transactionArg": {},
            "functionName": "getWeIdDocument",
            "v": self.version
        }
        return self.post("/weid/api/invoke", data=data)

    def create_authority_issuer(self, weId, orgName, invokerWeId):
        # 创建AuthorityIssuer
        data = {
            "functionArg": {
                "weid": weId,
                "name": orgName
            },
            "transactionArg": {
                "invokerWeId": invokerWeId
            },
            "functionName": "registerAuthorityIssuer",
            "v": self.version
        }
        return self.post("/weid/api/invoke", data=data)

    def get_authority_issuer(self, weId, orgName, invokerWeId):
        # 查询AuthorityIssuer
        data = {
            "functionArg": {
               "weId": weId
            },
            "transactionArg": {
            },
            "functionName": "queryAuthorityIssuer",
            "v": self.version
        }
        return self.post("/weid/api/invoke", data=data)

    def create_cpt(self, weId, invokerWeId, cptJsonSchema):
        # 创建CPT
        data = {
          "functionArg": {
              "weId": weId,
              "cptJsonSchema": cptJsonSchema
          },
          "transactionArg": {
              "invokerWeId": invokerWeId
          },
          "functionName": "registerCpt",
          "v": self.version
        }

        return self.post("/weid/api/invoke", data=data)

    def get_cpt(self, cptId):
        # 查询CPT
        data = {
            "functionArg": {
                "cptId": cptId,
            },
            "transactionArg": {
            },
            "functionName": "queryCpt",
            "v": self.version
        }

        return self.post("/weid/api/invoke", data=data)

    def create_credential(self, cptId, issuerWeId, expirationDate, claim, invokerWeId):
        # 创建Credential
        data = {
            "functionArg": {
                "cptId": cptId,
                "issuer": issuerWeId,
                "expirationDate": expirationDate,
                "claim": claim,
            },
            "transactionArg": {
                "invokerWeId": invokerWeId
            },
            "functionName": "createCredential",
            "v": self.version
        }

        return self.post("/weid/api/invoke", data=data)

    def verify_credential(self, cptId, uuid, issuerWeId, expirationDate, issuranceDate, claim, context, proof):
        # 验证Credential
        data = {
            "functionArg": {
              "@context": context,
              "claim": claim,
              "cptId": cptId,
              "expirationDate": expirationDate,
              "id": uuid,
              "issuanceDate": issuranceDate,
              "issuer": issuerWeId,
              "proof": proof
            },
            "transactionArg": {
            },
            "functionName": "verifyCredential",
            "v": self.version
        }

        return self.post("/weid/api/invoke", data=data)


    def create_credentialpojo(self, cptId, issuerWeId, expirationDate, claim,invokerWeId):
        # 创建CredentialPojo
        data = {
            "functionArg": {
                "cptId": cptId,
                "issuer": issuerWeId,
                "expirationDate": expirationDate,
                "claim": claim,
            },
            "transactionArg": {
                "invokerWeId": invokerWeId
            },
            "functionName": "createCredentialPojo",
            "v": self.version
        }

        return self.post("/weid/api/invoke", data=data)

    def verify_credentialpojo(self, cptId, issuanceDate, context, claim, uuid, proof, issuerWeId, expirationDate):
        # 验证CredentialPojo
        data = {
            "functionArg": {
              "cptId": cptId,
              "issuanceDate": issuanceDate,
              "context": context,
              "claim": claim,
              "id": uuid,
              "proof": proof,
              "type": [
                  "VerifiableCredential",
                  "hashTree"
              ],
              "issuer": issuerWeId,
              "expirationDate": expirationDate
            },
            "transactionArg": {
            },
            "functionName": "verifyCredentialPojo",
            "v": self.version
        }

        return self.post("/weid/api/invoke", data=data)

    def get_registered_endpoint(self):
        # 获取所有已注册的Endpoint信息
        return self.get("/weid/api/endpoint")

    def get_endpoint(self, body):
        # 进行Endpoint调用
        data = {
            "body": body
        }

        return self.post("/weid/api/endpoint", data=data)

    def get_authorize_fetch_data(self, authToken, signedNonce):
        data = {
          "authToken": authToken,
          "signedNonce": signedNonce
        }
        return self.post("/weid/api/authorize/fetch-data", data=data)


weid = weidentityService("http://192.168.80.140:6001")
create_weid = weid.create_weidentity_did()
print(create_weid)
we_id = create_weid['respBody']
print("\n======================================\n")
get_weid = weid.get_weidentity_did(we_id)
pprint(get_weid)


