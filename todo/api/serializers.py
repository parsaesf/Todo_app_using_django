from rest_framework import serializers
from todo.models import TODOO
from django.contrib.auth.models import User






class TodoSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")
    class Meta:
        model = TODOO
        read_only_fields = ["user"]
        fields = [
            "title",
            "date",
            "status",
            "user",
            "absolute_url",
        ]
        

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get("request")
        rep =  super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url',None)
        else:
            rep.pop('date',None)
        
        return rep
    

    def create(self, validated_data):
        # Get the Profile instance associated with the current user
        user = User.objects.get(id=self.context.get("request").user.id)
        validated_data["user"] = user
        return super().create(validated_data)