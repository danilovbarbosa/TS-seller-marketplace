import pytest

from django.urls import reverse
from django.test import Client

from seller.models import Seller, Address, Contact

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestSeller:
    pytestmark = pytest.mark.django_db

    def test_quando_um_novo_seller_com_todos_atributos_for_adicionado_no_bd_entao_a_tabela_deve_estar_com_mais_uma_linha(
        self,
    ):
        len_before = Seller.objects.all().count()
        Seller.objects.create(
            name="test", document="test", phone_number="test", email="test@test.com"
        )

        len_after = Seller.objects.all().count()

        assert len_before < len_after

    def test_quando_hover_requisicao_get_em_view_seller_list_entao_status_code__deve_ser_200(
        self,
    ):
        url = reverse("seller_list")

        client = Client()
        response = client.get(url)

        assert response.status_code == 200

    def test_quando_hover_requisicao_get_em_view_seller_update_entao_content__deve_ter_uma_string_pertencente_ao_user(
        self,
    ):
        # TODO: inserir valor do id automaticamente, de acordo com o que estiver presente na tabela.
        seller = Seller.objects.create(
            name="test", document="test", phone_number="test", email="test@test.com"
        )
        Address.objects.create(
            number="test",
            street="test",
            district="test",
            city="test",
            state="test",
            zip_code="test",
            seller=seller,
        )
        Contact.objects.create(number="test", seller=seller)

        url = reverse("seller_update", kwargs={"id": seller.id})

        client = Client()
        response = client.get(url)

        assert response.status_code == 200
        assert "test" in str(response.content)


@pytest.mark.django_db
class TestAddress:
    pytestmark = pytest.mark.django_db

    def test_quando_um_novo_address_com_todos_atributos_for_adicionado_no_bd_entao_a_tabela_deve_estar_com_mais_uma_linha(
        self,
    ):
        len_before = Address.objects.all().count()

        seller = Seller.objects.create(
            name="test", document="test", phone_number="test", email="test@test.com"
        )
        Address.objects.create(
            number="test",
            street="test",
            district="test",
            city="test",
            state="test",
            zip_code="test",
            seller=seller,
        )

        len_after = Address.objects.all().count()

        assert len_before < len_after


@pytest.mark.django_db
class TestContact:
    pytestmark = pytest.mark.django_db

    def test_quando_um_novo_contact_com_todos_atributos_for_adicionado_no_bd_entao_a_tabela_deve_estar_com_mais_uma_linha(
        self,
    ):
        len_before = Contact.objects.all().count()

        seller = Seller.objects.create(
            name="test", document="test", phone_number="test", email="test@test.com"
        )
        Contact.objects.create(number="test", seller=seller)

        len_after = Contact.objects.all().count()

        assert len_before < len_after
