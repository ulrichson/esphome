from esphome import pins
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light
from esphome.const import CONF_NAME, CONF_OUTPUT_ID, CONF_RESTORE_MODE

AUTO_LOAD = ["light", "output"]

light_ns = cg.esphome_ns.namespace("light")
LightRestoreMode = light_ns.enum("LightRestoreMode")
RESTORE_MODES = {
    "RESTORE_DEFAULT_OFF": LightRestoreMode.LIGHT_RESTORE_DEFAULT_OFF,
    "RESTORE_DEFAULT_ON": LightRestoreMode.LIGHT_RESTORE_DEFAULT_ON,
    "ALWAYS_OFF": LightRestoreMode.LIGHT_ALWAYS_OFF,
    "ALWAYS_ON": LightRestoreMode.LIGHT_ALWAYS_ON,
    "RESTORE_INVERTED_DEFAULT_OFF": LightRestoreMode.LIGHT_RESTORE_INVERTED_DEFAULT_OFF,
    "RESTORE_INVERTED_DEFAULT_ON": LightRestoreMode.LIGHT_RESTORE_INVERTED_DEFAULT_ON,
    "RESTORE_AND_OFF": LightRestoreMode.LIGHT_RESTORE_AND_OFF,
    "RESTORE_AND_ON": LightRestoreMode.LIGHT_RESTORE_AND_ON,
}

modelrailway_ns = cg.esphome_ns.namespace("modelrailway")
ModelRailwayComponent = modelrailway_ns.class_(
    "ModelRailwayComponent", light.LightOutput, cg.Component
)

CONFIG_SCHEMA = cv.All(
    light.BINARY_LIGHT_SCHEMA.extend(
        {
            cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(ModelRailwayComponent),
            cv.Optional(CONF_NAME, default="Effect"): cv.string,
            cv.Optional(CONF_RESTORE_MODE, default="RESTORE_DEFAULT_OFF"): cv.enum(
                RESTORE_MODES, upper=True, space="_"
            ),
        }
    )
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    await cg.register_component(var, config)
    await light.register_light(var, config)
