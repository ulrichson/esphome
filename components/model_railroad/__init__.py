import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome.components import (
   light
)

DEPENDENCIES = []

modelrailroad_ns = cg.esphome_ns.namespace('modelrailroad')
ModelRailroadComponent = modelrailroad_ns.class_('ModelRailroadComponent', light.LightOutput, cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ModelRailroadComponent),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await light.register_light(var, config)