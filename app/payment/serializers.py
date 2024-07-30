from rest_framework import serializers


def more_than_zero(value):
    if value <= 0:
        raise serializers.ValidationError('Only more than 0')


class IncomeUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    amount = serializers.IntegerField(
        required=True, validators=[more_than_zero])


class SpendUserSerializer(serializers.Serializer):
    amount = serializers.IntegerField(
        required=True, validators=[more_than_zero])
    partner_id = serializers.IntegerField(
        required=True, validators=[more_than_zero])
