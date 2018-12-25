======================
Microservice: HoatDong
======================

Services performed processing CRUD for HoatDong

Endpoints
=========

Get hoatdong list
    :ref:`GET http://127.0.0.1:8000/admin/hoatdong/ <get_hoatdong_list>`

Create a new hoatdong
    :ref:`POST http://127.0.0.1:8000/admin/hoatdong/ <post_hoatdong>`

Get a hoatdong
    :ref:`GET http://127.0.0.1:8000/admin/hoatdong/{id}/ <get_hoatdong>`

Update a hoatdong
    :ref:`PUT http://127.0.0.1:8000/admin/hoatdong/{id}/ <put_hoatdong>`

Delete a hoatdong
    :ref:`DELETE http://127.0.0.1:8000/admin/hoatdong/{id}/ <delete_hoatdong>`


.. _get_hoatdong_list:

Get hoatdong list
=================

GET http://127.0.0.1:8000/admin/hoatdong/

.. _get_hoatdong_list_request:

Request
-------

::

    # Get 5 hoatdong and sort by latest added-date
    http://127.0.0.1:8000/admin/hoatdong/?limit=5&sort=latest-added

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

.. _get_hoatdong_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://127.0.0.1:8000/admin/hoatdong/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://127.0.0.1:8000/admin/hoatdong/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "ten": "Action 1"
            },
            {
                "id": 2,
                "ten": "Action 2"
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
      - http://127.0.0.1:8000/admin/hoatdong/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://127.0.0.1:8000/admin/hoatdong/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of HoatDong <results_response>`


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
      - Id of HoatDong

    * - ten
      - string
      - Action 1
      - Ten of HoatDong

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


.. _post_hoatdong:

Create a new hoatdong
=====================

POST http://127.0.0.1:8000/admin/hoatdong/

Request
-------

::

    POST http://127.0.0.1:8000/admin/hoatdong/

    {
        "ten": "Action 1"
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
      - Action 1
      - Ten of HoatDong

.. _hoatdong_response:

Response
--------

::

    {
        "id": 1,
        "ten": "Action 1"
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
      - Id of HoatDong

    * - ten
      - string
      - Action 1
      - Ten of HoatDong

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


.. _get_hoatdong:

Get a hoatdong
==============

GET http://127.0.0.1:8000/admin/hoatdong/{id}/

.. _get_hoatdong_request:

Request
-------

::

    # Get a hoatdong
    http://127.0.0.1:8000/admin/hoatdong/1/

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
      - ID of HoatDong

Response
--------

::

    {
        "id": 1,
        "ten": "Action 1"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST HoatDong response <hoatdong_response>`


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


.. _put_hoatdong:

Update a hoatdong
=================

PUT http://127.0.0.1:8000/admin/hoatdong/{id}/

.. _put_hoatdong_request:

Request
-------

::

    # Update a hoatdong
    PUT http://127.0.0.1:8000/admin/hoatdong/1/

    {
        "ten": "Action update"
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
      - ID of HoatDong

    * - ten
      -
      - JSON
      - string
      -
      - Action update
      - New ten of HoatDong

Response
--------

::

    {
        "id": 1,
        "ten": "Action update"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST HoatDong response <hoatdong_response>`


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

.. _delete_hoatdong:

Delete a hoatdong
=================

DELETE http://127.0.0.1:8000/admin/hoatdong/{id}/

Request
-------

::

    # Delete a hoatdong
    DELETE http://127.0.0.1:8000/admin/hoatdong/1/

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
      - ID of HoatDong

.. _delete_hoatdong_response:

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
