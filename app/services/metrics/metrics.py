

class MetricsService:
    def __init__(self):
        self.logs = []

    def log(self, data):
        self.logs.append(data)

    def get_all_logs(self):
        return self.logs

metrics_service = MetricsService()