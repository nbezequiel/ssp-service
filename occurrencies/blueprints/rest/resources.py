from flask import abort, request
from flask_restful import Resource
from ...services.occurrence_service import OccurrenceService
from ...models.dtos.occurrence_variation_dto import OccurrenceVariationDTO
from ...models.dtos.occurrence_monthly_dto import OccurrenceMonthlyDTO
from ...models.dtos.occurrence_yearly_dto import OccurrenceYearlyListDTO
from ...models.dtos.occurrence_monthly_overview_dto import OccurrenceMonthlyOverviewDTO


class OccurrenceResource(Resource):

    def __init__(self):
        self._service = OccurrenceService()
        

    def get(self):
        params = request.args
        department = params.get("department-name")
        year = params.get("year")

        if department == None or year == None:
            return abort(400, "missing parameters")

        all_occurrencies = self._service.all_ocurrencies(department, year)
        return OccurrenceVariationDTO(many=True).dump(all_occurrencies)



class OccurrenceMonthOverviewResource(Resource):

    def __init__(self):
        self._service = OccurrenceService()
        

    def get(self):
        params = request.args
        department = params.get("department-name")
        year = params.get("year")

        if department == None or year == None:
            return abort(400, "missing parameters")

        all_occurrencies = self._service.all_ocurrencies_monthly(department, year)
        print(OccurrenceMonthlyOverviewDTO().dump(all_occurrencies))
        return OccurrenceMonthlyOverviewDTO().dump(all_occurrencies)


class MonthlyOccurrenceResource(Resource):
    
    def __init__(self):
        self._service = OccurrenceService()
        

    def get(self):
        params = request.args
        department = params.get("department-name")
        year = params.get("year")
        crime_type = params.get("crime-type")

        monthly_occ = self._service.monthly_ocurrencies(department, year, crime_type)
        return OccurrenceMonthlyDTO(many=False).dump(monthly_occ)


class YearlyOccurrenceResource(Resource):
    
    def __init__(self):
        self._service = OccurrenceService()
        

    def get(self):
        params = request.args
        department = params.get("department-name")
        crime_type = params.get("crime-type")

        yearly_occ = self._service.yearly_ocurrencies(department, crime_type)

        return OccurrenceYearlyListDTO().dump(yearly_occ)

