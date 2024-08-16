from tkinter import *
from typing import Optional


class Gui:
    def __init__(self, window: Tk) -> None:
        """Initializes the GUI

        Args:
            window (Tk): The root window
        """
        self.window = window
        self.logic: Optional["Logic"] = None

        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, text='Cast Your Vote!', font=('', 15))
        self.label_title.pack()
        self.frame_title.pack(pady=20)

        self.frame_id = Frame(self.window)
        self.label_id = Label(self.frame_id, text='ID:', font=('', 10))
        self.entry_id = Entry(self.frame_id, width=20)
        self.label_id.pack(side=LEFT, padx=5)
        self.entry_id.pack(side=LEFT, padx=5)
        self.frame_id.pack(pady=20)

        self.frame_votes = Frame(self.window)
        self.vote_answer = IntVar()
        self.vote_answer.set(0)
        self.label_votes = Label(self.frame_votes, text='Candidates:', font=('', 10))
        self.radio_jane = Radiobutton(self.frame_votes, text='Jane Doe', variable=self.vote_answer, value=1, font=('', 10))
        self.radio_john = Radiobutton(self.frame_votes, text='John Doe', variable=self.vote_answer, value=2, font=('', 10))
        self.label_votes.pack(side=LEFT)
        self.radio_jane.pack(side=LEFT)
        self.radio_john.pack(side=LEFT)
        self.frame_votes.pack(pady=20)

        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.frame_submit, text='Submit Vote', command=self.submit)
        self.button_submit.pack()
        self.frame_submit.pack(pady=20)

        self.frame_status = Frame(self.window)
        self.label_status = Label(self.frame_status, text='Click "Submit Vote" To Cast Your Ballot!', font=('', 10))
        self.label_status.pack()
        self.frame_status.pack(pady=20)

    def set_logic(self, logic: "Logic") -> None:
        """Sets logic for the GUI

        Args:
            logic (Logic): is the logic for casting votes
        """

        self.logic = logic

    def submit(self) -> None:
        """Submits the vote using the logic object."""
        if self.logic:
            self.logic.submit_vote()
