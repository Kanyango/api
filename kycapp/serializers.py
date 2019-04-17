from rest_framework import serializers

class MrzSerializers(serializers.Serializer):
    surname = serializers.CharField()
    sex = serializers.CharField(max_length=200)
    date_of_birth = serializers.CharField()
    optional2 = serializers.CharField()
