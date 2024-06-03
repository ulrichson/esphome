from esphome import pins
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light
from esphome.const import CONF_OUTPUT_ID
from .. import status_led_ns

AUTO_LOAD = ["output"]

modelrailway_ns = cg.esphome_ns.namespace('modelrailway')
ModelRailwayComponent = modelrailway_ns.class_('ModelRailwayComponent', light.LightOutput, cg.Component)

CONFIG_SCHEMA = cv.All(
    light.BINARY_LIGHT_SCHEMA.extend(
        {
            cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(ModelRailwayComponent)
        }
    )
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    await cg.register_component(var, config)
    await light.register_light(var, config)