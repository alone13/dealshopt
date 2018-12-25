==================
Microservice: User
==================

Services performed processing CRUD for User

Endpoints
=========

Get user list
    :ref:`GET http://127.0.0.1:8000/user/user/ <get_user_list>`

Create a new user
    :ref:`POST http://127.0.0.1:8000/user/user/ <post_user>`

Get a user
    :ref:`GET http://127.0.0.1:8000/user/user/{id}/ <get_user>`

Update a user
    :ref:`PUT http://127.0.0.1:8000/user/user/{id}/ <put_user>`

Delete a user
    :ref:`DELETE http://127.0.0.1:8000/user/user/{id}/ <delete_user>`


.. _get_user_list:

Get user list
=============

GET http://127.0.0.1:8000/user/user/

.. _get_user_list_request:

Request
-------

::

    # Get 5 user and sort by latest added-date
    http://127.0.0.1:8000/user/user/?limit=5&sort=latest-added

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

.. _get_user_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://127.0.0.1:8000/user/user/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://127.0.0.1:8000/user/user/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "taikhoan_id": 1
            },
            {
                "id": 2,
                "taikhoan_id": 1
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
      - http://127.0.0.1:8000/user/user/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://127.0.0.1:8000/user/user/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of User <results_response>`


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
      - Id of User

    * - taikhoan_id
      - integer
      - 1
      - TaiKhoan_Id of TaiKhoan


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


.. _post_user:

Create a new user
=================

POST http://127.0.0.1:8000/user/user/

Request
-------

::

    POST http://127.0.0.1:8000/user/user/

    {
        "taikhoan_id": 1
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

    * - taikhoan_id
      - True
      - JSON
      - integer
      -
      - 0
      - TaiKhoan_Id of TaiKhoan

.. _user_response:

Response
--------

::

    {
        "id": 1,
        "taikhoan_id": 1
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
      - Id of User

    * - taikhoan_id
      - integer
      - 1
      - TaiKhoan_Id of TaiKhoan

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


.. _get_user:

Get a user
==========

GET http://127.0.0.1:8000/user/user/{id}/

.. _get_user_request:

Request
-------

::

    # Get a user
    http://127.0.0.1:8000/user/user/1/

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
      - ID of User

Response
--------

::

    {
        "id": 1,
        "taikhoan_id": 1
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST User response <user_response>`


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


.. _put_user:

Update a user
=============

PUT http://127.0.0.1:8000/user/user/{id}/

.. _put_user_request:

Request
-------

::

    # Update a user
    PUT http://127.0.0.1:8000/user/user/1/

    {
        "danhmuc_id": 10
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
      - Id of User

    * - taikhoan_id
      - True
      - Query string
      - integer
      -
      - 10
      - New taikhoan_Id of TaiKhoan

Response
--------

::

    {
        "id": 1,
        "taikhoan_id": 10
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST User response <user_response>`


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

.. _delete_user:

Delete a user
=============

DELETE http://127.0.0.1:8000/user/user/{id}/

Request
-------

::

    # Delete a user
    DELETE http://127.0.0.1:8000/user/user/1/

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
      - ID of User

.. _delete_user_response:

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
