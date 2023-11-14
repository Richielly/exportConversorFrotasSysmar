import datetime
from collections import deque

class BuildCache:
    def __init__(self, cache_size=100):
        self.cache = deque(maxlen=cache_size)
        self.time_data = {}

    def increment_seconds(self, input_time):
        # Verifica se a data e hora estão no formato correto
        try:
            input_datetime = datetime.datetime.strptime(input_time, "%d/%m/%Y %H:%M")
        except ValueError:
            return "Formato de data e hora inválido."

        # Verifica se a data e hora já estão no cache
        if input_datetime in self.time_data:
            self.time_data[input_datetime] += datetime.timedelta(seconds=1)

            # Ajusta os minutos e horas, se necessário
            if self.time_data[input_datetime].second >= 60:
                self.time_data[input_datetime] = self.time_data[input_datetime].replace(second=0, minute=self.time_data[input_datetime].minute + 1)

        else:
            # Se não estiver no cache, começa com 0 segundos
            self.time_data[input_datetime] = input_datetime
            self.cache.append(input_datetime)

        return self.time_data[input_datetime].strftime("%d/%m/%Y %H:%M:%S")