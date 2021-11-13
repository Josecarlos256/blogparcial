import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from blogtech.models import Publicaciones

# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class PublicacionNode(DjangoObjectType):
    class Meta:
        model = Publicaciones
        filter_fields = ['titulo', 'cuerpo', 'fecha', 'autor']
        interfaces = (relay.Node, )



class Query(graphene.ObjectType):

    publicacion = relay.Node.Field(PublicacionNode)
    all_publicacion = DjangoFilterConnectionField(PublicacionNode)
