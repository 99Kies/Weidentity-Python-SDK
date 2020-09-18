import requests
import logging
from pprint import pprint
from Base import Base

LOG = logging.getLogger(__name__)

class weidentityClient(Base):
    def __init__(self, host, port=None, version="1.0.0"):
        super(weidentityClient, self).__init__(host, port, version)

    def create_weidentity_did_first(self, publicKey, nonce):
        # 创建WeIdentity DID
        data = {
            "functionArg": {
                "publicKey": publicKey
            },
            "transactionArg": {
                "nonce": nonce
            },
            "functionName": "createWeId",
            "v": self.version
        }
        return self.post("/weid/api/encode", data=data)

    def create_weidentity_did_second(self, nonce, data, signedMessage):
        # 创建WeIdentity DID
        data = {
            "functionArg": {},
            "transactionArg": {
                "nonce": nonce,
                "data": data,
                "signedMessage": signedMessage
            },
            "functionName": "createWeId",
            "v": self.version
        }
        return self.post("/weid/api/transact", data=data)

    def create_weidentity_did(self, publicKey, nonce, data, signedMessage):
        self.create_weidentity_did_first(publicKey, nonce)
        return self.create_weidentity_did_second(nonce, data, signedMessage)

    def register_authority_issuer_first(self, name, weId, nonce):
        # 注册Authority Issuer
        data = {
            "functionArg": {
                "name": name,
                "weId": weId
            },
            "transactionArg": {
                "nonce": nonce
            },
            "functionName": "registerAuthorityIssuer",
            "v": self.version
        }
        return self.post("/weid/api/encode", data=data)

    def register_authority_issuer_second(self, nonce, data, signedMessage):
        # 注册Authority Issuer
        data = {
            "functionArg": {},
            "transactionArg": {
                "nonce": nonce,
                "data": data,
                "signedMessage": signedMessage
            },
            "functionName": "registerAuthorityIssuer",
            "v": self.version
        }
        return self.post("/weid/api/transact", data=data)

    def register_authority_issuer(self, name, weId, nonce, data, signedMessage):
        self.register_authority_issuer_first(name, weId, nonce)
        return self.register_authority_issuer_second(nonce, data, signedMessage)

    def create_cpt_first(self, weId, cptJsonSchema, cptSignature, nonce):
        # 创建CPT
        data = {
            "functionArg": {
                "weId": weId,
                "cptJsonSchema": cptJsonSchema,
                "cptSignature": cptSignature
            },
            "transactionArg": {
                "nonce": nonce
            },
            "functionName": "registerCpt",
            "v": self.version
        }
        return self.post("/weid/api/encode", data=data)

    def create_cpt_second(self, nonce, data, signedMessage):
        # 创建CPT
        data = {
            "functionArg": {},
            "transactionArg": {
                "nonce": nonce,
                "data": data,
                "signedMessage": signedMessage
            },
            "functionName": "registerCpt",
            "v": self.version
        }
        return self.post("/weid/api/transact", data=data)

    def create_cpt(self, name, weId, nonce, data, signedMessage):
        self.register_authority_issuer_first(name, weId, nonce)
        return self.register_authority_issuer_second(nonce, data, signedMessage)

    def create_credential_pojo(self, cptId, issuer_weid, expirationDate, claim):
        # 创建CredentialPojo
        data = {
            "functionArg": {
                "cptId": cptId,
                "issuer": issuer_weid,
                "expirationDate": expirationDate,
                "claim": claim,
            },
            "transactionArg": {
            },
            "functionName": "createCredentialPojo",
            "v": self.version
        }
        return self.post("/weid/api/encode", data=data)


weid = weidentityClient("http://192.168.80.140:6001")
create_1 = weid.create_weidentity_did_first(publicKey="712679236821355231513532168231727831978932132185632517152735621683128", nonce="1474800601011307365506121304576347479508653499989424346408343855615822146039")
pprint(create_1)
create_2 = weid.create_weidentity_did_second(nonce="1474800601011307365506121304576347479508653499989424346408343855615822146039", data="809812638256c1235b1231000e000000001231287bacf213c", signedMessage="HEugP13uDVBg2G0kmmwbTkQXobsrWNqtGQJW6BoHU2Q2VQpwVhK382dArRMFN6BDq7ogozYBRC15QR8ueX5G3t8=")
pprint(create_2)

create_f = weid.create_weidentity_did(publicKey="712679236821355231513532168231727831978932132185632517152735621683128", nonce="1474800601011307365506121304576347479508653499989424346408343855615822146039", data="809812638256c1235b1231000e000000001231287bacf213c", signedMessage="HEugP13uDVBg2G0kmmwbTkQXobsrWNqtGQJW6BoHU2Q2VQpwVhK382dArRMFN6BDq7ogozYBRC15QR8ueX5G3t8=")
pprint(create_f)