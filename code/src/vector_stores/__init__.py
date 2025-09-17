from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chroma import ChromaDatabase
    from .milvus import MilvusDatabase
    from .opengauss import OpenGaussDatabase
    from .opensearch import OpenSearchDatabase
    from .pgvector import PGVectorDatabase
    from .pinecone import PineconeDatabase
    from .qdrant import QdrantDatabase
    from .weaviate import WeaviateDatabase
