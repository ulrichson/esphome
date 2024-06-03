# Model Railway

Add following to the ESPHome Devide:

```yaml
external_components:
  - source: github://ulrichson/esphome@main
    components: [modelrailway]
    # refresh: 0s

modelrailway:
  # name: "Lichteffekt"
  # restore_mode: RESTORE_DEFAULT_OFF
```

- `name`: is optional and can be used to override the default name
- `restore_mode`: a custom restore mode
