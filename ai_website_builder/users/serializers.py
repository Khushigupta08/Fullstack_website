from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate_email(self, value):
        if "example.com" in value:  # Example validation logic
            raise serializers.ValidationError("Emails from example.com are not allowed.")
        return value
