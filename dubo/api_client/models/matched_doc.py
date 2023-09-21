from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchedDoc")


@_attrs_define
class MatchedDoc:
    """
    Attributes:
        body (str):
        score (float):
        matched_doc_id (Union[Unset, str]):
    """

    body: str
    score: float
    matched_doc_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        score = self.score
        matched_doc_id = self.matched_doc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "score": score,
            }
        )
        if matched_doc_id is not UNSET:
            field_dict["matched_doc_id"] = matched_doc_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body")

        score = d.pop("score")

        matched_doc_id = d.pop("matched_doc_id", UNSET)

        matched_doc = cls(
            body=body,
            score=score,
            matched_doc_id=matched_doc_id,
        )

        matched_doc.additional_properties = d
        return matched_doc

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
