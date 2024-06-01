import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome.components import (
   light
)

DEPENDENCIES = []

modelrailway_ns = cg.esphome_ns.namespace('modelrailway')
ModelRailwayComponent = modelrailway_ns.class_('ModelRailwayComponent', light.LightOutput, cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ModelRailwayComponent),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    # await light.register_light(var, config)