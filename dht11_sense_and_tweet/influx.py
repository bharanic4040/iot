import argparse

from influxdb import InfluxDBClient


def main(temp, humid):
    """Instantiate a connection to the InfluxDB."""
    user = 'root'
    password = 'root'
    dbname = 'iot'
    dbuser = 'raspberry'
    dbuser_password = 'password'
    query = 'select temp_value,humid_value from temp_humid;'
    json_body = [
        {
            "measurement": "temp_humid",
            "fields": {
                "temp_value": temp,
                "humid_value":humid 
	}
        }
    ]

    client = InfluxDBClient('localhost', 8086, user, password, dbname)

    #client.create_database(dbname)

    print("Write points: {0}".format(json_body))
    client.write_points(json_body)

    #print("Querying data: " + query)
    #result = client.query(query)

    #print("Result: {0}".format(result))

    #client.drop_database(dbname)


def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--temp', type=str, required=True)
                      
    parser.add_argument('--humid', type=str, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(temp=args.temp, humid=args.humid)

