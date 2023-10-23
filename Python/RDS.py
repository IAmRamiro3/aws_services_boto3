import boto3

def create_rds_instance(
        AllocatedStorage, 
        DBInstanceClass, 
        DBInstanceIdentifier, 
        Engine, 
        MasterUserPassword, 
        MasterUsername
    ):
    client = boto3.client('rds')
    response = client.create_db_instance(
        AllocatedStorage=AllocatedStorage,
        DBInstanceClass=DBInstanceClass,
        DBInstanceIdentifier=DBInstanceIdentifier,
        Engine=Engine,
        MasterUserPassword=MasterUserPassword,
        MasterUsername=MasterUsername
    )
    return response

def modify_rds_instance_password(DBInstanceIdentifier, NewMasterUserPassword):
    client = boto3.client('rds')
    response = client.modify_db_instance(
        DBInstanceIdentifier=DBInstanceIdentifier,
        MasterUserPassword=NewMasterUserPassword
    )
    return response

def describe_rds_instances(DBInstanceIdentifier):
    client = boto3.client('rds')
    filters = [
        {
            'Name': 'engine',
            'Values': ['MySQL']
        }
    ]
    if DBInstanceIdentifier:
        filters.append({
            'Name': 'db-instance-id',
            'Values': [DBInstanceIdentifier]
        })

    response = client.describe_db_instances(Filters=filters)
    return response

def delete_rds_instance(DBInstanceIdentifier, SkipFinalSnapshot=True):
    client = boto3.client('rds')
    response = client.delete_db_instance(
        DBInstanceIdentifier=DBInstanceIdentifier,
        SkipFinalSnapshot=SkipFinalSnapshot
    )
    return response


## EXAMPLES ##


create_rds_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='database-instance-01',
    Engine='MySQL',
    MasterUserPassword='testpw0021',
    MasterUsername='admin01'
)

modify_rds_instance_password('database-instance-01', 'new-pa$$word')

describe_rds_instances('database-instance-01')

delete_rds_instance('database-instance-01-readreplica', SkipFinalSnapshot=True)