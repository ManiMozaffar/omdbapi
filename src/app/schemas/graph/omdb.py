import graphene


class Movie(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node, )

    imdbID = graphene.String()
    Title = graphene.String()
    Year = graphene.String()
    Type = graphene.String()
    Poster = graphene.String()


class MovieConnection(graphene.relay.Connection):
    class Meta:
        node = Movie

    total_count = graphene.Int()

    def resolve_total_count(root, info: graphene.ResolveInfo):
        return info.context.get("total_results")
