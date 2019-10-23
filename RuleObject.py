import json


class RuleObject:
    def __init__(self, json_filename):

        with open(json_filename, "r") as f:
            self._json_obj = json.loads(f.read())

            self._rule_number = self._json_obj["rulenumber"]
            self._crime = self._json_obj["crime"]
            self._x1_permission = self._json_obj["x1_permission"]
            self._x2n3n4_comb = self._json_obj["x2n3n4_comb"]
            self._yscore = self._json_obj["yscore"]

    @property
    def rule_number(self):
        return self._rule_number

    @property
    def crime(self):
        return self._crime

    @property
    def x1_permission(self):
        return self._x1_permission

    @property
    def x2n3n4_comb(self):
        return self._x2n3n4_comb

    @property
    def yscore(self):
        return self._yscore
