# pynamodb-study
- the study of pythonic interface for amazon's dynamodb
- reference: https://pynamodb.readthedocs.io/en/stable/tutorial.html#why-pynamodb

## pynamodb
- 3개의 `api levels`
  - `connection` , `tableconnection`, `model`

## model
- hah_key: partition_key
  - hash_key에 callable, value를 지정할 수 있음
- sort_key: range_key
- dynamodb는 기본적으로 null 값을 저장하지 않음
  - null 값을 지정하려면 `null=True`
### meta
- table_name
- region
- host
- rcu
- wcu


## Index
- `projection` attribute 필요
- rcu, wcu 명시
- index_name
### gsi
- TODO
### lsi
- TODO
### querying an index
- TODO
### pagination and last evaluated key
- 쿼리는 `ResultIterator`object 리턴
- 객체를 지연평가(generator)하고 싶으면 `last_evaluated_key`


## Batch
- 배치는 context manager를 이용한 동작
- 다이나모디비는 25개의 요청밖에 보내지 못하기 때문에 context manager 사용

## Update Operations
- updateitem은 upsert로 동작 

## Conditional Expression
- TODO

## Polymorphism
- discriminators


## Custom Attributes
- 모든 `Atrribute` 클래스들은 세개의 메소드를 정의해야 됨
  - `serialize`, `deserialize`, `get_value`
### List Attributes
- TODO
### Map Attributes
- TODO

## Optimistic locking
> 자원에 락을 걸어서 선점하지말고, 동시성 문제가 발생하면 그때 가서 처리
- 낙관적 잠금은 데이터베이스 쓰기가 다른 사용자의 쓰기에 의해 덮어쓰기되지 않도록 하는 전략
- version의 상태를 보고 충돌을 확인
충돌이 확인된 경우 롤백을 진행시킴
- db단에서 동시성 처리가 아닌, 어플리케이션단에서 처리
- 글로벌 테이블(여러 리전)을 사용하는 경우 잠금이 제대로 작동 안 할 수 있음