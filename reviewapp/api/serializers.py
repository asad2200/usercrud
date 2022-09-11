from rest_framework import serializers
from reviewapp import models 

class ApartmentReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ApartmentReview
        exclude = ('apartment', 'user',)

    def create(self, validated_data):
        """
            Check if user has already given review for this apartment 
            then raise error
        """
        apartment_review = models.ApartmentReview.objects.filter(apartment=validated_data['apartment'], user=validated_data['user'])
        if apartment_review:
            raise serializers.ValidationError('User has already given review for this apartment.')
        return super().create(validated_data)
