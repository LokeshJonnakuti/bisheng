from bisheng.api.v1.schemas import UnifiedResponseModel
from fastapi.exceptions import HTTPException


class BaseErrorCode:
    # 错误码前三位代表具体功能模块，后两位表示模块内部具体的报错。例如10001
    Code: int
    Msg: str

    @classmethod
    def return_resp(cls, msg: str = None, data: any = None) -> UnifiedResponseModel:
        return UnifiedResponseModel(status_code=cls.Code, status_message=msg or cls.Msg, data=data)

    @classmethod
    def http_exception(cls, msg: str = None) -> Exception:
        return HTTPException(status_code=cls.Code, detail=msg or cls.Msg)


class UnAuthorizedError(BaseErrorCode):
    Code: int = 403
    Msg: str = '暂无操作权限'
