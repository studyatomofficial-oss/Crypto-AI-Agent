import sys


class ProgressBar:

    def __init__(self, total: int):

        self.total = total

        self.width = 40

    def update(self, current: int):

        progress = current / self.total

        filled = int(self.width * progress)

        bar = (
            "█" * filled
            + "-" * (self.width - filled)
        )

        percent = progress * 100

        sys.stdout.write(
            f"\rScanning: [{bar}] "
            f"{percent:6.2f}% "
            f"({current}/{self.total})"
        )

        sys.stdout.flush()

    def finish(self):

        print()
