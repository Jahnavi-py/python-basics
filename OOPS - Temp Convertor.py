#Write a class TemperatureConverter with static methods to convert between Celsius and Fahrenheit.
class Temperature_Converter:
    @staticmethod
    def Celsius(temp):
        return (temp * 9/5) + 32
    @staticmethod
    def Fahrenheit(temp):
        return (temp - 32) * 5/9
print(f"The temperature in Fahrenheit is : {Temperature_Converter.Celsius(35)}")
print(f"The temperature in Celsius is : {Temperature_Converter.Fahrenheit(78)}")