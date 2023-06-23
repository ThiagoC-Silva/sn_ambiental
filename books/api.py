from ninja import Router

router = Router()

@router.get('test/')
def test(request):
    return 1