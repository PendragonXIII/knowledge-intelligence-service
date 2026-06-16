from app.repository.object_resolver import ObjectResolver


repository_path = r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"


resolver = ObjectResolver(
    repository_path=repository_path
)


result = resolver.resolve_object(
    "EID.08"
)


print(result)