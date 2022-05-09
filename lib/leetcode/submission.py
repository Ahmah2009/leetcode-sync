class Submission:
    def __init__(self, submission_dict):
        self.id = submission_dict["id"]
        self.lang = submission_dict["lang"]
        self.timestamp = submission_dict["timestamp"]
        self.code = submission_dict["code"]
        self.title_slug = submission_dict["title_slug"]
        self.title = submission_dict["title"]
