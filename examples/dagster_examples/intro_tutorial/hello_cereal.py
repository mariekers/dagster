import csv

from dagster import execute_pipeline, execute_solid, pipeline, solid 

@solid 
def hello_cereal(context):
    dataset_path = 'cereal.csv'
    with open(dataset_path, 'r') as fd:
        cereals = [row for row in csv.DictReader(fd)]

    context.log.info(
        'Found {n_cereals} cereals'.format(n_cereals=len(cereals))
    )

    return cereals 

