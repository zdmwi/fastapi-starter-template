from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def read_root():
    return {'hello': 'world'}
