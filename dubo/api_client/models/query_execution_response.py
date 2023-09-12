import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.query_status import QueryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_execution_response_results_set_item import QueryExecutionResponseResultsSetItem


T = TypeVar("T", bound="QueryExecutionResponse")


@_attrs_define
class QueryExecutionResponse:
    """
    Attributes:
        id (str):
        start_time (datetime.datetime):
        status (QueryStatus): An enumeration.
        user_id (str):
        sql_text (str):
        data_source_id (str):
        cancellable (bool):
        end_time (Union[Unset, datetime.datetime]):
        error_message (Union[Unset, str]):
        user_query (Union[Unset, str]):
        thread_id (Union[Unset, str]):
        results_set (Union[Unset, List['QueryExecutionResponseResultsSetItem']]):
        row_count (Union[Unset, int]):
    """

    id: str
    start_time: datetime.datetime
    status: QueryStatus
    user_id: str
    sql_text: str
    data_source_id: str
    cancellable: bool
    end_time: Union[Unset, datetime.datetime] = UNSET
    error_message: Union[Unset, str] = UNSET
    user_query: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    results_set: Union[Unset, List["QueryExecutionResponseResultsSetItem"]] = UNSET
    row_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        start_time = self.start_time.isoformat()

        status = self.status.value

        user_id = self.user_id
        sql_text = self.sql_text
        data_source_id = self.data_source_id
        cancellable = self.cancellable
        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        error_message = self.error_message
        user_query = self.user_query
        thread_id = self.thread_id
        results_set: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results_set, Unset):
            results_set = []
            for results_set_item_data in self.results_set:
                results_set_item = results_set_item_data.to_dict()

                results_set.append(results_set_item)

        row_count = self.row_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start_time": start_time,
                "status": status,
                "user_id": user_id,
                "sql_text": sql_text,
                "data_source_id": data_source_id,
                "cancellable": cancellable,
            }
        )
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if user_query is not UNSET:
            field_dict["user_query"] = user_query
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if results_set is not UNSET:
            field_dict["results_set"] = results_set
        if row_count is not UNSET:
            field_dict["row_count"] = row_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_execution_response_results_set_item import QueryExecutionResponseResultsSetItem

        d = src_dict.copy()
        id = d.pop("id")

        start_time = isoparse(d.pop("start_time"))

        status = QueryStatus(d.pop("status"))

        user_id = d.pop("user_id")

        sql_text = d.pop("sql_text")

        data_source_id = d.pop("data_source_id")

        cancellable = d.pop("cancellable")

        _end_time = d.pop("end_time", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        error_message = d.pop("error_message", UNSET)

        user_query = d.pop("user_query", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        results_set = []
        _results_set = d.pop("results_set", UNSET)
        for results_set_item_data in _results_set or []:
            results_set_item = QueryExecutionResponseResultsSetItem.from_dict(results_set_item_data)

            results_set.append(results_set_item)

        row_count = d.pop("row_count", UNSET)

        query_execution_response = cls(
            id=id,
            start_time=start_time,
            status=status,
            user_id=user_id,
            sql_text=sql_text,
            data_source_id=data_source_id,
            cancellable=cancellable,
            end_time=end_time,
            error_message=error_message,
            user_query=user_query,
            thread_id=thread_id,
            results_set=results_set,
            row_count=row_count,
        )

        query_execution_response.additional_properties = d
        return query_execution_response

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
