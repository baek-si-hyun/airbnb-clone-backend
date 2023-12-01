from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    # ModelViewSet은 두개의 프로퍼티를 필요로 한다
    # 첫번째는 serializer가 무엇인지 알아야한다. (serializers.py참고)
    # 두번쨰는 viewSet의 Object가 뭔지 알아야한다.
    # ViewSet은 Django REST framework에서 제공하는 클래스로, 데이터 모델에 대한 CRUD (Create, Retrieve, Update, Delete) 작업을 처리하는 데 사용된다.
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
