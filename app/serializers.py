from rest_framework import serializers
from .models import CustomUser, FamilyMember, ImportantDate, Store
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from .validators import mobile_phone_regex, telephone_regex, id_number_regex, zip_code_regex


class ObtainTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=128, allow_null=False)
    refresh = serializers.CharField(max_length=128, allow_null=False)
    created = serializers.BooleanField()



class CustomUserSerializer(serializers.ModelSerializer):
    mobile_phone = serializers.CharField(validators=[mobile_phone_regex])
    telephone_number = serializers.CharField(validators=[telephone_regex])
    id_number = serializers.CharField(validators=[id_number_regex])
    zip_code = serializers.CharField(validators=[zip_code_regex])
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'id_number', 'mobile_phone', 'telephone_number', 'address', 'zip_code', 'password')
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}



    def create(self, validated_data):
        user = CustomUser(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            id_number=validated_data.get('id_number'),
            mobile_phone=validated_data.get('mobile_phone'),
            telephone_number=validated_data.get('telephone_number', None),
            address=validated_data.get('address'),
            zip_code=validated_data.get('zip_code')
        )   
        user.set_password(validated_data.get('password'))
        user.save()
        return user


    def __init__(self, *args, **kwargs):
        super(CustomUser, self).__init__(*args, **kwargs)
        self.fields["Birth_date"]= JalaliDateField(
            label=("تاریخ تولد"),
            widget=AdminJalaliDateWidget)
    
class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model: Store
        fields = '__all__'


class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model: FamilyMember
        fields = '__all__'

class ImportantDateSerializer(serializers.ModelSerializer):

    class Meta:
        model: ImportantDate
        fields = '__all__'


