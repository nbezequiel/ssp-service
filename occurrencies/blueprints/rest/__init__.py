from flask import Blueprint
from flask_restful import Api

from .resources import OccurrenceResource, MonthlyOccurrenceResource, YearlyOccurrenceResource, OccurrenceMonthOverviewResource

bp = Blueprint("rest", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(OccurrenceResource, "/occurrence/overview" )
    api.add_resource(MonthlyOccurrenceResource, "/occurrence/monthly" )
    api.add_resource(YearlyOccurrenceResource, "/occurrence/yearly" )
    api.add_resource(OccurrenceMonthOverviewResource, "/occurrence/overview/monthly" )
    app.register_blueprint(bp)