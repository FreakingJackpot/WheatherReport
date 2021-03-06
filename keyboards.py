from telebot import types


class KeyboardBuilder:
    def mode_keyboard_maker(self):
        """Создаем клавиатуру для выбора города в списке"""
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                             resize_keyboard=True)
        current_weather_button = types.KeyboardButton("Текущая погода")
        five_day_weather_forecast_button = types.KeyboardButton(
            "Погода на 5 дней")
        keyboard.add(current_weather_button, five_day_weather_forecast_button)
        return keyboard

    def cities_list_keyboard_maker(self, count):
        """Создаем клавиатуру для выбора нужной функции"""
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                             resize_keyboard=True)
        buttons = [types.KeyboardButton(str(i + 1)) for i in range(count)]
        keyboard.add(*buttons)
        return keyboard