
from flask_marshmallow import Schema


class OccurrenceYearlyDTO(Schema):
    class Meta:
        ordered = True
        fields = (
            "department",
            "year",
            "occurrence",
            "total")

class OccurrenceYearlyListDTO(Schema):
    class Meta:
        ordered = True
        fields = (
            "years",
            "average")



    
