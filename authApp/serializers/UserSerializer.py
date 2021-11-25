from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'usu_nombres', 'usu_apellidos', 'usu_correo', 'usu_cargo', 'password']
    
    # def to_representation(self, obj):        
    #     usuario = User.objects.get(id=obj.id)
    #     return {
    #         'id': usuario.id,
    #         'usu_nombres': usuario.usu_nombres,
    #         'usu_apellidos': usuario.usu_apellidos,
    #         'usu_correo': usuario.usu_correo,
    #         'usu_cargo': usuario.usu_cargo,
    #     }