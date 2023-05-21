from string import Template
from faker import Faker


fake = Faker()


def create_fake_query(default_name=None, limit=10, skip=0):
    template_string = Template("""
query {
    movies(Title: "$title", Limit: $limit, Skip: $skip) {
        edges {
            node {
                imdbID
                Title
                Year
                Type
                Poster
            }
        }
        totalCount
    }
}""")
    if default_name is None:
        return template_string.substitute(
            title=fake.word(), limit=limit, skip=skip
        )
    else:
        return template_string.substitute(
            title=default_name, limit=limit, skip=skip
        )
