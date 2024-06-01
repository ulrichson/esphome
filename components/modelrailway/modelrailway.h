#pragma once

#include "esphome/components/light/light_output.h"
#include "esphome/core/component.h"

namespace esphome
{
  namespace modelrailway
  {

    class ModelRailwayComponent : public Component, public LightOutput
    {

    private:
      constexpr static long INTERVAL_MS = 1000 /* ms */ / 30 /* fps */;
      constexpr static unsigned int LED_PIN0 = 0;
      constexpr static unsigned int LED_PIN1 = 1;
      constexpr static unsigned int LED_PIN2 = 2;
      constexpr static unsigned int LED_PIN3 = 3;
      constexpr static unsigned int DAMP_RANDOM_BUFFER_LENGTH = 128;

      int buffer[4][DAMP_RANDOM_BUFFER_LENGTH];
      int bufferIdx = 0;
      unsigned long currentMs = 0;
      unsigned long previousMs = 0;

      int setLight(int pin, int idx)
      {
        int intensity = int((avg(buffer[idx]) * dampFactor + float(random(minIntensity, 255)) * (1 - dampFactor)) / 2);

        analogWrite(pin, intensity);
        pop(idx);
        push(intensity, idx);

        return intensity;
      }

      boolean push(int element, int idx)
      {
        if (bufferIdx < DAMP_RANDOM_BUFFER_LENGTH)
        {
          buffer[idx][bufferIdx++] = element;
          return true;
        }

        return false;
      }

      int pop(int idx)
      {
        if (bufferIdx > 0)
          return buffer[idx][--bufferIdx];
        else
          return 0;
      }

      float avg(int values[])
      {
        int sum = 0;
        for (int i = 0; i < DAMP_RANDOM_BUFFER_LENGTH; i++)
        {
          sum += values[i];
        }
        return sum / DAMP_RANDOM_BUFFER_LENGTH;
      }

    public:
      bool enable = true;
      float dampFactor = 0.15f; // 0 .. 1, higher is more damped;
      int minIntensity = 160;

      ModelRailwayComponent() {}

      LightTraits get_traits() override
      {
        auto traits = LightTraits();
        traits.set_supports_brightness(false);
        return traits;
      }

      void write_state(LightState *state) override
      {
        state->current_values_as_binary(&enable);
      }

      void setup() override
      {
        pinMode(LED_PIN0, OUTPUT);
        pinMode(LED_PIN1, OUTPUT);
        pinMode(LED_PIN2, OUTPUT);
        pinMode(LED_PIN3, OUTPUT);
        digitalWrite(LED_PIN0, LOW);
        digitalWrite(LED_PIN1, LOW);
        digitalWrite(LED_PIN2, LOW);
        digitalWrite(LED_PIN3, LOW);
        for (int i = 0; i < 4; i++)
        {
          for (int j = 0; j < DAMP_RANDOM_BUFFER_LENGTH; j++)
          {
            buffer[i][j] = 0;
          }
        }
      }

      void loop() override
      {
        if (!enable)
        {
          digitalWrite(LED_PIN0, LOW);
          digitalWrite(LED_PIN1, LOW);
          digitalWrite(LED_PIN2, LOW);
          digitalWrite(LED_PIN3, LOW);
          return;
        }

        currentMs = millis();
        if (currentMs - previousMs >= INTERVAL_MS)
        {
          previousMs = currentMs;
          setLight(LED_PIN0, 0);
          setLight(LED_PIN1, 1);
          setLight(LED_PIN2, 2);
          setLight(LED_PIN3, 3);
        }
      }
    };
  }
}