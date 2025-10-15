class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✓" if self.done else "✕"
        return f"[{status}] {self.title}"