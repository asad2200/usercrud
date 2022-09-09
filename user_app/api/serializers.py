from rest_framework import serializers
from user_app.models import UserModel, UserAddress

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['address_1', 'address_2', 'city', 'state', 'country', 'pincode']

class UserModelSerializer(serializers.ModelSerializer):
    # nested serializer of user address
    user_address = UserAddressSerializer()
    class Meta:
        model = UserModel
        fields = '__all__'
    
    def create(self, validated_data):
        """
            Popout user_address data from validate data and save user data.
            Then give user reference to useraddress
        """

        user_address = validated_data.pop('user_address')
        user = UserModel.objects.create(**validated_data)
        user_address = UserAddress.objects.create(user=user, **user_address)
        
        return user
    
    def update(self, instance, validated_data):
        """
            Check if user_address data is available then pop out it from validate data 
            then update both user_address and user data.
            if user_address is not available then only update user data.
        """

        if 'user_address' in validated_data:
            user_address_serializer = self.fields['user_address']
            user_address_data = validated_data.pop('user_address')
            user_address_serializer.update(instance.user_address, user_address_data)

        return super(UserModelSerializer, self).update(instance, validated_data)