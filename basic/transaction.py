from pynamodb.models import Model
from pynamodb.attributes import BooleanAttribute, NumberAttribute, UnicodeAttribute
from pynamodb.connection import  Connection
from pynamodb.transactions import TransactWrite


class BankStatement(Model):
    class Meta:
        table_name = 'BankStatement'

    user_id = UnicodeAttribute(hash_key=True)
    account_balance = NumberAttribute(default=0)
    is_active = BooleanAttribute()

# connection - requried
# client_request-token
# return-consumed-capacity
# return-item-collection-metrics
"""
what is clientRequestToken
Providing a ClientRequestToken makes the call to TransactWriteItems idempotent, meaning that multiple identical calls have the same effect as one single call.
"""


user1_statement = BankStatement("user1" ,account_balance= 2000, is_active=True)
user2_statement = BankStatement('user2', account_balance=0, is_active=True)

connection = Connection()

with TransactWrite(connection=connection, client_request_token="super-unique-key") as transaction:
   transfer_amount = 1000
   transaction.update(
       BankStatement(user_id="user1"),
       actions=[BankStatement.account_balance.add(transfer_amount * -1)],
       condition= (
           (BankStatement.account_balance >= transfer_amount) &
           (BankStatement.isactive == True)
       )
   )
   transaction.update(
       BankStatement(user_id="user2"),
       actions=[BankStatement.account_balance.add(transfer_amount)],
       condition = (BankStatement.isactive == True)
   )

user1_statement.refresh()
user2_statement.refresh()
