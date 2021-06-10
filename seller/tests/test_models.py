import pytest

from seller.models import Seller, Address, Contact

pytestmark = pytest.mark.django_db

# class TestUsers:
#     pytestmark = pytest.mark.django_db
    
#     def test_my_user(self):
#         me = User.objects.get(username='admin')
#         assert me.is_superuser

@pytest.mark.django_db
class TestSeller:
    pytestmark = pytest.mark.django_db

    def test_um_novo_seller_com_todos_atributos_entao_deve_estar_no_bd(self):
        len_before = Seller.objects.all().count()
        Seller.objects.create(name="test", document="test", phone_number="test", email="test@test.com")
        
        len_after = Seller.objects.all().count()

        assert len_before < len_after
    
    
    def test_um_novo_seller_com_todos_atributos_entao_deve_estar_no_bd_2(self):
        len_before = Seller.objects.all().count()
        Seller.objects.create(name="test", document="test", phone_number="test", email="test@test.com")
        
        len_after = Seller.objects.all().count()

        assert len_before < len_after