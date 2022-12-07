from graphene import *
from flask import Flask
from graphql_server.flask import GraphQLView


class Query(ObjectType) :
    hallo = Field(String)
    aanspreking = Field(String, naam = String(default_value=""))

    def resolve_aanspreking(parent, info, naam) :
        return "Dag " + naam

    def resolve_hallo(parent, info) :
        return "testje"

schema = Schema(query=Query)

result = schema.execute("{hallo}")
print(result)




myWebApp = Flask("My App")
myWebApp.add_url_rule('/graphql',
                    view_func=GraphQLView.as_view('graphql',
                                schema=schema,
                                graphiql=True)
                    )

@myWebApp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@myWebApp.route("/naam/<naam>")
def hello(naam):
    return "<p>Hello, " + naam + "</p>"

myWebApp.run()