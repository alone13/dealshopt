==================
Microservice: Role
==================

Services performed processing CRUD for Role

Endpoints
=========

Get role list
    :ref:`GET http://localhost/admin/role/ <get_role_list>`

Create a new role
    :ref:`POST http://localhost/admin/role/ <post_role>`

Get a role
    :ref:`GET http://localhost/admin/role/{id}/ <get_role>`

Update a role
    :ref:`PUT http://localhost/admin/role/{id}/ <put_role>`

Delete a role
    :ref:`DELETE http://localhost/admin/role/{id}/ <delete_role>`


.. _get_role_list:

Get role list
=============

GET http://localhost/admin/role/

.. _get_role_list_request:

Request
-------

::

    # Get 5 role and sort by latest added-date
    http://localhost/admin/role/?limit=5&sort=latest-added

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - limit
      -
      - query string
      - integer
      - 5
      - 5
      - LIMIT number default to be acquired 5

    * - offset
      -
      - query string
      - integer
      - 0
      - 5
      - OFFSET of acquisition number

    * - sort
      -
      - query string
      - string
      - latest-added
      - latest-added
      - Sort by latest added date

.. _get_role_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://localhost/admin/role/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://localhost/admin/role/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "ten": "Role 1"
            },
            {
                "id": 2,
                "ten": "Role 2"
            },
            ...
        ]
    }

Response Format
^^^^^^^^^^^^^^^

Main
****

.. list-table::

    * - **name**
      - **data type**
      - **example**
      - **comment**

    * - count
      - integer
      - 5
      - Number of records returned

    * - current
      - url
      - http://localhost/admin/role/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://localhost/admin/role/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of Role <results_response>`


.. _results_response:

results
#######

.. list-table::

    * - **name**
      - **data type**
      - **example**
      - **comment**

    * - id
      - integer
      - 1
      - Id of Role

    * - ten
      - string
      - Role 1
      - Ten of Role

HTTP Response Status
^^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - **code**
    - **comment**

  * - 200
    - OK

  * - 400
    - BAD REQUEST

  * - 404
    - NOT FOUND

  * - 500
    - INTERNAL SERVER ERROR


.. _post_role:

Create a new role
=================

POST http://localhost/admin/role/

Request
-------

::

    POST http://localhost/admin/role/

    {
        "ten": "Role 1"
    }

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - ten
      - True
      - JSON
      - string
      -
      - Role 1
      - Ten of Role

.. _role_response:

Response
--------

::

    {
        "id": 1,
        "ten": "Role 1"
    }

Response Format
^^^^^^^^^^^^^^^

Main
****

.. list-table::

    * - **name**
      - **data type**
      - **example**
      - **comment**

    * - id
      - integer
      - 1
      - Id of Role

    * - ten
      - string
      - Role 1
      - Ten of Role

HTTP Response Status
^^^^^^^^^^^^^^^^^^^^


.. list-table::

  * - **code**
    - **comment**

  * - 201
    - CREATED

  * - 400
    - BAD REQUEST

  * - 500
    - INTERNAL SERVER ERROR


.. _get_role:

Get a role
==========

GET http://localhost/admin/role/{id}/

.. _get_role_request:

Request
-------

::

    # Get a role
    http://localhost/admin/role/1/

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - id
      - True
      - Query string
      - integer
      -
      - 1
      - ID of Role

Response
--------

::

    {
        "id": 1,
        "ten": "Role 1"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Role response <role_response>`


HTTP Response Status
^^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - **code**
    - **comment**

  * - 200
    - OK

  * - 400
    - BAD REQUEST

  * - 404
    - NOT FOUND

  * - 500
    - INTERNAL SERVER ERROR


.. _put_role:

Update a role
=============

PUT http://localhost/admin/role/{id}/

.. _put_role_request:

Request
-------

::

    # Update a role
    PUT http://localhost/admin/role/1/

    {
        "ten": "Role update"
    }

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - id
      - True
      - Query string
      - integer
      -
      - 1
      - ID of Role

    * - ten
      -
      - JSON
      - string
      -
      - Role update
      - New ten of Role

Response
--------

::

    {
        "id": 1,
        "ten": "Role update"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Role response <role_response>`


HTTP Response Status
^^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - **code**
    - **comment**

  * - 200
    - OK

  * - 400
    - BAD REQUEST

  * - 404
    - NOT FOUND

  * - 500
    - INTERNAL SERVER ERROR

.. _delete_role:

Delete a role
=============

DELETE http://localhost/admin/role/{id}/

Request
-------

::

    # Delete a role
    DELETE http://localhost/admin/role/1/

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - id
      - True
      - Query string
      - integer
      -
      - 1
      - ID of Role

.. _delete_role_response:

Response
--------

::

    Delete method is return status code only.

HTTP Response Status
^^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - **code**
    - **comment**

  * - 200
    - OK

  * - 400
    - BAD REQUEST

  * - 404
    - NOT FOUND

  * - 500
    - INTERNAL SERVER ERROR
