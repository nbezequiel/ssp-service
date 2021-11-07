
from flask_marshmallow import Schema


class OccurrenceMonthlyOverviewDTO(Schema):
    class Meta:
        ordered = True
        fields = (
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec"
        )
