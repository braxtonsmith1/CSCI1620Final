import csv
from tkinter import messagebox


class Logic:
    def __init__(self, gui: "Gui") -> None:
        """Initializes logic for the GUI

        Args:
            gui (Gui): the GUI object
        """
        self.gui = gui
        self.data_file: str = 'data.csv'
        self.create_data_file_if_not_exists()

    def create_data_file_if_not_exists(self) -> None:
        """Opens/Creates the data.csv file for storing values"""
        try:
            with open(self.data_file, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Vote'])
        except FileExistsError:
            pass

    def submit_vote(self) -> None:
        """Takes the submission of a vote using validation"""
        user_id = self.gui.entry_id.get().strip()
        candidate = self.gui.vote_answer.get()

        # Validate ID input
        if not self.is_valid_id(user_id):
            self.gui.label_status.config(text="Please enter a valid ID!", fg='red')
            return

        if candidate == 0:
            messagebox.showwarning("Input Error", "Please select a candidate.")
            return

        if self.has_already_voted(user_id):
            self.gui.label_status.config(text="Already Voted", fg='red')
        else:
            self.record_vote(user_id, candidate)
            self.gui.label_status.config(text="Thank you for voting!", fg='green')

        self.clear_fields()  # Clear all fields after submission

    def is_valid_id(self, user_id: str) -> bool:
        """Takes the ID as long as it is an eight digit, positive, integer

        Args:
            user_id (str): The ID

        Returns:
            bool: Validation of ID
        """
        if len(user_id) == 8 and user_id.isdigit() and int(user_id) > 0:
            return True
        return False

    def has_already_voted(self, user_id: str) -> bool:
        """Checks to see if the ID has voted already

        Args:
            user_id (str): The ID

        Returns:
              bool: Validation of ID
        """
        try:
            with open(self.data_file, 'r') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                if header is None:
                    return False

                for row in reader:
                    if row[0] == user_id:
                        return True
        except FileNotFoundError:
            return False

        return False

    def record_vote(self, user_id: str, candidate: int) -> None:
        """Records the vote as well as the given ID

        Args:
            user_id (str): The ID
            candidate (int): The candidate to be voted for (1 or 2)
        """
        candidate_name = "Jane Doe" if candidate == 1 else "John Doe"
        with open(self.data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_id, candidate_name])

    def clear_fields(self) -> None:
        """Clears the GUI fields"""
        self.gui.entry_id.delete(0, 'end')
        self.gui.vote_answer.set(0)
