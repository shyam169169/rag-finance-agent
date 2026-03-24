

class MetricsService:
    def __init__(self):
        self.logs = []

    def log(self, data):
        self.logs.append(data)

metrics_service = MetricsService()