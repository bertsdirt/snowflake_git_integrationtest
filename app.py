from __future__ import annotations
from snowflake.snowpark.session import Session
from snowflake.snowpark import DataFrame
from snowflake.snowpark.functions import col

def hello(session: Session) -> DataFrame:
    df = session.table("SFDB_SBOX.DSANDD01.KB_PRICE_COND")
    return df
# return df.filter(col("SAP_SLS_ORG_CD") == 2000)

# For local debugging
if __name__ == "__main__":
    from snowflake.snowpark.mock.mock_connection import MockServerConnection
    import init_local

    session = Session(MockServerConnection())
    session = init_local.init(session)
    print(hello(session).show())
