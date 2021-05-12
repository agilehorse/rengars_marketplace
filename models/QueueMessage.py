from models.BaseModel import BaseModel
from models.QueueMessageType import QueueMessageType

id = '_id'
event_type = 'event_type'
payload = 'payload'


class QueueMessage(BaseModel):

    def __init__(self, new_id: int, new_event_type: QueueMessageType, new_payload: dict):
        self._data = {
            id: new_id,
            event_type: new_event_type,
            payload: new_payload
        }
