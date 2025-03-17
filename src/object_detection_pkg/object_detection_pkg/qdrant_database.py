from qdrant_client import QdrantClient
import numpy as np

client = QdrantClient("localhost", port=6333)

def store_detection(label, bbox):
    vector = np.array([(bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2])
    client.upsert(
        collection_name="object_detections",
        points=[{
            "id": int(label),
            "vector": vector.tolist(),
            "payload": {"label": int(label)}
        }]
    )
