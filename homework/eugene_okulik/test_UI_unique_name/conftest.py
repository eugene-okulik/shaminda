import pytest
from test_UI_unique_name.pages.regisration import RegistrationPage
from test_UI_unique_name.pages.eco_friendly import EcoFriendlyPage
from test_UI_unique_name.pages.sale import SalePage


@pytest.fixture
def registration(page):
    return RegistrationPage(page)

@pytest.fixture
def eco_friendly(page):
    return EcoFriendlyPage(page)

@pytest.fixture
def sale(page):
    return SalePage(page)
