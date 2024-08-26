from fastapi import APIRouter, Body

from app.schemas.schemas import Person


router = APIRouter()


@router.post(
        '/hello',
        tags=['common methods'],
        summary='Общее приветствие',
        response_description='Полная строка приветствия',
)
def greetings(
    *,
    person: Person = Body(
        ...,
        examples=Person.Config.schema_extra['examples']
    ),
) -> dict[str, str]:
    if isinstance(person.surname, str):
        surnames = person.surname
    else:
        surnames = ' '.join(person.surname)
    result = ' '.join([person.name, surnames]).title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}
