from crewai import Agent
import requests

class WeatherAgent(Agent):
    def __init__(self, name):
        super().__init__(name=name)
        self.history = []

    def respond(self, query):
        self.history.append(query)
        if "temperatura" in query.lower():
            temperatura = self.get_temperature()
            return f"A temperatura atual é {temperatura}°C"
        return "Desculpe, não entendi."

    def get_temperature(self):
        return 25
