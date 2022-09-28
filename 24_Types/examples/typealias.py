from typing import TypeAlias, Dict, List
# Note: prior to 3.10 you would omit the 'TypeAlias' annotation
# and just do Gradebook = Dict[...]

Gradebook: TypeAlias = Dict[str, Dict[int, List[float]]]

def ex_1() -> None:
    my_gradebook: Gradebook = get_gradebook_for_semester()
    print(my_gradebook)


#### Alternatively ####

StudentName: TypeAlias = str
TestId: TypeAlias = int
PointsPerQuestion: TypeAlias = List[float]
Gradebook2: TypeAlias = Dict[StudentName, Dict[TestId, PointsPerQuestion]]


def ex_2() -> None:
    my_gradebook: Gradebook2 = get_gradebook_for_semester2()
    print(my_gradebook)


def get_gradebook_for_semester() -> Gradebook:
    return {}

def get_gradebook_for_semester2() -> Gradebook2:
    return {}
