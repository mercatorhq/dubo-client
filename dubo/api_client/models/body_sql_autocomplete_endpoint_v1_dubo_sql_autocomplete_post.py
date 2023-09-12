from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.autocomplete_request_body import AutocompleteRequestBody
    from ..models.dubo_query import DuboQuery


T = TypeVar("T", bound="BodySqlAutocompleteEndpointV1DuboSqlAutocompletePost")


@_attrs_define
class BodySqlAutocompleteEndpointV1DuboSqlAutocompletePost:
    """
    Attributes:
        dq (DuboQuery):
        autocomplete (AutocompleteRequestBody):
    """

    dq: "DuboQuery"
    autocomplete: "AutocompleteRequestBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dq = self.dq.to_dict()

        autocomplete = self.autocomplete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dq": dq,
                "autocomplete": autocomplete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.autocomplete_request_body import AutocompleteRequestBody
        from ..models.dubo_query import DuboQuery

        d = src_dict.copy()
        dq = DuboQuery.from_dict(d.pop("dq"))

        autocomplete = AutocompleteRequestBody.from_dict(d.pop("autocomplete"))

        body_sql_autocomplete_endpoint_v1_dubo_sql_autocomplete_post = cls(
            dq=dq,
            autocomplete=autocomplete,
        )

        body_sql_autocomplete_endpoint_v1_dubo_sql_autocomplete_post.additional_properties = d
        return body_sql_autocomplete_endpoint_v1_dubo_sql_autocomplete_post

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
