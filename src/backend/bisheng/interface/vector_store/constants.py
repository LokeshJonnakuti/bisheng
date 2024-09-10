from bisheng.interface.vector_store.custom import (ElasticsearchWithPermissionCheck,
                                                   MilvusWithPermissionCheck)

CUSTOM_VECTORSTORE = {
    'MilvusWithPermissionCheck': MilvusWithPermissionCheck,
    'ElasticsearchWithPermissionCheck': ElasticsearchWithPermissionCheck
}
