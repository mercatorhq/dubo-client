from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_metadata import DatasetMetadata


T = TypeVar("T", bound="DatasetRetrievalResponse")


@_attrs_define
class DatasetRetrievalResponse:
    """
    Attributes:
        metadata (DatasetMetadata):
        url (str):
    """

    metadata: "DatasetMetadata"
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata = self.metadata.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset_metadata import DatasetMetadata

        d = src_dict.copy()
        metadata = DatasetMetadata.from_dict(d.pop("metadata"))

        url = d.pop("url")

        dataset_retrieval_response = cls(
            metadata=metadata,
            url=url,
        )

        dataset_retrieval_response.additional_properties = d
        return dataset_retrieval_response

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
