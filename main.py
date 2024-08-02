from enum import Enum
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get('/{name}')
def greetings(
    name: str,
    surname: str,
    age: Optional[int] = None,
    is_staff: bool = False,
    education_level: Optional[EducationLevel] = None,
) -> dict[str, str]:
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
        result += ', ' + education_level.lower()
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}
