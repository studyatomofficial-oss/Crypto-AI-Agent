class ConsoleReporter:
    def report(self, snapshots) -> None:
        for snapshot in snapshots:
            print(snapshot)
