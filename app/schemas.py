from app import ma
from app.models import Url

from marshmallow import fields, validate


class UrlSchema(ma.Schema):

    long_url = fields.Str(required=True, validate=[validate.Length(min=6)])

    class Meta:
        model = Url
