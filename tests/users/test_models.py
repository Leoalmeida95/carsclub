# Third

from mongoengine import (
    BooleanField,
    StringField
)

# Apps

from apps.users.models import User, Car


class TestUser:

    def setup_method(self):
        self.data_user = {
            'email': 'teste1@teste.com', 'password': 'teste123',
            'active': True, 'full_name': 'Teste',
            'cpf_cnpj': '11111111111',
        }

        self.data_car = {
            'color': 'red', 'value': 10000,
            'mileage': 0, 'number_ports': 2, 'user': self.data_user
        }

        # Crio uma instancia do modelo User
        self.user = User(**self.data_user)
        self.car = Car(**self.data_car)

    def test_model_user_email_field_exists(self):
        """
        Verifico se o campo email existe
        """
        assert 'email' in self.user._fields

    def test_model_user_email_field_is_required(self):
        """
        Verifico se o campo email é requirido
        """
        assert self.user._fields['email'].required is True

    def test_model_user_email_field_is_unique(self):
        """
        Verifico se o campo email é unico
        """
        assert self.user._fields['email'].unique is True

    def test_model_user_email_field_is_str(self):
        """
        Verifico se o campo email é do tipo string
        """
        assert isinstance(self.user._fields['email'], StringField)

    def test_model_user_active_field_exists(self):
        assert 'active' in self.user._fields

    def test_model_user_active_field_is_default_true(self):
        assert self.user._fields['active'].default is False

    def test_model_user_active_field_is_bool(self):
        """
        Verifico se o campo active é booleano
        """
        assert isinstance(self.user._fields['active'], BooleanField)

    def test_model_user_full_name_field_exists(self):
        """
        Verifico se o campo full_name existe
        """
        assert 'full_name' in self.user._fields

    def test_model_user_full_name_field_is_str(self):
        assert isinstance(self.user._fields['full_name'], StringField)

    def test_model_user_function_is_active(self):
        is_active = getattr(self.user, 'is_active')
        assert hasattr(is_active, '__call__'), 'o is_active deve ser invocável'

    def test_model_user_function_is_admin(self):
        is_admin = getattr(self.user, 'is_admin')
        assert hasattr(is_admin, '__call__'), 'o is_admin deve ser invocável'

    def test_model_user_all_fields_in_user(self):
        """
        Verifico se todos os campos estão de fato no meu modelo
        """
        fields = [
            'active', 'cpf_cnpj', 'created', 'email',
            'full_name', 'id', 'password', 'roles'
        ]

        user_keys = [i for i in self.user._fields.keys()]

        fields.sort()
        user_keys.sort()

        assert fields == user_keys

    def test_model_car_field_color_exists(self):
        assert 'color' in self.car._fields

    def test_model_car_field_brand_exists(self):
        assert 'brand' in self.car._fields

    def test_model_car_field_model_exists(self):
        assert 'model' in self.car._fields

    def test_model_car_field_value_exists(self):
        assert 'value' in self.car._fields

    def test_model_car_field_mileage_exists(self):
        assert 'mileage' in self.car._fields

    def test_model_car_field_number_ports_exists(self):
        assert 'number_ports' in self.car._fields

    def test_model_car_field_number_fuel_exists(self):
        assert 'fuel' in self.car._fields

    def test_model_car_field_number_user_exists(self):
        assert 'user' in self.car._fields

    def test_model_car_color_field_is_required(self):
        assert self.car._fields['color'].required is True

    def test_model_car_value_field_is_required(self):
        assert self.car._fields['value'].required is True

    def test_model_car_number_ports_field_is_required(self):
        assert self.car._fields['number_ports'].required is True

    def test_model_car_user_ports_field_is_required(self):
        assert self.car._fields['user'].required is True
