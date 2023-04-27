from flask import Blueprint
from flask_restful import Api
from utils.jwt import check_premission
from resources.en_readability.views import (
    ARI,
    ARIGradeLevels,
    RIX,
    FlsechKincaidGrade,
    GunningFog,
    Smog,
    ColemanLiauIndex,
    DaleChallIndex,
    LWIndex,
    AllReadability,
    FleschReading
)

readability_indicator = Blueprint('ReadAbility', __name__, url_prefix='/readability')
readability_api = Api(readability_indicator)
readability_api.add_resource(ARI, '/ari')
readability_api.add_resource(RIX, '/rix')
readability_api.add_resource(FleschReading, '/flsechreading')
readability_api.add_resource(FlsechKincaidGrade, '/flsechkincaid')
readability_api.add_resource(GunningFog, '/gunningfog')
readability_api.add_resource(Smog, '/smog')
readability_api.add_resource(ColemanLiauIndex, '/colemanLiauIndex')
readability_api.add_resource(DaleChallIndex, '/daleChallIndex')
readability_api.add_resource(LWIndex, '/lwIndex')
readability_api.add_resource(AllReadability, '/all')
