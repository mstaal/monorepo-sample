from fastapi import APIRouter
from lib_x.generic_module.nested_module.cool_logic import square_root


router = APIRouter(
    prefix="/path_a",
)


@router.get("/api")
async def root():
    x = 16
    result = square_root(x)
    return {"message": f"The square root of {x} is {result}"}
