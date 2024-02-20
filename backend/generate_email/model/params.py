import datetime as dt

from marshmallow import Schema, fields


class Params(object):
    def __init__(self, product_name, drug_name, indications, dosing_period, pharma_producer):
        self.product_name = product_name
        self.drug_name = drug_name
        self.indications = indications
        self.dosing_period = dosing_period
        self.pharma_producer = pharma_producer

    def __repr__(self):
        return '<EmailParams(name={self.channel!r})>'.format(self=self)


class ParamsSchema(Schema):
    product_name = fields.Str()
    drug_name = fields.Str()
    indications = fields.List(fields.Str())
    dosing_period = fields.Str()
    pharma_producer = fields.Str()
