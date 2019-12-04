from rest_framework import serializers
from antisocial.api.models import User, NeighborHood, Business, Post, ContactInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = dict(
            password={
                'write_only': True,
                'required': True,
                'allow_null': False
            },
            email={
                'required': True,
                'allow_null': False
            },
            first_name={
                'required': True,
                'allow_null': False
            },
            last_name={
                'required': True,
                'allow_null': False
            }
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighborHood
        fields = '__all__'
        extra_kwargs = dict(
            name={
                'required': True,
                'allow_null': False
            },
            location={
                'required': True,
                'allow_null': False
            }
        )


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
        extra_kwargs = dict(
            facility={
                'required': True,
                'allow_null': False
            },
            phone_number={
                'required': True,
                'allow_null': False
            },
            email={
              'required': True,
              'allow_null': False
            }
        )
