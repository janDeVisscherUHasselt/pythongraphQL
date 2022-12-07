from graphene import *
from flask import Flask
from graphql_server.flask import GraphQLView

def showSomething(request):
    return "hallo"

class KleinType(ObjectType) :
    naam = Field(String)
    getal = Field(Int)

object1 = KleinType(naam = "mezelf")
object2 = KleinType(naam = "andere mezelf")

kleineObjecten = [object1, object2]
ding = TypeMetLijst(naam="vb", dingekes = kleineObjecten)


class AndereType(ObjectType):
    andereNaam = Field(String)
    kleinObject = Field(KleinType)

class TypeMetLijst(ObjectType):
    naam = Field(String)
    dingekes = Field(List(KleinType))

complexObject = AndereType(andereNaam = "buh")

class Query(ObjectType) :
    hallo = Field(String)
    aanspreking = Field(String, naam = String(default_value=""))

    def resolve_aanspreking(parent, info, naam) :
        return "Dag " + naam

    def resolve_hallo(parent, info) :
        return "testje"

    getObject1 = Field(KleinType)
    def resolve_getObject1(parent, info):
        return object1

    getComplexObject = Field(KleinType)
    def resolve_getComplexObject(parent, info):
        return complexObject

schema = Schema(query=Query)

result = schema.execute("{hallo}")
print(result)

myWebApp = Flask("My App")
myWebApp.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@myWebApp.route("/")
def hello_world():
    return "<p>Hello World!<p>"

@myWebApp.route("/naam/<naam>")
def hello(naam):
    return "<p>Hello: " + naam + "<p>"

myWebApp.run()