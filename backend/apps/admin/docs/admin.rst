===================
Microservice: Admin
===================

Services performed processing CRUD for Admin

Endpoints
=========

Get admin list
    :ref:`GET http://localhost/admin/admin/ <get_admin_list>`

Create a new admin
    :ref:`POST http://localhost/admin/admin/ <post_admin>`

Get a admin
    :ref:`GET http://localhost/admin/admin/{id}/ <get_admin>`

Update a admin
    :ref:`PUT http://localhost/admin/admin/{id}/ <put_admin>`

Delete a admin
    :ref:`DELETE http://localhost/admin/admin/{id}/ <delete_admin>`


.. _get_admin_list:

Get admin list
==============

GET http://localhost/admin/admin/

.. _get_admin_list_request:

Request
-------

::

    # Get 5 admin and sort by latest added-date
    http://localhost/admin/admin/?limit=5&sort=latest-added

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

.. _get_admin_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://localhost/admin/admin/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://localhost/admin/admin/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "taikhoan_id": "1"
            },
            {
                "id": 2,
                "taikhoan_id": "2"
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
      - http://localhost/admin/admin/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://localhost/admin/admin/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of Admin <results_response>`


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
      - Id of Admin

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


.. _post_admin:

Create a new admin
==================

POST http://localhost/admin/admin/

Request
-------

::

    POST http://localhost/admin/admin/

    {
        "taikhoan_id": "1"
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
      - 1
      - TaiKhoan_Id of TaiKhoan

.. _admin_response:

Response
--------

::

    {
        "id": 1,
        "taikhoan_id": "1"
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
      - Id of Admin

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


.. _get_admin:

Get a admin
===========

GET http://localhost/admin/admin/{id}/

.. _get_admin_request:

Request
-------

::

    # Get a admin
    http://localhost/admin/admin/1/

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
      - ID of Admin

Response
--------

::

    {
        "id": 1,
        "taikhoan_id": "1"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Admin response <admin_response>`


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


.. _put_admin:

Update a admin
==============

PUT http://localhost/admin/admin/{id}/

.. _put_admin_request:

Request
-------

::

    # Update a admin
    PUT http://localhost/admin/admin/1/

    {
        "taikhoan_id": "2"
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
      - ID of Admin

    * - taikhoan_id
      -
      - JSON
      - integer
      -
      - 2
      - New taikhoan_id of Admin

Response
--------

::

    {
        "id": 1,
        "taikhoan_id": "2"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Admin response <admin_response>`


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

.. _delete_admin:

Delete a admin
==============

DELETE http://localhost/admin/admin/{id}/

Request
-------

::

    # Delete a admin
    DELETE http://localhost/admin/admin/1/

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
      - ID of Admin

.. _delete_admin_response:

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
