
from flask_marshmallow import Schema


class OccurrenceVariationDTO(Schema):
    class Meta:
        ordered = True
        fields = (
            "department",
            "year",
            "occurrence",
            "total",
            "average",
            "variation"
        )
