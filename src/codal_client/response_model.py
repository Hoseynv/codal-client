class ResponseModel:
    def __init__(self, success, status_code, data=None, error_message=None):
        self.success = success
        self.status_code = status_code
        self.data = data
        self.error_message = error_message

    def __repr__(self):
        return (
            f"<ResponseModel "
            f"success={self.success}, "
            f"status_code={self.status_code}, "
            f"data_preview={str(self.data)}, "
            f"error_message={self.error_message!r}>"
        )