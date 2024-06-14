from dataclasses import dataclass

@dataclass
class ResponseMessage:
    message: str
    status_code: int = 200
    data: dict = None

@dataclass(init=False)
class ResponseBuilder:

    def add_status_code(self, status_code: int = 200):
        self.status_code = status_code
        return self
    
    def add_message(self, message:str):
        self.message = message
        return self
    
    def add_data(self, data: dict = None):
        self.data = data
        return self
    
    def build(self):
        return ResponseMessage(
            message=self.message,
            status_code=self.status_code,
            data=self.data
        )