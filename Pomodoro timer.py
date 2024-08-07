import time

class PomodoroTimer:
    def __init__(self, work_duration=25, break_duration=5, cycles=4):
        """
        Initialize the Pomodoro timer.

        Args:
            work_duration (int): Duration of work intervals in minutes.
            break_duration (int): Duration of break intervals in minutes.
            cycles (int): Number of work/break cycles to complete.
        """
        self.work_duration = work_duration * 60  # Convert to seconds
        self.break_duration = break_duration * 60  # Convert to seconds
        self.cycles = cycles

    def start_timer(self, duration, message):
        """
        Start a timer for a given duration.

        Args:
            duration (int): Duration of the timer in seconds.
            message (str): Message to display when the timer ends.
        """
        print(f"Starting: {message}")
        time.sleep(duration)  # Sleep for the duration
        print(f"{message} is over!")

    def run(self):
        """Run the Pomodoro timer for the defined cycles."""
        for cycle in range(1, self.cycles + 1):
            print(f"\nCycle {cycle} of {self.cycles}")
            self.start_timer(self.work_duration, "Work session")
            if cycle < self.cycles:
                self.start_timer(self.break_duration, "Break time")

        print("\nAll cycles complete! Great job!")


if __name__ == "__main__":
    # Create a Pomodoro timer instance
    pomodoro = PomodoroTimer(work_duration=25, break_duration=5, cycles=4)
    
    # Start the Pomodoro timer
    pomodoro.run()