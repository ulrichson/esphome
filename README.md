# Model Railway

Add following to the ESPHome Devide:

```yaml
external_components:
  - source: github://ulrichson/esphome@main
    components: [modelrailway]
    refresh: 0s

modelrailway:
  # name: "Lichteffekt"
```

- `name` is optional and can be used to override the default name
