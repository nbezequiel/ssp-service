from mongoengine import Document, StringField, queryset_manager


class Occurrence(Document):
    
    department = StringField()

    year = StringField()

    occurrence = StringField()

    jan = StringField()

    feb = StringField()

    mar = StringField()

    apr = StringField()

    may = StringField()

    jun = StringField()

    jul = StringField()

    aug = StringField()

    sep = StringField()

    oct = StringField()

    nov = StringField()

    dec = StringField()

    total = StringField()



    @queryset_manager
    def all_occurrencies(doc_cls, queryset, department, year):
        return queryset.filter(department=department, year=year, occurrence__ne = "NOT_USED")

    @queryset_manager
    def all_occurrencies_monthly(doc_cls, queryset, department):
        return queryset.filter(department=department, occurrence__ne = "NOT_USED")
    
    @queryset_manager
    def monthly_occurrence(doc_cls, queryset, department, year, crimeType):
        return queryset.filter(department=department, year=year, occurrence = crimeType)
    
    @queryset_manager
    def yearly_occurrence(doc_cls, queryset, department, crimeType):
        return queryset.filter(department=department, occurrence = crimeType)
    
    @queryset_manager
    def occurrence_average(doc_cls, queryset, ocurrence):
        return queryset.filter(department = ocurrence.department, 
                              year__lt = str(ocurrence.year),
                              year__gte = "2014",
                              year__gt = str(int(ocurrence.year) - 5),
                              occurrence = ocurrence.occurrence)