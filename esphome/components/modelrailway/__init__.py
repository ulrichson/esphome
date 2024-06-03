import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components.light import LightState
from esphome.const import CONF_ID, CONF_OUTPUT_ID

from esphome.components import light

MULTI_CONF = False

AUTO_LOAD = [ "light" ]

DEPENDENCIES = []

modelrailway_ns = cg.esphome_ns.namespace('modelrailway')
ModelRailwayComponent = modelrailway_ns.class_('ModelRailwayComponent', light.LightOutput, cg.Component)

CONF_LIGHT = "light"

# CONFIG_SCHEMA = light.BINARY_LIGHT_SCHEMA.extend(
#     {
#         # cv.GenerateID(CONF_ID): cv.declare_id(LightState),
#         # cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(ModelRailwayComponent)
#         cv.GenerateID(): cv.declare_id(ModelRailwayComponent),
#     }
# ).extend(cv.COMPONENT_SCHEMA)

CONFIG_SCHEMA = light.BINARY_LIGHT_SCHEMA.extend(
    {
        cv.GenerateID(CONF_ID): cv.declare_id(LightState),
        cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(ModelRailwayComponent)
        # cv.GenerateID(): cv.declare_id(ModelRailwayComponent),
    }
).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    # cg.add(cg.App.register_light(var))
    # await cg.register_component(var, config)
    await light.register_light(var, config)