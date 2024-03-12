from fastapi import FastAPI

# from pathParam import PathParam
# from pathParam import PathTypedParam
# from pathParam import OrderFirst
# from pathParam import SamePath
# from pathParam import EnumPathParam
# from pathParam import PathInPathParam
# from queryParam import DefaultValueQueryParam
# from queryParam import OptionalQueryParam
# from queryParam import TypeConversionQParam
# from queryParam import PathQueryParamTogether
# from queryParam import RequiredQueryParam
# from requestBody import SimpleReqBody
# from requestBody import UsingReqBody
# from requestBody import ReqBodyWithParam
# from requestBody import ReqBodyParamQuery
# from queryAnnotation import QueryParamValidation
# from queryAnnotation import MultipleQuery
# from queryAnnotation import QueryMetadata
# from pathAnnotation import PathMetadata
# from pathAnnotation import NumericValidation
# from bodyMultiParam import MultipleParam
# from bodyFields import MetaDataValidations
# from bodyNestedModels import ListFields
# from bodyNestedModels import Sets
# from bodyNestedModels import NestedModels
# from bodyNestedModels import SpecialTypesValidation
# from bodyNestedModels import DeeplyNestedModels
# from bodyNestedModels import BodyAsLists
from requestExample import WithReqExample

app = FastAPI()

app.include_router(WithReqExample.router)
# app.include_router(BodyAsLists.router)
# app.include_router(DeeplyNestedModels.router)
# app.include_router(SpecialTypesValidation.router)
# app.include_router(NestedModels.router)
# app.include_router(Sets.router)
# app.include_router(ListFields.router)
# app.include_router(MetaDataValidations.router)
# app.include_router(MultipleParam.router)
# app.include_router(NumericValidation.router)
# app.include_router(PathMetadata.router)
# app.include_router(QueryMetadata.router)
# app.include_router(MultipleQuery.router)
# app.include_router(QueryParamValidation.router)
# app.include_router(ReqBodyParamQuery.router)
# app.include_router(ReqBodyWithParam.router)
# app.include_router(UsingReqBody.router)
# app.include_router(SimpleReqBody.router)
# app.include_router(RequiredQueryParam.router)
# app.include_router(PathQueryParamTogether.router)
# app.include_router(TypeConversionQParam.router)
# app.include_router(OptionalQueryParam.router)
# app.include_router(DefaultValueQueryParam.router)
# app.include_router(PathInPathParam.router)
# app.include_router(EnumPathParam.router)
# app.include_router(SamePath.router)
# app.include_router(OrderFirst.router)
# app.include_router(PathTypedParam.router)
# app.include_router(PathParam.router)