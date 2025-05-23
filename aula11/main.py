import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class User:
    id: int
    name: str

fake_user_db = {"id": 1, "name": "John Doe"}

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        if id == fake_user_db["id"]:
            return User(id=id, name=fake_user_db["name"])
        return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def update_name(self, id: int, new_name: str) -> User:
        if id == fake_user_db["id"]:
            fake_user_db["name"] = new_name
            return User(id=id, name=new_name)
        raise Exception("Usuário não encontrado")

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
graphql_app = GraphQLRouter(schema, graphiql=True)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
