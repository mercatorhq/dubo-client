from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matched_doc import MatchedDoc


T = TypeVar("T", bound="PageMatchedDoc")


@_attrs_define
class PageMatchedDoc:
    """A generic page response.

    This is used to return a list of items with pagination information.

    The `data` field contains the list of items.
    The `next_page` field contains the next page number, or `None` if there is no next page.

        Attributes:
            data (List['MatchedDoc']):
            next_page (Union[Unset, int]):
    """

    data: List["MatchedDoc"]
    next_page: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        next_page = self.next_page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if next_page is not UNSET:
            field_dict["next_page"] = next_page

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.matched_doc import MatchedDoc

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MatchedDoc.from_dict(data_item_data)

            data.append(data_item)

        next_page = d.pop("next_page", UNSET)

        page_matched_doc = cls(
            data=data,
            next_page=next_page,
        )

        page_matched_doc.additional_properties = d
        return page_matched_doc

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
