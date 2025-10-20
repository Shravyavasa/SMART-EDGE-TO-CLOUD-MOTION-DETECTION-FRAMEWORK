#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char *ssid = "YOUR_SSID";
const char *password = "YOUR_PASSWORD";
const char *server = "http://<PI_IP>:5000/motion_trigger"; // Flask route on Pi
const int pirPin = D2;

void setup()
{
    Serial.begin(115200);
    pinMode(pirPin, INPUT);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED)
        delay(500);
}

void loop()
{
    if (digitalRead(pirPin) == HIGH)
    {
        HTTPClient http;
        http.begin(server);
        http.POST("");
        http.end();
        delay(10000); // wait before re-trigger
    }
}