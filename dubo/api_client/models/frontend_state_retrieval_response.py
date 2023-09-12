from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.frontend_state_retrieval_response_state import FrontendStateRetrievalResponseState


T = TypeVar("T", bound="FrontendStateRetrievalResponse")


@_attrs_define
class FrontendStateRetrievalResponse:
    """
    Attributes:
        state (FrontendStateRetrievalResponseState):
    """

    state: "FrontendStateRetrievalResponseState"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.frontend_state_retrieval_response_state import FrontendStateRetrievalResponseState

        d = src_dict.copy()
        state = FrontendStateRetrievalResponseState.from_dict(d.pop("state"))

        frontend_state_retrieval_response = cls(
            state=state,
        )

        frontend_state_retrieval_response.additional_properties = d
        return frontend_state_retrieval_response

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
