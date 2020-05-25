from pathlib import Path


class Context:
    def __init__(self, base_path, user_id, datetime):
        self.base_path = Path(base_path)
        self.user_id = user_id
        self.datetime = datetime
        self.base_path.mkdir(parents=True, exist_ok=True)

    def path(self, filename):
        p = Path(self.base_path / str(self.user_id) / str(self.datetime))
        p.mkdir(parents=True, exist_ok=True)
        return p / filename
