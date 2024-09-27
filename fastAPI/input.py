from datetime import date
from pydantic import BaseModel, EmailStr, conlist, field_validator, model_validator, Field
from typing import Optional


class CreateEmployee(BaseModel):
    Operation_Cd: str
    Emp_Id: int
    Emp_First_Name: str
    Emp_Last_Name: str
    Emp_Job_Loc: str
    Emp_Join_Dt: date
    Emp_Email: EmailStr
    Emp_Phone: int
    Emp_Designation: str
    Emp_Skills: conlist(str)
    Emp_Project_Nm: str
    Emp_Project_Loc: str
    Emp_Manager_Nm: str
    Emp_Project_Join_Dt: date
    Emp_Blood_Grp: str
    Emp_Address: str
    Emp_Personal_Email: EmailStr
    Emp_Personal_Phone: int
    Emp_Father_Nm: str
    Emp_Mother_Nm: str
    Emp_Marital_Status: str = Field(default = 'N', description="Y for married, N for not married")
    Emp_Partner_Nm: Optional[str] = None

    @field_validator('Operation_Cd')
    def validate_operation_cd(cls, v):
        if v not in {'C', 'R', 'U', 'D'}:
            raise ValueError('Operation code must be C, R, U or D')
        return v

    @field_validator('Emp_Phone')
    def validate_emp_phone(cls, v):
        if not len(str(v)) == 10:
            raise ValueError('Phone number must be numeric and up to 10 digits')
        return v

    @field_validator('Emp_Personal_Phone')
    def validate_emp_personal_phone(cls, v):
        if not len(str(v)) == 10:
            raise ValueError('Phone number must be numeric and up to 10 digits')
        return v

    @model_validator(mode='after')
    def validate_emp_marital_status_and_partner_nm(cls, values):
        emp_marital_status = values.Emp_Marital_Status
        emp_partner_nm = values.Emp_Partner_Nm

        if emp_marital_status not in {'Y', 'N'}:
            raise ValueError('Marital Status must be Y or N')

        if emp_marital_status == 'Y' and not emp_partner_nm:
            raise ValueError('Partner name is required when marital status is Y')

        return values


class GetEmployee(BaseModel):
    Operation_Cd: str
    Emp_Id: int


class UpdateEmployee(BaseModel):
    Operation_Cd: str
    Emp_Id: int
    Emp_First_Name: Optional[str] = None
    Emp_Last_Name: Optional[str] = None
    Emp_Job_Loc: Optional[str] = None
    Emp_Join_Dt: Optional[date] = None
    Emp_Email: Optional[EmailStr] = None
    Emp_Phone: Optional[int] = None
    Emp_Designation: Optional[str] = None
    Emp_Skills: Optional[conlist(str)] = None
    Emp_Project_Nm: Optional[str] = None
    Emp_Project_Loc: Optional[str] = None
    Emp_Manager_Nm: Optional[str] = None
    Emp_Project_Join_Dt: Optional[date] = None
    Emp_Blood_Grp: Optional[str] = None
    Emp_Address: Optional[str] = None
    Emp_Personal_Email: Optional[EmailStr] = None
    Emp_Personal_Phone: Optional[int] = None
    Emp_Father_Nm: Optional[str] = None
    Emp_Mother_Nm: Optional[str] = None
    Emp_Marital_Status: Optional[str] = 'N'
    Emp_Partner_Nm: Optional[str] = None

    @field_validator('Operation_Cd')
    def validate_operation_cd(cls, v):
        if v not in {'C', 'R', 'U', 'D'}:
            raise ValueError('Operation code must be C, R, U or D')
        return v

    @field_validator('Emp_Phone')
    def validate_emp_phone(cls, v):
        if not len(str(v)) == 10:
            raise ValueError('Phone number must be numeric and up to 10 digits')
        return v

    @field_validator('Emp_Personal_Phone')
    def validate_emp_personal_phone(cls, v):
        if not len(str(v)) == 10:
            raise ValueError('Phone number must be numeric and up to 10 digits')
        return v

    @model_validator(mode='after')
    def validate_emp_marital_status_and_partner_nm(cls, values):
        emp_marital_status = values.Emp_Marital_Status
        emp_partner_nm = values.Emp_Partner_Nm

        if emp_marital_status not in {'Y', 'N'}:
            raise ValueError('Marital Status must be Y or N')

        if emp_marital_status == 'Y' and not emp_partner_nm:
            raise ValueError('Partner name is required when marital status is Y')

        return values


class DeleteEmployee(BaseModel):
    Operation_Cd: str
    Emp_Id: int
