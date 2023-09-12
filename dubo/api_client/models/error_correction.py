from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dubo_query import DuboQuery


T = TypeVar("T", bound="ErrorCorrection")


@_attrs_define
class ErrorCorrection:
    """
    Attributes:
        error (str):
        sql (str):
        dq (DuboQuery):
    """

    error: str
    sql: str
    dq: "DuboQuery"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        sql = self.sql
        dq = self.dq.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "sql": sql,
                "dq": dq,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dubo_query import DuboQuery

        d = src_dict.copy()
        error = d.pop("error")

        sql = d.pop("sql")

        dq = DuboQuery.from_dict(d.pop("dq"))

        error_correction = cls(
            error=error,
            sql=sql,
            dq=dq,
        )

        error_correction.additional_properties = d
        return error_correction

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
