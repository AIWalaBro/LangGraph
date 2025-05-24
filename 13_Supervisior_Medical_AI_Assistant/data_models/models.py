import re
from pydantic import BaseModel, Field, field_validator

class DateTimeModel(BaseModel):
    # keep the detail of the date parameter
    date: str = Field(description= "Properly formatted the date", pattern = r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$')

    @field_validator("date")
    def check_format_date(cls, v):
        if not re.match(r'^\d{2}-\d{2}-\d{4}-\d{2}-\d{2}$', v):
             raise ValueError("The date should not in correct format 'DD-MM-YYYY HH:MM")
        return v
    
class DateModel(BaseModel):
    date: str = Field(description = "Properly formatted date", pattern= r"\d{2}-\d{2}-\d{4}$")

    @field_validator("date")
    def check_fromat_date(cls, v):
        if not re.match(r"\d{2}-\d{2}-d{2}$", str(v)):
            raise ValueError("The date is not formatted in 'DD-MM-YYYY'")
        return v
    
class IdentificationNumberModel(BaseModel):
    id : int = Field(description = "The Identification number should be in 7 or 8 digit long")

    @field_validator("id")
    def check_format_id(cls, v):
        if re.match(r"\d{7,8}$", str(v)): # convert string before matching
            raise ValueError("The Id number provided that are (7-8 digit long)")
        return v
    