select *
from places
where host_id in (
    SELECT host_id
    from places
    group by host_id
    having count(id)>=2
)
order by id;
