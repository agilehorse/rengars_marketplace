from models.BaseModel import BaseModel


class QueueMessageType(BaseModel):
    """
    allowed enum values
    """
    JOB_OFFER_CREATED = 'JOB_OFFER_CREATED'
    JOB_OFFER_UPDATED = 'JOB_OFFER_UPDATED'
