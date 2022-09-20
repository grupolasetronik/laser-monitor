

from uuid import UUID


class InputMessageSerializer:
    def __init__(self,**kwargs):
        self.d = kwargs
        self.errors = []
        self.topic = None
        self.data = None
        self.valid = None

    def check_if_there_is_topic(self):

        ret = self.d.get("topic") is not None and self.d.get("topic") != ""
        if not ret:
            self.errors.append("Must include a topic key")
            return ret
        if not isinstance(self.d.get("topic"),str):
            self.errors.append("Must be a string")
            return ret
        self.topic = self.d.get("topic")
        return ret

    def check_if_there_is_data(self):
        ret = self.d.get("data") is not None
        self.data = self.d.get("data")
        if not ret:
            self.errors.append("Must include a data key")
        return ret

            

    def is_valid(self):
        ret = True
        ret &= self.check_if_there_is_topic()
        ret &= self.check_if_there_is_data()
        return ret
        

    def to_dict(self):
        return {
            "topic":self.topic,
            "data":self.data
        }

    