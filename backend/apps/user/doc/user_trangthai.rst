============================
Microservice: User_TrangThai
============================

Services performed processing CRUD for User_TrangThai

Endpoints
=========

Get user_trangthai list
    :ref:`GET http://127.0.0.1:8000/user/user_trangthai/ <get_user_trangthai_list>`

Create a new user_trangthai
    :ref:`POST http://127.0.0.1:8000/user/user_trangthai/ <post_user_trangthai>`

Get a user_trangthai
    :ref:`GET http://127.0.0.1:8000/user/user_trangthai/{id}/ <get_user_trangthai>`

Update a user_trangthai
    :ref:`PUT http://127.0.0.1:8000/user/user_trangthai/{id}/ <put_user_trangthai>`

Delete a user_trangthai
    :ref:`DELETE http://127.0.0.1:8000/user/user_trangthai/{id}/ <delete_user_trangthai>`


.. _get_user_trangthai_list:

Get user_trangthai list
=======================

GET http://127.0.0.1:8000/user/user_trangthai/

.. _get_user_trangthai_list_request:

Request
-------

::

    # Get 5 user_trangthai and sort by latest added-date
    http://127.0.0.1:8000/user/user_trangthai/?limit=5&sort=latest-added

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

.. _get_user_trangthai_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://127.0.0.1:8000/user/user_trangthai/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://127.0.0.1:8000/user/user_trangthai/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "trangthai": "True"
            },
            {
                "id": 2,
                "trangthai": "False"
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
      - http://127.0.0.1:8000/user/user_trangthai/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://127.0.0.1:8000/user/user_trangthai/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of User_TrangThai <results_response>`


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
      - Id of User_TrangThai

    * - trangthai
      - boolean
      - True
      - TrangThai of User_TrangThai


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


.. _post_user_trangthai:

Create a new user_trangthai
===========================

POST http://127.0.0.1:8000/user/user_trangthai/

Request
-------

::

    POST http://127.0.0.1:8000/user/user_trangthai/

    {
        "trangthai": "True"
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

    * - trangthai
      - True
      - JSON
      - boolean
      -
      - True
      - TrangThai of User_TrangThai

.. _user_trangthai_response:

Response
--------

::

    {
        "id": 1,
        "trangthai": "True"
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
      - Id of User_TrangThai

    * - trangthai
      - boolean
      - True
      - TrangThai of User_TrangThai

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


.. _get_user_trangthai:

Get a user_trangthai
====================

GET http://127.0.0.1:8000/user/user_trangthai/{id}/

.. _get_user_trangthai_request:

Request
-------

::

    # Get a user_trangthai
    http://127.0.0.1:8000/user/user_trangthai/1/

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
      - ID of User_TrangThai

Response
--------

::

    {
        "id": 1,
        "trangthai": "True"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST User_TrangThai response <user_trangthai_response>`


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


.. _put_user_trangthai:

Update a user_trangthai
=======================

PUT http://127.0.0.1:8000/user/user_trangthai/{id}/

.. _put_user_trangthai_request:

Request
-------

::

    # Update a user_trangthai
    PUT http://127.0.0.1:8000/user/user_trangthai/1/

    {
        "trangthai": "False"
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
      - Id of User_TrangThai

    * - trangthai
      - True
      - Query string
      - boolean
      -
      - False
      - New trangthai of User_TrangThai

Response
--------

::

    {
        "id": 1,
        "trangthai": "False"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST User_TrangThai response <user_trangthai_response>`


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

.. _delete_user_trangthai:

Delete a user_trangthai
=======================

DELETE http://127.0.0.1:8000/user/user_trangthai/{id}/

Request
-------

::

    # Delete a user
    DELETE http://127.0.0.1:8000/user/user_trangthai/1/

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
      - ID of User_TrangThai

.. _delete_user_trangthai_response:

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
