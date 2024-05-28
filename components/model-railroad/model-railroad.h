#include "esphome.h"

#define LED_PIN0 0
#define LED_PIN1 1;
#define LED_PIN2 2;
#define LED_PIN3 3;
#define DAMP_RANDOM_BUFFER_LENGTH 128;

class ModelRailroadComponent : public Component
{
public:
  ModelRailroadComponent() {}

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
    setLight(LED_PIN0, 0);
    setLight(LED_PIN1, 1);
    setLight(LED_PIN2, 2);
    setLight(LED_PIN3, 3);
    delay(1000 /* ms */ / 30 /* fps */);
  }

private:
  const float DAMP_FACTOR = 0.15f; // 0 .. 1, higher is more damped;
  const int MIN_INTENSITY = 160;

  int buffer[4][DAMP_RANDOM_BUFFER_LENGTH];
  int bufferIdx = 0;

  int setLight(int pin, int idx)
  {
    int intensity = int((avg(buffer[idx]) * DAMP_FACTOR + float(random(MIN_INTENSITY, 255)) * (1 - DAMP_FACTOR)) / 2);

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
};
