import pytest

from seller.models import Seller, Address, Contact

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestSeller:
    pytestmark = pytest.mark.django_db

    def test_quando_um_novo_seller_com_todos_atributos_for_adicionado_no_bd_entao_a_tabela_deve_estar_com_mais_uma_linha(self):
        len_before = Seller.objects.all().count()
        Seller.objects.create(name="test", document="test", phone_number="test", email="test@test.com")
        
        len_after = Seller.objects.all().count()

        assert len_before < len_after
    
    
    def test_um_novo_seller_com_todos_atributos_entao_deve_estar_no_bd_2(self):
        len_before = Seller.objects.all().count()
        Seller.objects.create(name="test", document="test", phone_number="test", email="test@test.com")
        
        len_after = Seller.objects.all().count()

        assert len_before < len_after


@pytest.mark.django_db
class TestAddress:
    pytestmark = pytest.mark.django_db

    def test_quando_um_novo_address_com_todos_atributos_for_adicionado_no_bd_entao_a_tabela_deve_estar_com_mais_uma_linha(self):
        len_before = Address.objects.all().count()
        
        seller = Seller.objects.create(name="test", document="test", phone_number="test", email="test@test.com")
        Address.objects.create(number="test", street="test", district="test", city="test", state="test", zip_code="test", seller=seller)
        
        len_after = Address.objects.all().count()

        assert len_before < len_after



@pytest.mark.django_db
class TestContact:
    pytestmark = pytest.mark.django_db

    def test_quando_um_novo_contact_com_todos_atributos_for_adicionado_no_bd_entao_a_tabela_deve_estar_com_mais_uma_linha(self):
        len_before = Contact.objects.all().count()
        
        seller = Seller.objects.create(name="test", document="test", phone_number="test", email="test@test.com")
        Contact.objects.create(number="test", seller=seller)
        
        len_after = Contact.objects.all().count()

        assert len_before < len_after