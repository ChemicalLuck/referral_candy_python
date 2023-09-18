import hashlib
import requests
import time

_DEFAULT_API_URL = 'https://my.referralcandy.com/api/v1/'


class ReferralCandy:
    def __init__(self, access_id, secret_key):
        self.access_id = access_id
        self.secret_key = secret_key

    def _add_signature_to(self, params):
        params.update({'accessID': self.access_id, 'timestamp': int(time.time())})
        params.update({'signature': self._signature(params)})
        return params

    def _signature(self, params):
        collected_params = ''.join(('%s=%s' % (k,v)) for k, v in sorted(params.items()))
        return hashlib.md5((self.secret_key + collected_params).encode()).hexdigest()

    def verify(self, params):
        return requests.get("%sverify.json" % _DEFAULT_API_URL,
                            params=self._add_signature_to(params))

    def referrals(self, params):
        return requests.get("%sreferrals.json" % _DEFAULT_API_URL,
                            params=self._add_signature_to(params))

    def referrer(self, params):
        return requests.get("%sreferrer.json" % _DEFAULT_API_URL,
                            params=self._add_signature_to(params))

    def contacts(self, params):
        return requests.get("%scontacts.json" % _DEFAULT_API_URL,
                            params=self._add_signature_to(params))

    def purchase(self, params):
        return requests.post("%spurchase.json" % _DEFAULT_API_URL,
                             params=self._add_signature_to(params))

    def referral(self, params):
        return requests.post("%sreferral.json" % _DEFAULT_API_URL,
                             params=self._add_signature_to(params))

    def signup(self, params):
        return requests.post("%ssignup.json" % _DEFAULT_API_URL,
                             params=self._add_signature_to(params))

    def invite(self, params):
        return requests.post("%sinvite.json" % _DEFAULT_API_URL,
                             params=self._add_signature_to(params))

