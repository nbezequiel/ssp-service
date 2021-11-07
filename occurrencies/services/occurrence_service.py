from ..models.occurrence import Occurrence
from ..exception.exceptions import *
from ..mappers.mapper import *
import pandas as pd
import json


class OccurrenceService:

    ## overview
    def all_ocurrencies(self, department, year):
        try:
            ocurrencies = Occurrence.all_occurrencies(department, year)
        except Exception as e:
            raise DatabaseIntegrationError(e)

        overview = self._variations(ocurrencies)
        self.check_is_empty(overview)
        return overview
        
    ## overview monthly
    def all_ocurrencies_monthly(self, department, year):
        try:
            ocurrencies = Occurrence.all_occurrencies_monthly(department)
        except Exception as e:
            raise DatabaseIntegrationError(e)

        return self.all_years_mothly_mean(ocurrencies)
    
    ## monthly occurrencies
    def monthly_ocurrencies(self, department, year, crime_type):
        try:
            occurrencies = Occurrence.monthly_occurrence(department, year, crime_type)
        except Exception as e:
            raise DatabaseIntegrationError(e)
        self.check_is_empty(occurrencies)
        return self.calc_monthly_mean(occurrencies[0])

    ## yearly occurrencies
    def yearly_ocurrencies(self, department, crime_type):
        try:
            occurrencies = Occurrence.yearly_occurrence(department, crime_type)
        except Exception as e:
            raise DatabaseIntegrationError(e)
        self.check_is_empty(occurrencies)
        return self.calc_yearly_mean(occurrencies)
    
    def calc_monthly_mean(self, occ):
        occ_data = pd.DataFrame(eval(occ.to_json()))
        occ_data = occ_data.drop('_id',1)
        self.remove_points(occ_data)
        average = round(occ_data[occ_data.columns[4:16]].sum().astype("int").mean(),2)
        return occ_frame_to_monthly_dto(occ_data.to_dict(), average)
    
    def calc_yearly_mean(self, occs):
        occs_data = pd.DataFrame(eval(occs.to_json()))
        occs_data = occs_data.drop('_id',1)
        occs_data = self.remove_points(occs_data)
        average = round(occs_data['total'].astype("int").mean(),2)
        years = [occ_frame_to_yearly_dto(x) for x in occs]
    
        return occ_frame_to_yearly_list_dto(years, average)

    def all_years_mothly_mean(self, ocurrencies):
        occs_data = pd.DataFrame(eval(ocurrencies.to_json()))
        occs_data = occs_data.drop('_id',1)
        occs_data = self.remove_points(occs_data)

        return occ_frame_to_monthly_overview_dto(occs_data)

    def _variations(self, ocurrencies):
        variations = []
        for occ in ocurrencies: 
            metrics = self._calc_metrics(occ)
            variation = occurrence_to_dto(occ, metrics)
            variations.append(variation)
        return variations
    

    def _calc_metrics(self, occ):
        older_occs = self._get_older_occurrencies(occ)
        occs_data = pd.DataFrame(eval(older_occs.to_json()))
        occs_data = occs_data.drop('_id',1)
        self.remove_points(occs_data)

        occ_total = int(occ.total.replace(".", ""))

        average = round(float(occs_data['total'].astype(int).mean()), 2)  
        variation = round(((occ_total-average)/average)*100,2) if average != 0 else 0
        return [average, variation]

    def _get_older_occurrencies(self, occurrence):
        try:
            return Occurrence.occurrence_average(occurrence)
        except Exception as e:
            raise DatabaseIntegrationError(e)

    def remove_points(self, data):
        for column in data.columns.values:
            data[column] = data[column].apply(lambda t: t.replace('.', ''))
            data[column] = data[column].apply(lambda t:  '0' if t == '' else t)
        return data
    
    def check_is_empty(self, occs):
        if occs == [] or list(occs) == []:
            raise NotFoundException()