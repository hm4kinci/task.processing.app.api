from bson import ObjectId
from common.database import MongoDBConnection
import logging


def run_scripts():
    db_connection = MongoDBConnection()
    database = db_connection.get_database()

    logging.info('db.seed.started')
    logging.info('collection.members.started')
    members = [
        {
            "_id": ObjectId("5fd590a1df3159da19b80c80"),
            "name": "John Smith",
            "email": "john@company1.com",
            "name_variations": [
                "john",
                "john s",
                "smith j"
            ],
            "organization_id": 1
        },
        {
            "_id": ObjectId("5fd590c7df3159da19b80c90"),
            "name": "Jeremy Graham",
            "email": "jeremy@company1.com",
            "name_variations": [
                "jeremy",
                "jeremy g",
                "graham j"
            ],
            "organization_id": 1
        },
        {
            "_id": ObjectId("5fd590eddf3159da19b80c9a"),
            "name": "Deborah Chapman",
            "email": "deborah@company1.com",
            "name_variations": [
                "deborah",
                "deborah c",
                "chapman d"
            ],
            "organization_id": 1
        },
        {
            "_id": ObjectId("5fd590f8df3159da19b80c9f"),
            "name": "Paul Day",
            "email": "paul@company1.com",
            "name_variations": [
                "paul",
                "paul d",
                "day p"
            ],
            "organization_id": 1
        },
        {
            "_id": ObjectId("5fd5910cdf3159da19b80ca9"),
            "name": "Jane Day",
            "email": "jane@company1.com",
            "name_variations": [
                "jane",
                "jane d",
                "day j"
            ],
            "organization_id": 1
        },
        {
            "_id": ObjectId("5fd5911bdf3159da19b80cac"),
            "name": "Matthew Clark",
            "email": "matt@company1.com",
            "name_variations": [
                "matthew",
                "matt",
                "matt c",
                "clark m",
                "matthew c"
            ],
            "organization_id": 1
        },
        {
            "_id": ObjectId("5fd59137df3159da19b80cb5"),
            "name": "Joe Doe",
            "email": "joe@company2.com",
            "name_variations": [
                "joe",
                "joe d",
                "doe j"
            ],
            "organization_id": 2
        },
        {
            "_id": ObjectId("5fd5913fdf3159da19b80cb8"),
            "name": "Benjamin Ballmer",
            "email": "benjamin@company2.com",
            "name_variations": [
                "benjamin",
                "benjamin b",
                "ballmer b",
                "ben b",
                "ben"
            ],
            "organization_id": 2
        },
        {
            "_id": ObjectId("5fd5914cdf3159da19b80cbe"),
            "name": "Christian Gates",
            "email": "chris@company2.com",
            "name_variations": [
                "chris",
                "christian",
                "christian g",
                "gates c"
            ],
            "organization_id": 2
        },
        {
            "name": "Heather Parks",
            "email": "heather@company2.com",
            "name_variations": [
                "heather",
                "heather p",
                "parks h"
            ],
            "organization_id": 2
        },
        {
            "name": "Ian Pearce",
            "email": "ian@company2.com",
            "name_variations": [
                "ian",
                "ian p",
                "pearce i"
            ],
            "organization_id": 2
        },
        {
          "name": "David Pearce",
          "email": "david@company2.com",
          "name_variations": [
              "david",
              "dave",
              "david p",
              "pearce d"
          ],
          "organization_id": 2
        },
        {
            "name": "Matthew Clark",
            "email": "matt@company2.com",
            "name_variations": [
                "matthew",
                "matt",
                "matt c",
                "clark m",
                "matthew c"
            ],
            "organization_id": 2
        }
    ]
    members_collection_name = 'members'
    database.drop_collection(members_collection_name)
    database.create_collection(members_collection_name)
    database[members_collection_name].insert_many(members)
    logging.info(f'collection.members.completed {len(members)} members added')

    logging.info('collection.projects.started')
    projects = [
        {
            "_id": ObjectId("5fd56d3adf3159da19b808a1"),
            "name": "Project Alpha",
            "code": "1_alpha",
            "name_variations": [
                'alpha', 'alpha project'
            ],
            "organization_id": 1
        },
        {
            "_id": ObjectId("5fd57c97df3159da19b80ab8"),
            "name": "Project Beta",
            "code": "1_beta",
            "name_variations": [
                "beta", "beta project"
            ],
            "organization_id": 1
        },
        {
            "name": "Project Theta",
            "code": "1_theta",
            "name_variations": [
                "theta", "theta project"
            ],
            "organization_id": 1
        },
        {
            "name": "Project Black",
            "code": "1_black",
            "name_variations": [
                "black", "black project"
            ],
            "organization_id": 1
        },
        {
            "_id": ObjectId("5fd59034df3159da19b80c5e"),
            "name": "Project Green",
            "code": "1_green",
            "name_variations": [
                "green", "green project"
            ],
            "organization_id": 2
        },
        {
            "_id": ObjectId("5fd5906ddf3159da19b80c6d"),
            "name": "Project Yellow",
            "code": "2_yellow",
            "name_variations": [
                "yellow", "yellow project"
            ],
            "organization_id": 2
        },
        {
            "_id": ObjectId("5fd5b2960db66a5ddd8c4dce"),
            "name": "Project Red",
            "code": "2_red",
            "name_variations": [
                "Red", "red project"
            ],
            "organization_id": 2
        },
        {
            "name": "Project Black",
            "code": "2_black",
            "name_variations": [
                "black", "black project"
            ],
            "organization_id": 2
        }
    ]
    projects_collection_name = 'projects'
    database.drop_collection(projects_collection_name)
    database.create_collection(projects_collection_name)
    database[projects_collection_name].insert_many(projects)
    logging.info(f'collection.projects.completed {len(projects)} projects added')
    logging.info('db.seed.completed')
