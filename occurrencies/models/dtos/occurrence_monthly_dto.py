
from flask_marshmallow import Schema


class OccurrenceMonthlyDTO(Schema):
    class Meta:
        ordered = True
        fields = (
            "department",
            "year",
            "occurrence",
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
            "dez",
            "total",
            "average" )



    
