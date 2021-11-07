

from pandas.core.frame import DataFrame
from occurrencies.models.dtos.occurrence_variation_dto import OccurrenceVariationDTO
from occurrencies.models.dtos.occurrence_monthly_dto import OccurrenceMonthlyDTO
from occurrencies.models.dtos.occurrence_yearly_dto import OccurrenceYearlyDTO, OccurrenceYearlyListDTO
from occurrencies.models.dtos.occurrence_monthly_overview_dto import OccurrenceMonthlyOverviewDTO


def occurrence_to_dto(occ, metrics):
    variation = OccurrenceVariationDTO()
    variation.average = metrics[0]
    variation.variation = metrics[1]
    variation.total = occ.total
    variation.occurrence = occ.occurrence
    variation.department = occ.department
    variation.year = occ.year
    return variation

def occ_frame_to_monthly_dto(occ, average):
    monthly_occ = OccurrenceMonthlyDTO()
    monthly_occ.department = occ['department']["$oid"]
    monthly_occ.year = occ['year']["$oid"]
    monthly_occ.jan = occ['jan']["$oid"]
    monthly_occ.feb = occ['feb']["$oid"]
    monthly_occ.mar = occ['mar']["$oid"]
    monthly_occ.apr = occ['apr']["$oid"]
    monthly_occ.may = occ['may']["$oid"]
    monthly_occ.jun = occ['jun']["$oid"]
    monthly_occ.jul = occ['jul']["$oid"]
    monthly_occ.aug = occ['aug']["$oid"]
    monthly_occ.sep = occ['sep']["$oid"]
    monthly_occ.oct = occ['oct']["$oid"]
    monthly_occ.nov = occ['nov']["$oid"]
    monthly_occ.dez = occ['dec']["$oid"]
    monthly_occ.total = occ['total']["$oid"]
    monthly_occ.average = average
    return monthly_occ

def occ_frame_to_monthly_overview_dto(occs_data):
    print(occs_data)
    monthly_occ = OccurrenceMonthlyOverviewDTO()
    monthly_occ.jan = round(float(occs_data['jan'].astype(int).mean()), 2) 
    monthly_occ.feb = round(float(occs_data['feb'].astype(int).mean()), 2)
    monthly_occ.mar = round(float(occs_data['mar'].astype(int).mean()), 2)
    monthly_occ.apr = round(float(occs_data['apr'].astype(int).mean()), 2)
    monthly_occ.may = round(float(occs_data['may'].astype(int).mean()), 2)
    monthly_occ.jun = round(float(occs_data['jun'].astype(int).mean()), 2)
    monthly_occ.jul = round(float(occs_data['jul'].astype(int).mean()), 2)
    monthly_occ.aug = round(float(occs_data['aug'].astype(int).mean()), 2)
    monthly_occ.sep = round(float(occs_data['sep'].astype(int).mean()), 2)
    monthly_occ.oct = round(float(occs_data['oct'].astype(int).mean()), 2)
    monthly_occ.nov = round(float(occs_data['nov'].astype(int).mean()), 2)
    monthly_occ.dec = round(float(occs_data['dec'].astype(int).mean()), 2)
    return monthly_occ

def occ_frame_to_yearly_dto(occ):
    yearly_occ = OccurrenceYearlyDTO()
    yearly_occ.department = occ["department"]
    yearly_occ.year = occ["year"]
    yearly_occ.occurrence = occ["occurrence"]
    yearly_occ.total = occ["total"]
    return yearly_occ

def occ_frame_to_yearly_list_dto(occs, average):
    occ_list = OccurrenceYearlyListDTO()
    occ_list.years = OccurrenceYearlyDTO(many=True).dump(occs)
    occ_list.average = average
    return occ_list
    
