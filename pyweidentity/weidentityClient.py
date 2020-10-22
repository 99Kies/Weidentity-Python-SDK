import requests
import logging
from .Base import Base
import time

LOG = logging.getLogger(__name__)

class weidentityClient(Base):
    def __init__(self, host, port=None, version="1.0.0"):
        super(weidentityClient, self).__init__(host, port, version)

    def create_weidentity_did_first(self, publicKey, nonce):
        # 创建WeIdentity DID
        data_dict = {
            "functionArg": {
                "publicKey": publicKey
            },
            "transactionArg": {
                "nonce": nonce
            },
            "functionName": "createWeId",
            "v": self.version
        }
        return self.post("/weid/api/encode", data=data_dict)

    def create_weidentity_did_second(self, nonce, data, signedMessage):
        # 创建WeIdentity DID
        data_dict = {
            "functionArg": {},
            "transactionArg": {
                "nonce": nonce,
                "data": data,
                "signedMessage": signedMessage
            },
            "functionName": "createWeId",
            "v": self.version
        }
        return self.post("/weid/api/transact", data=data_dict)

    def create_weidentity_did(self, publicKey, nonce, data, signedMessage):
        self.create_weidentity_did_first(publicKey, nonce)
        return self.create_weidentity_did_second(nonce, data, signedMessage)

    def register_authority_issuer_first(self, name, weId, nonce):
        # 注册Authority Issuer
        data_dict = {
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
        return self.post("/weid/api/encode", data=data_dict)

    def register_authority_issuer_second(self, nonce, data, signedMessage):
        # 注册Authority Issuer
        data_dict = {
            "functionArg": {},
            "transactionArg": {
                "nonce": nonce,
                "data": data,
                "signedMessage": signedMessage
            },
            "functionName": "registerAuthorityIssuer",
            "v": self.version
        }
        return self.post("/weid/api/transact", data=data_dict)

    def register_authority_issuer(self, name, weId, nonce, data, signedMessage):
        self.register_authority_issuer_first(name, weId, nonce)
        return self.register_authority_issuer_second(nonce, data, signedMessage)

    def create_cpt_first(self, weId, cptJsonSchema, cptSignature, nonce):
        # 创建CPT
        data_dict = {
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
        return self.post("/weid/api/encode", data=data_dict)

    def create_cpt_second(self, nonce, data, signedMessage):
        # 创建CPT
        data_dict = {
            "functionArg": {},
            "transactionArg": {
                "nonce": nonce,
                "data": data,
                "signedMessage": signedMessage
            },
            "functionName": "registerCpt",
            "v": self.version
        }
        return self.post("/weid/api/transact", data=data_dict)

    def create_cpt(self, name, weId, nonce, data, signedMessage):
        self.register_authority_issuer_first(name, weId, nonce)
        return self.register_authority_issuer_second(nonce, data, signedMessage)

    def create_credential_pojo(self, cptId, issuer_weid, expirationDate, claim):
        # 创建CredentialPojo
        if isinstance(expirationDate, int):
            expirationDate = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(expirationDate))
        data_dict = {
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
        return self.post("/weid/api/encode", data=data_dict)