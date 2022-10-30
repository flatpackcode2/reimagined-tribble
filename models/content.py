from models.base_model import BaseModel
import peewee as pw



class Content(BaseModel):
    body = pw.TextField(null=False)

    def validate(self):
      if self.content=="":
        self.errors.append('Content cannot be empty')